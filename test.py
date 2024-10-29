# Sample database of stores and products
stores = {
    1: {"name": "Asia", "products": [
        {"name": "Chocolate", "category": "Food products", "price": 10.5, "quantity": 129},
        {"name": "Rice", "category": "Food products", "price": 5.0, "quantity": 200}
    ]},
    2: {"name": "Globus", "products": [
        {"name": "Milk", "category": "Dairy", "price": 2.5, "quantity": 50},
        {"name": "Cheese", "category": "Dairy", "price": 8.0, "quantity": 30}
    ]},
    3: {"name": "Spar", "products": [
        {"name": "Bread", "category": "Bakery", "price": 1.5, "quantity": 100},
        {"name": "Butter", "category": "Dairy", "price": 3.5, "quantity": 40}
    ]}
}

# Display the initial message
print(
    "Вы можете отобразить список продуктов по выбранному id магазина из перечня магазинов ниже, для выхода из программы введите цифру 0:")

# Display list of stores
for store_id, store_info in stores.items():
    print(f"{store_id}. {store_info['name']}")

# Main program loop
while True:
    try:
        # Ask the user for a store ID
        store_id = int(input("Введите id магазина: "))

        # Exit the program if the user enters 0
        if store_id == 0:
            print("Выход из программы.")
            break

        # Check if the store ID exists in the database
        if store_id in stores:
            print(f"Товары в магазине {stores[store_id]['name']}:")

            # Display products in the selected store
            for product in stores[store_id]["products"]:
                print(f"Название продукта: {product['name']}")
                print(f"Категория: {product['category']}")
                print(f"Цена: {product['price']}")
                print(f"Количество на складе: {product['quantity']}\n")
        else:
            print("Неверный id магазина. Пожалуйста, попробуйте снова.")

    except ValueError:
        print("Пожалуйста, введите корректное числовое значение.")