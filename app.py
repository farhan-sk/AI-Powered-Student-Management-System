import smtplib
from email.mime.text import MIMEText
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, login_required, logout_user, UserMixin
from datetime import datetime
import qrcode
import os
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')

db = SQLAlchemy(app)
login_manager = LoginManager(app)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    roll_no = db.Column(db.String(50), unique=True)
    student_class = db.Column(db.String(50))
    marks = db.Column(db.Integer)
    attendance = db.Column(db.Float)
    contact = db.Column(db.String(100))

class ChatLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    query = db.Column(db.String(500))
    response = db.Column(db.String(500))
    timestamp = db.Column(db.DateTime, default=datetime.now)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.before_first_request
def create_tables():
    db.create_all()

def send_email(subject, body, to_email):
    print("DEBUG: Attemping to send email...")
    from_email = 'sfarhan3592@gmail.com'
    from_password = os.environ.get('GMAIL_APP_PASSWORD')

    if not from_password:
        print("DEBUG: FALAT-Email password not found in environment variables.")
        return
    
    try:
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = from_email
        msg['To'] = to_email

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        print("DEBUG: Connected to SMTP server. Login in...")
        server.login(from_email, from_password)
        print("DEBUG: Login successful. Sending message...")
        server.send_message(msg)
        print("DEBUG: Email sent successfully!")
        server.quit()
    except Exception as e:
        print(f"DEBUG: FALAT-An error occurred: {e}")


@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username, password=password).first()
        if user:
            login_user(user)
            return redirect(url_for('dashboard'))
        flash('Invalid credentials')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/dashboard')
@login_required
def dashboard():
    students = Student.query.all()
    return render_template('dashboard.html', students=students)

@app.route('/add_student', methods=['GET', 'POST'])
@login_required
def add_student():
    if request.method == 'POST':
        name = request.form['name']
        roll_no = request.form['roll_no']
        student_class = request.form['student_class']
        marks = request.form['marks']
        attendance = request.form['attendance']
        contact = request.form['contact']

        new_student = Student(
            name=name,
            roll_no=roll_no,
            student_class=student_class,
            marks=int(marks),
            attendance=float(attendance),
            contact=contact
        )
        db.session.add(new_student)
        db.session.commit()

        qr_data = f"Name: {name}, Roll No: {roll_no}, Class: {student_class}"
        qr_img = qrcode.make(qr_data)
        qr_folder = 'static/qr_codes'
        os.makedirs(qr_folder, exist_ok=True)
        qr_img.save(f'{qr_folder}/{roll_no}.png')

        send_email(
            subject="New Student Added",
            body=f"Student {name} (Roll No: {roll_no}) has been successfully added.",
            to_email="sfarhan3592@gmail.com"
        )

        flash('Student added successfully!')
        return redirect(url_for('dashboard'))

    return render_template('add_student.html')

@app.route('/delete_student/<int:id>')
@login_required
def delete_student(id):
    student = Student.query.get(id)
    if student:
        db.session.delete(student)
        db.session.commit()
        flash('Student deleted successfully!')
    return redirect(url_for('dashboard'))

@app.route('/chatbot', methods=['GET', 'POST'])
@login_required
def chatbot():
    response = None
    if request.method == 'POST':
        user_query = request.form['query']
        responses = [
            "I'm here to help!",
            "Please provide more details.",
            "Check the attendance section.",
            "Contact admin@example.com for further help."
        ]
        response = random.choice(responses)

        new_log = ChatLog(query=user_query, response=response, timestamp=datetime.now())
        db.session.add(new_log)
        db.session.commit()

    return render_template('chatbot.html', response=response)

if __name__ == '__main__':
    app.run(debug=True)
