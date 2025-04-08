# KcalCall - Calorie Tracking Application

## Overview
KcalCall is a Django-based web application designed to help users track their daily calorie intake and calculate their nutritional needs. The application allows users to select food items, track their consumption, and calculate personalized calorie requirements based on individual metrics.

## Features
- **Food Tracking**: Add and remove food items from your daily consumption log
- **Calorie Counter**: View total calories consumed against your daily goal
- **Nutritional Calculator**: Calculate personalized calorie and macronutrient needs based on:
  - Age
  - Gender
  - Height
  - Weight
  - Activity level
- **Nutritional Breakdown**: View detailed macronutrient (protein, fat) recommendations
- **Responsive Design**: Built with Bootstrap for a mobile-friendly experience

## Technologies Used
- **Backend**: Django 5.1.5
- **Database**: SQLite
- **Frontend**: HTML, CSS, JavaScript
- **UI Framework**: Bootstrap 5
- **Icons**: Bootstrap Icons

## Installation

### Prerequisites
- Python 3.x
- pip (Python package manager)

### Setup Instructions

1. Clone the repository
   ```
   git clone https://github.com/yourusername/KcalCall.git
   cd KcalCall
   ```

2. Create and activate a virtual environment (optional but recommended)
   ```
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. Install dependencies
   ```
   pip install -r requirements.txt
   ```

4. Run database migrations
   ```
   python manage.py migrate
   ```

5. Create a superuser (for admin access)
   ```
   python manage.py createsuperuser
   ```

6. Start the development server
   ```
   python manage.py runserver
   ```

7. Access the application at http://127.0.0.1:8000/

## Usage

### Home Page
- Select food items from the dropdown menu and add them to your daily log
- View your consumed calories against your daily goal
- Remove food items from your log as needed

### Calculator
- Enter your personal metrics (age, gender, height, weight, activity level)
- Get personalized calorie and macronutrient recommendations
- View detailed breakdown of daily and weekly calorie needs

### Admin Interface
- Access the admin interface at http://127.0.0.1:8000/admin/
- Add, edit, or remove food items from the database
- Manage user accounts

## Project Structure
```
Calorie_Track/
├── calorie/              # Main Django project folder
│   ├── settings.py       # Project settings
│   ├── urls.py           # Main URL configuration
│   └── wsgi.py           # WSGI configuration
├── track/                # Main application folder
│   ├── models.py         # Data models (Food, Consume)
│   ├── views.py          # View functions
│   ├── urls.py           # App URL configuration
│   └── templates/        # HTML templates
│       ├── home.html     # Home page template
│       ├── calculator.html # Calculator page template
│       ├── result.html   # Results page template
│       └── contact.html  # Contact page template
├── static/               # Static files (CSS, JS, images)
├── manage.py             # Django management script
└── requirements.txt      # Project dependencies
```

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## Contact
For any questions or suggestions, please use the contact form in the application.