
# MoebiusTech Django App

This folder contains the main Django application for the MoebiusTech project, a platform for managing products, contractors, and user-driven project cost estimation. The app provides APIs and web views for interacting with products, questions, choices, contractors, and search results.

## Project Overview

MoebiusTech is designed to help users estimate project costs, find contractors, and manage reviews and product details. The application supports:

- Product and service management
- Dynamic question and choice system for cost estimation
- Contractor registration and expertise matching
- Search and filtering for contractors based on user input and location
- Review and rating system for products
- Admin interface for managing all data

## Features

- REST API endpoints for products, questions, choices, and contractors
- Web views for user interaction and cost estimation
- Customizable forms and templates
- Automated matching of contractors to user needs
- Admin dashboard for data management

## Folder Structure

- `models.py`: Database models for products, questions, choices, contractors, results, etc.
- `views.py`: API and web views for user and admin interaction
- `serializer.py`: Serializers for API data exchange
- `forms.py`: Django forms for user input
- `admin.py`: Admin interface configuration
- `urls.py`: URL routing for the app
- `tests.py`: Unit tests
- `migrations/`: Django migration files
- `templates/`: HTML templates for the app

## Installation

1. **Clone the repository:**
   ```sh
   git clone <your-repo-url>
   cd moebiustech
   ```

2. **Create and activate a virtual environment:**
   ```sh
   python -m venv venv
   venv\Scripts\activate  # On Windows
   # Or
   source venv/bin/activate  # On macOS/Linux
   ```

3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Apply migrations:**
   ```sh
   python manage.py migrate
   ```

5. **Create a superuser (for admin access):**
   ```sh
   python manage.py createsuperuser
   ```

6. **Run the development server:**
   ```sh
   python manage.py runserver
   ```

7. **Access the app:**
   - User interface: http://127.0.0.1:8000/
   - Admin dashboard: http://127.0.0.1:8000/admin/

## Configuration

- Edit `settings.py` for database, static files, and other Django settings as needed.
- Add or update environment variables for production deployments.

## License

This project is for internal use at MoebiusTech. Contact the project owner for licensing details.
