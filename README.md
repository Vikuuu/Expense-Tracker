# **Expense Tracker**

Welcome to Expense Tracker! This repository contains the backend code for an expense and income tracking application built with Django and Django Rest Framework. Expense Tracker allows users to manage their expenses and incomes, with features including authentication, email account verification, password reset via email, and CRUD operations for both expenses and incomes.

## Features

- **Authentication**: Users can register, login, and logout securely.
- **Email Account Verification**: New users are required to verify their email addresses before accessing the application.
- **Password Reset by Email**: Users can reset their passwords via email if they forget them.
- **Expense CRUD**: Users can create, retrieve, update, and delete expenses.
- **Income CRUD**: Users can create, retrieve, update, and delete incomes.
- **Swagger Documentation**: The API endpoints are documented using Swagger.
- **Social Authentication**: Users can sign in using Google, Facebook, and Twitter accounts.

## Technologies Used

- **Django**: A high-level Python web framework that encourages rapid development and clean, pragmatic design.
- **Django Rest Framework (DRF)**: A powerful and flexible toolkit for building Web APIs in Django.
- **Swagger**: An open-source software framework backed by a large ecosystem of tools that helps developers design, build, document, and consume RESTful Web services.
- **Google API Python Client**: Python library for accessing Google's APIs.
- **Facebook SDK**: Python library for interacting with Facebook's Graph API.
- **python-twitter**: Python library for accessing Twitter's API.

## Setup Instructions

To set up Expense Tracker locally, follow these steps:

1. Clone this repository to your local machine:

```bash
git clone https://github.com/Vikuuu/Expense-Tracker.git
```

2. Navigate to the project directory:

```bash
cd Expense_Tracker
```
3. Create a Virtual Environment

```bash
python -m venv venv
```

4. Activate the Environment
```bash
venv/scripts/activate
```

5. Install the required dependencies:

```bash
pip install -r requirements.txt
```

6. Run migrations to create the database schema:

```bash
python manage.py migrate
```

7. Start the development server:

```bash
python manage.py runserver
```

8. Access the application at [http://localhost:8000](http://localhost:8000).

## API Documentation

The API endpoints are documented using Swagger. Once the server is running, you can access the Swagger documentation at [http://localhost:8000/](http://localhost:8000/) to explore the available endpoints and their usage.

## Contributing

Contributions are welcome! If you would like to contribute to Expense Tracker, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them with descriptive messages.
4. Push your changes to your fork.
5. Submit a pull request to the `main` branch of the original repository.

