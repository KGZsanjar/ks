import sqlite3

def create_db():
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()

    # Создание таблицы products
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_title TEXT NOT NULL CHECK(LENGTH(product_title) <= 200),
        price REAL NOT NULL DEFAULT 0.0 CHECK(price >= 0),
        quantity INTEGER NOT NULL DEFAULT 0 CHECK(quantity >= 0)
    )
    ''')

    conn.commit()
    conn.close()

# Вызов функции для создания базы данных и таблицы
create_db()

def insert_products():
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()

    products = [
        ('Товар 1', 120.50, 10),
        ('Товар 2', 80.00, 5),
        ('Товар 3', 150.00, 2),
        ('Товар 4', 99.99, 8),
        ('Товар 5', 200.00, 15),
        ('Товар 6', 70.50, 0),
        ('Товар 7', 300.75, 6),
        ('Товар 8', 45.99, 20),
        ('Товар 9', 110.00, 4),
        ('Товар 10', 65.00, 7),
        ('Товар 11', 25.99, 12),
        ('Товар 12', 89.00, 3),
        ('Товар 13', 150.75, 5),
        ('Товар 14', 60.99, 11),
        ('Товар 15', 35.49, 9)
    ]

    cursor.executemany('INSERT INTO products (product_title, price, quantity) VALUES (?, ?, ?)', products)
    conn.commit()
    conn.close()

# Вызов функции для добавления товаров
insert_products()


def update_quantity(product_id, new_quantity):
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE products SET quantity = ? WHERE id = ?', (new_quantity, product_id))
    conn.commit()
    conn.close()

# Пример вызова: изменение количества товара с id=1 на 20
update_quantity(1, 20)

def update_price(product_id, new_price):
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE products SET price = ? WHERE id = ?', (new_price, product_id))
    conn.commit()
    conn.close()

# Пример вызова: изменение цены товара с id=2 на 75.00
update_price(2, 75.00)

def delete_product(product_id):
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM products WHERE id = ?', (product_id,))
    conn.commit()
    conn.close()

# Пример вызова: удаление товара с id=3
delete_product(3)

def get_all_products():
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM products')
    products = cursor.fetchall()

    for product in products:
        print(product)

    conn.close()

# Вызов функции для вывода всех товаров
get_all_products()

def get_products_by_price_and_quantity(price_limit, quantity_limit):
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM products WHERE price < ? AND quantity > ?', (price_limit, quantity_limit))
    products = cursor.fetchall()

    for product in products:
        print(product)

    conn.close()

# Пример вызова: товары дешевле 100 сом и с количеством больше 5
get_products_by_price_and_quantity(100, 5)

def search_products_by_title(search_term):
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM products WHERE product_title LIKE ?', ('%' + search_term + '%',))
    products = cursor.fetchall()

    for product in products:
        print(product)

    conn.close()

# Пример вызова: поиск товаров, содержащих слово "мыло"
search_products_by_title('мыло')

# Тестирование функции изменения количества товара
update_quantity(1, 25)

# Тестирование функции изменения цены товара
update_price(2, 85.00)

# Тестирование функции удаления товара
delete_product(3)

# Тестирование функции вывода всех товаров
get_all_products()

# Тестирование функции поиска товаров по цене и количеству
get_products_by_price_and_quantity(100, 5)

# Тестирование функции поиска товаров по названию
search_products_by_title('Товар')