# Dynamic CV Application with Django

## Project Description

This is a web application built with Python and Django that dynamically generates a professional CV/resume. Instead of using a static HTML file, this project leverages Django's MVT (Model-View-Template) architecture to create a maintainable and scalable personal portfolio page.

All content—from personal profiles and work experience to education and skills—is stored in a database and can be easily managed through Django's built-in admin interface without ever touching the source code.

## Features

- **Dynamic Content:** The CV is rendered dynamically from database content.
- **Database-Driven:** Uses SQLite3 (Django's default) to store all CV information.
- **Admin Management:** Provides a secure admin panel for all CRUD (Create, Read, Update, Delete) operations on your CV data.
- **Structured Data:** Employs Django models to define a clear and logical structure for professional information (Profile, Experience, Education, Skills).
- **Clean and Maintainable:** Separates logic (views), data structure (models), and presentation (templates) for a clean codebase.

## Technology Stack

- **Backend:** Python 3, Django 4.x
- **Database:** SQLite 3 (Default)
- **Frontend:** HTML5

## Project Structure

A brief overview of the key files in this project:

## Setup and Installation

Follow these steps to get the project running on your local machine.

### 1. Prerequisites

- Python 3.8 or newer
- `pip` package manager

### 2. Clone the Repository

Clone this project to your local machine.
```bash
git clone https://github.com/nirmal141/cv-to-html_django.git
cd cv_to_html
```

### 3. Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install dependencies
```bash
pip install -r requirements.txt
```

### 5. Apply database migrations
```bash
python manage.py migrate
```
### 6. Create a superuser

```bash
python manage.py createsuperuser
```

### 7. Start the dev server
```bash
python manage.py runserver
```

### 8. Access the admin panel and add whatever resume data you want to add

- Navigate to http://127.0.0.1:8000/admin/ in your web browser
- Login using the superuser credentials you created earlier
- In the admin dashboard, you will see sections for Profiles, Experiences, Educations, and Skills.
- Important: You must add at least one Profile object and populate the other sections with sample data for the CV to render correctly.

### 9. View your CV

- Once you have added data through the admin panel, navigate to the home page: https://127.0.0.1:8000/
- This will display the CV, rendered with the data you entered.