# Заварін Валентин КВ-31мн
lab1

Тема: Розробка серверної частини Web-додатка» 

Завдання:

Запропонувати тематику Web-додатку (див. рекомендований список).
Ознайомившись з переліком обов’язкових функцій, виконати їх кодування, використовуючи Django:
Встановити середовище розробки (рекомендовано Pycharm Community Edition)
Встановити virtualenv, Django, DRF (Приклад)
Розробити базу даних, створити проєкт Django та його необхідні додатки
Наповнити даними базу за допомогою Django Admin Panel
Розробити функціональність відповідно до обраного завдання 
За бажанням студента доповнити сайт іншими функціями.
Створити документацію API у форматі redoc
Створити необхідні запити та тести у Postman, впевнитись у коректній роботі серверного API.
Підготувати звіт, створити репозиторій та завантажити усі власні файли на github.com.


# Contact Management System
This is a Django-based Contact Management System that allows users to add, edit, delete, and search contacts. The system includes a front-end built with HTML, CSS, and JavaScript (using jQuery for AJAX calls).

Google Docs: https://docs.google.com/document/d/1dSMBMgTc4dVGUnesh-6GZvC6I_S9YO9g-ZR_F5SXt2Y/edit?usp=sharing

# Features
Add new contacts
Edit existing contacts
Delete contacts
Search contacts
Sort contacts by name, email, phone number, and address

# Installation
Clone the repository:
```
git clone https://github.com/V1zav/tech_dev_1
```
Create and activate a virtual environment:
```
python -m venv venv
venv\Scripts\activate
```
Install the required packages:
```
pip install -r requirements.txt
```
Apply migrations:
```
python manage.py migrate
```
Create a superuser:
```
python manage.py createsuperuser
```
Run the development server:
```
python manage.py runserver
```
Open your browser and navigate to:
```
http://127.0.0.1:8000/
```
# Usage
Navigate to the Contacts Page:
On the homepage, click on the "Contacts" link to navigate to the contacts page.

Add a New Contact:
Fill out the form at the bottom of the contacts page and click "Add Contact".

Edit an Existing Contact:
Click the "Edit" button next to a contact, modify the information, and click "Save".

Delete a Contact:
Click the "Delete" button next to a contact and confirm the deletion.

Search for Contacts:
Use the search bar at the top of the page to filter contacts by name, email, phone number, or address.

Sort Contacts:
Use the sort buttons to sort contacts by name, email, phone number, or address.

# API Endpoints
GET /api/contacts/: Retrieve a list of contacts.

POST /api/contacts/: Add a new contact.

PUT /api/contacts/{id}/: Update an existing contact.

DELETE /api/contacts/{id}/: Delete a contact.
