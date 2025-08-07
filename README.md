# meu_blog_final

This is a Django project named "meu_blog_final" designed to create a functional blog application. The project includes an app called "posts" that manages blog posts and displays them on the homepage.

## Project Structure

```
meu_blog_final/
├── manage.py               # Command-line utility for interacting with the project
├── meu_blog_final/         # Main project directory
│   ├── __init__.py         # Indicates that this directory is a Python package
│   ├── asgi.py             # ASGI configuration for asynchronous server communication
│   ├── settings.py         # Project settings and configuration
│   ├── urls.py             # URL patterns for the project
│   └── wsgi.py             # WSGI configuration for web server communication
├── posts/                  # Blog posts application
│   ├── __init__.py         # Indicates that this directory is a Python package
│   ├── admin.py            # Admin site configuration for managing blog posts
│   ├── apps.py             # Configuration for the posts app
│   ├── migrations/          # Database migrations for the posts app
│   │   └── __init__.py     # Indicates that this directory is a Python package
│   ├── models.py           # Data models for blog posts
│   ├── tests.py            # Tests for the posts app
│   ├── urls.py             # URL patterns for the posts app
│   ├── views.py            # Views for the posts app
│   └── templates/          # HTML templates for the posts app
│       └── posts/
│           └── post_list.html # Template for rendering the list of blog posts
└── README.md               # Documentation for the project
```

## Setup Instructions

1. **Clone the repository** (if applicable):
   ```
   git clone <repository-url>
   cd meu_blog_final
   ```

2. **Create a virtual environment**:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```
   pip install django
   ```

4. **Run migrations**:
   ```
   python manage.py migrate
   ```

5. **Create a superuser** (for admin access):
   ```
   python manage.py createsuperuser
   ```

6. **Run the development server**:
   ```
   python manage.py runserver
   ```

7. **Access the blog**:
   Open your web browser and go to `http://127.0.0.1:8000/` to view the homepage with the list of posts.

## Functionality

- The homepage displays a list of blog posts.
- Administrative management of posts is available through the Django admin interface.
- The project is structured to allow for easy expansion and customization.