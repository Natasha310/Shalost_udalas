import sqlite3

"""Створіть базу даних для інтернет-магазину з наступними таблицями:
products: таблиця для зберігання інформації про продукти, включаючи назву, опис, ціну тощо.
categories: таблиця для категорій продуктів.
products повинна мати зовнішній ключ на таблицю categories.
Напишіть SQL-скрипт для створення зазначених таблиць.
Внесіть декілька рядків даних в кожну таблицю
Виконайте JOIN-запит, який повертає інформацію про продукти та назву їх категорій"""


conn = sqlite3.connect('new.db')
cursor = conn.cursor()

def create_tables():

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    price INTEGER 
    )''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name_of_category TEXT NOT NULL 
    )''')
create_tables()

def populate_tables():
    cursor.execute('''INSERT INTO Products (name, description, price)
    VALUES("onion", "fresh", 13 ) ''')
    conn.commit()

    cursor.execute('''INSERT INTO Products (name, description, price)
    VALUES("cucumber", "not fresh", 8 ) ''')
    conn.commit()

    cursor.execute('''INSERT INTO Categories (name_of_category)
    VALUES("vegetables") ''')
    conn.commit()

    cursor.execute('''INSERT INTO Categories (name_of_category)
    VALUES("fruits" ) ''')
    conn.commit()

    cursor.execute('''INSERT INTO Categories (name_of_category)
    VALUES("salad" ) ''')
    conn.commit()

populate_tables()

def join_tables():
    results3 = cursor.execute('''SELECT 
    Products.id AS id, 
    Products.name AS item, 
    Categories.name_of_category AS category
    FROM Products
    LEFT JOIN Categories ON Products.id = Categories.id''')

    #print(cursor.fetchall())
    for row in results3:
        print(row)

join_tables()

def print_tables():
    results1 = cursor.execute('''SELECT * FROM Products''')
    #print(cursor.fetchall())
    for row in results1:
       print(row)

    results2 = cursor.execute('''SELECT * FROM Categories''')
    #print(cursor.fetchall())
    for row in results2:
        print(row)


print_tables()



conn.close()
