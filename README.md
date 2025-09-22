# 📚 AI-Powered Student Management System

---

## ✅ Project Overview

This project is a **Student Management System** built using the Python Flask framework.

It provides a user-friendly interface to manage student records in a simple and efficient way.  
Key features include:
- User Authentication (Login/Logout)
- Add, View, Delete student records
- QR Code generation for each student (for easy identification)
- Email notification when a new student is added
- Simple Chatbot interface for basic help
- Beautiful Frontend Styling using CSS
- Fully prepared for Deployment (Heroku supported)

---

## ✅ Detailed Features

1️⃣ **User Authentication**
   - Secure login system using Flask-Login
   - Sessions managed automatically
   - Only logged-in users can add or delete students

2️⃣ **Student Record Management**
   - Add new student with details: Name, Roll No, Class, Marks, Attendance, Contact
   - Automatically generate a unique QR Code for each student containing their basic info
   - View list of students in a table format
   - Delete unwanted student records

3️⃣ **QR Code Generation**
   - For every new student added, a QR code image is created and stored in `static/qr_codes/`
   - QR Code contains info: Name, Roll Number, Class
   - Helps in easy identification during physical record checks

4️⃣ **Email Notifications**
   - When a new student is added, an automatic email alert is sent to admin email
   - Email includes the student’s basic info for easy reference

5️⃣ **Simple Smart Chatbot**
   - Chatbot interface to assist user in navigating the system
   - Provides helpful responses based on predefined rules
   - Example usage: User types "How to add a student?" → Chatbot replies "Go to Add Student page and fill the form."

6️⃣ **Frontend Styling**
   - Clean and simple CSS design
   - Easy to use and mobile responsive
   - Links to static `style.css` and `script.js`

7️⃣ **Deployment-Ready**
   - Built to be deployed on Heroku
   - Includes `Procfile`, `runtime.txt`, `requirements.txt` for deployment setup

---

## ✅ Installation Guide (Step by Step)

### ✅ Step 1: Clone the Project
```bash
git clone <Your GitHub Repo URL>
