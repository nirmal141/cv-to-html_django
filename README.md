# CV to HTML Django Project

A simple Django web application that displays a professional CV/resume.

## Quick Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/nirmal141/cv-to-html_django.git
   cd cv_to_html
   ```

2. **Create and activate virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Django:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run database migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Start the development server:**
   ```bash
   python manage.py runserver
   ```

6. **View the CV:**
   Open your browser and go to: http://127.0.0.1:8000/

## Project Structure

- `cv/views.py` - Contains all the CV data and view logic
- `cv/templates/cv/resume.html` - HTML template for the CV
- `cv_project/settings.py` - Django settings
- `manage.py` - Django management script

