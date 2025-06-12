# EECE430 Project: Employee Task Management System

This Django-based web application provides a comprehensive system to manage employees, their basic information, assigned tasks, progress tracking, and internal announcements. It is ideal for academic or prototype use in human resources and management systems.

## ✨ Features

- ✅ Employee registration with detailed personal and professional info
- 📁 Upload employee documents and photos
- 🗂 Task creation, assignment, and progress updates
- 📅 Calendar event management
- 📢 Post and view announcements
- 🔍 Search and list employee profiles
- 🧑‍💼 Role-based access to data (employee vs admin views)

---

## 📦 Tech Stack

- Python 3.x
- Django Web Framework
- SQLite3 (default DB)
- HTML/CSS (Django templates)
- Bootstrap (UI styling)

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/EECE430-project.git
cd EECE430-project
```

### 2. Create & Activate Virtual Environment

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

> If `requirements.txt` is empty, you can install Django manually:

```bash
pip install django
```

### 4. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Run the Server

```bash
python manage.py runserver
```

Then visit [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.

---

## 📂 Project Structure

```
EECE430-project/
├── manage.py
├── db.sqlite3
├── requirements.txt
├── myapp3/
│   ├── models.py            # Data models (Employee, Task, Event, Announcement)
│   ├── views.py             # View logic for all pages
│   ├── forms.py             # Form classes for user input
│   ├── templates/myapp3/    # HTML templates
│   └── static/              # CSS, JS, images
```

---

## 🧠 Core Models

- **Employee**: Stores name and email.
- **Basic_Employee_Information**: Full profile with contract, degree, specialization, contact info, and documents.
- **Task**: With progress, status, and assignment to employees.
- **Event**: Used in the calendar system.
- **Announcement**: General notices to all or selected employees.

---

## 📅 Calendar Events

- Add, update, and delete events dynamically via the UI.
- Rendered in a calendar format.
- Integrated with `fullcalendar.js` and Django views.

---

## 👨‍💼 Admin Panel

To use the Django admin interface:

```bash
python manage.py createsuperuser
```

Then login at:  
[http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

---

## 📝 Contributors

This project was developed as part of the EECE430 course at the American University of Beirut (AUB).

---

## 📃 License

This project is intended for educational purposes only. Use freely with proper credit.
