# Restaurant Management System

A console-based Restaurant Management System developed using **Python and MySQL**.

This project allows admins to manage the restaurant menu and view orders, while users can browse the menu, manage their cart, place orders, and generate bills.

## Features

### Admin

* Admin login
* Add menu items
* Delete menu items
* Modify menu items
* View order details
* Calculate day-wise profit

### User

* User registration
* View complete menu
* View menu by category
* Add items to cart
* Modify cart quantity
* Delete items from cart
* View cart
* Generate bill
* Place orders

## Technologies Used

* Python
* MySQL
* MySQL Connector/Python
* SQL
* VS Code

## Database

The project uses MySQL to store:

* Admin information
* User information
* Menu items
* Cart details
* Order details

## Project Workflow

Admin/User
    ↓
Login / User Registration
    ↓
Menu Management / Menu Browsing
    ↓
Cart Management
    ↓
Bill Generation
    ↓
Order Placement
    ↓
Order Storage in MySQL


## How to Run

### 1. Install Python

Make sure Python is installed on your computer.

### 2. Install MySQL Connector

```bash
pip install mysql-connector-python
```

### 3. Create the Database

Create a MySQL database named:

```sql
CREATE DATABASE Restaurant;
```

Create the required tables in MySQL Workbench before running the Python program.

### 4. Configure MySQL Connection

Update the database connection in `restaurant.py` with your own MySQL username and password.

```python
con = db.connect(
    user='root',
    password='My_MySQL_Password',
    host='localhost',
    database='Restaurant'
)
```

### 5. Run the Project

```bash
python restaurant.py
```

## What I Learned

Through this project, I practiced:

* Python programming
* MySQL database connectivity
* SQL queries
* CRUD operations
* Python and MySQL integration
* Input validation
* Cart and order management
* Database transactions
* Basic billing and profit calculation

## Author

**Akula Likitha**

B.Tech – Computer Science & Engineering

GitHub: `https://github.com/likitha5590`




