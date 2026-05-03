# 🚀 Team Task Manager

A full-stack web application that allows users to create projects, assign tasks, and track progress with role-based access.

---

## 📌 Project Overview

Team Task Manager is designed to help teams manage their work efficiently.  
Users can create projects, assign tasks, update task status, and monitor overall progress through a dashboard.

This project demonstrates full-stack development using Flask, database integration, and real-world application logic.

---

##  Features

-  User Authentication (Signup & Login)
-  Role-based access (Admin / Member)
-  Project creation and management
-  Task creation and assignment
-  Task status update (Pending → Completed)
-  Dashboard with task statistics
-  Clean and modern user interface

---

##  Tech Stack

**Backend:**
- Python
- Flask
- Flask-SQLAlchemy

**Frontend:**
- HTML
- CSS

**Database:**
- SQLite

**Deployment:**
- Railway

---

## 📂 Project Structure

```

team-task-manager/
│
├── app.py              # Main Flask application
├── models.py           # Database models
├── requirements.txt    # Dependencies
├── Procfile            # Deployment configuration
├── .gitignore          # Ignored files
│
├── templates/          # HTML files
│   ├── login.html
│   ├── dashboard.html
│
├── static/             # CSS files
│   └── style.css

```

---

##  How the App Works

### 1. User Authentication
- Users can sign up with name, email, password, and role
- Login verifies credentials and redirects to dashboard

### 2. Project Management
- Users can create projects
- Each project is linked to a user

### 3. Task Management
- Tasks can be created with:
  - Title
  - Description
  - Deadline
  - Assigned user
  - Project ID
- Tasks are initially marked as **Pending**

### 4. Task Updates
- Users can mark tasks as **Completed**
- Status updates dynamically on dashboard

### 5. Dashboard
Displays:
- Total tasks
- Completed tasks
- Pending tasks
- List of all tasks

---

##  Testing

The application was tested for:

- ✅ Successful signup and login
- ✅ Duplicate email handling
- ✅ Project creation
- ✅ Task creation and updates
- ✅ Dashboard accuracy
- ✅ No application crashes

---

##  Live Demo
 
*team-task-manager-production-1407.up.railway.app*

---

## 📸 Demo Video

*https://drive.google.com/file/d/1GGHjYgDmfmWj8Jv3hKXf7M48hdfWQg9t/view?usp=sharing*

---

##  How to Run Locally

1. Clone the repository:
```

git clone (https://github.com/akhilmaddi2004/team-task-manager.git)

```

2. Navigate to project folder:
```

cd team-task-manager

```

3. Install dependencies:
```

pip install -r requirements.txt

```

4. Run the app:
```

python app.py

```

5. Open in browser:
```

(http://127.0.0.1:5000)

```

---

##  Important Notes

- Virtual environment (venv) is not included in repository
- Database is auto-created when the app runs
- Basic validation implemented for user inputs

---

##  Future Improvements

- Password encryption (security)
- User sessions & logout
- Better role-based restrictions
- Dropdown selection for users/projects
- Improved UI with JavaScript
- Search and filtering features

---

##  Conclusion

This project demonstrates the complete development of a full-stack web application, including backend APIs, database integration, frontend UI, testing, and deployment.

It provides a strong foundation for building real-world scalable applications.

---
