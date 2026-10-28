# 🍔 Food Delivery Data Analysis Project

## 📌 Project Overview

This project is a complete Food Delivery Data Analysis System developed using MySQL, Python, Pandas, and Streamlit.

The project follows an end-to-end data analytics workflow:

1. Creating a database in MySQL.
2. Creating tables and inserting sample data.
3. Connecting MySQL with Python.
4. Extracting and cleaning data.
5. Performing customer, order, and delivery analysis.
6. Building an interactive dashboard using Streamlit.

---

# 🛠️ Technologies Used

- MySQL
- Python
- Pandas
- NumPy
- PyMySQL
- SQLAlchemy
- Streamlit
- Matplotlib
- VS Code

---

# 🗄️ Database Design

The following tables were created in MySQL:

### Customers
Stores customer information.

### Restaurants
Stores restaurant details.

### Menu
Stores food item information.

### Orders
Stores order-related information.

### Delivery
Stores delivery tracking data.

---

# 📥 Data Insertion

Sample data was inserted into all tables using SQL queries.

Key data included:

- Customer Details
- Restaurant Details
- Menu Information
- Order Records
- Delivery Records

---

# 🔗 Python and MySQL Connection

The database was connected with Python using PyMySQL and SQLAlchemy.

Required libraries:

```bash
pip install pymysql
pip install sqlalchemy
```

Example Connection:

```python
import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="Food_Delivery"
)
```

---

# 🧹 Data Cleaning

After loading data from MySQL into Pandas DataFrames, several cleaning operations were performed:

- Handling Missing