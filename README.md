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

4. **Start the development server:**
   ```bash
   python manage.py runserver
   ```

5. **View your CV:**
   Open your browser and go to: http://127.0.0.1:8000/

## Project Structure

```
cv_to_html/
├── manage.py                    # Django management script
├── requirements.txt             # Python dependencies
├── cv/
│   ├── apps.py                 # App configuration
│   ├── urls.py                 # URL routing
│   ├── views.py                # CV data and view logic (EDIT THIS!)
│   └── templates/cv/
│       └── resume.html         # HTML template with styling
└── cv_project/
    ├── settings.py             # Minimal Django settings
    ├── urls.py                 # Main URL configuration
    └── wsgi.py                 # WSGI configuration for deployment
```

