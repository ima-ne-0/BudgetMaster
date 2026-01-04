BudgetMaster 💰

BudgetMaster is a Backend API built with Django designed to help users manage their personal finances. It allows tracking income and expenses, categorizing transactions, and viewing a real-time financial summary.

🚀 Features

Transactions Management: Create, Read, Update, and Delete (CRUD) expenses and income.

Smart Categorization: Organize transactions by categories (e.g., Food, Salary).

Financial Dashboard: A dedicated endpoint (/api/transactions/summary/) that calculates your total balance instantly.

RESTful API: Fully browsable API interface.

🛠️ Technology Stack

Python 3

Django & Django REST Framework

SQLite (Database)

⚙️ How to Run

Clone the repository:

git clone [https://github.com/ima_ne_0/BudgetMaster.git](https://github.com/ima_ne_0/BudgetMaster.git)
cd BudgetMaster


Create a virtual environment:

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install dependencies:

pip install django djangorestframework django-cors-headers


Run migrations:

python manage.py migrate


Start the server:

python manage.py runserver


📍 API Endpoints

GET /api/categories/ - List all categories

GET /api/transactions/ - List all transactions

GET /api/transactions/summary/ - View financial dashboard
