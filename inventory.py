print("INVENTORY MANAGEMENT SYSTEM")
# inventory_with_list.py

inventory = {
    'P001': {'name': 'Laptop', 'quantity': 10, 'price': 1200.00},
    'P002': {'name': 'Mouse', 'quantity': 50, 'price': 15.00},
    'P003': {'name': 'Keyboard', 'quantity': 30, 'price': 25.00},
    'P004': {'name': 'Monitor', 'quantity': 20, 'price': 200.00},
}

def add_product():
    product_id = input("Enter product ID: ").upper()
    if product_id in inventory:
        print("Product ID already exists.\n")
        return
    name = input("Enter product name: ")
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price: "))
    inventory[product_id] = {'name': name, 'quantity': quantity, 'price': price}
    print("Product added successfully.\n")

def view_products():
    if not inventory:
        print("Inventory is empty.\n")
        return
    print("\nCurrent Inventory:")
    print(f"{'ID':<6} {'Name':<15} {'Qty':<6} {'Price':<10}")
    print("-" * 40)
    for pid, info in inventory.items():
        print(f"{pid:<6} {info['name']:<15} {info['quantity']:<6} ${info['price']:<.2f}")
    print()

def update_product():
    product_id = input("Enter product ID to update: ").upper()
    if product_id in inventory:
        quantity = int(input("Enter new quantity: "))
        inventory[product_id]['quantity'] = quantity
        print("Product updated.\n")
    else:
        print("Product not found.\n")

def delete_product():
    product_id = input("Enter product ID to delete: ").upper()
    if product_id in inventory:
        del inventory[product_id]
        print("Product deleted.\n")
    else:
        print("Product not found.\n")

def menu():
    while True:
        print("==== Inventory Commands ====")
        print("Type one of the following: add, view, update, delete, exit")
        command = input("Command: ").strip().lower()

        if command == 'add':
            add_product()
        elif command == 'view':
            view_products()
        elif command == 'update':
            update_product()
        elif command == 'delete':
            delete_product()
        elif command == 'exit':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid command. Please try again.\n")


menu()
