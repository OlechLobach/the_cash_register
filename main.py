class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.cart = []

class Admin:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.products = []

def main():
    admin = Admin("Admin", "Admin")
    users = []

    while True:
        print("\n1. Зареєструватись")
        print("2. Увійти як користувач")
        print("3. Увійти як адміністратор")
        print("4. Вийти")
        choice = input("Оберіть опцію: ")

        if choice == "1":
            username = input("Введіть ім'я користувача: ")
            password = input("Введіть пароль: ")
            users.append(User(username, password))
            print("Користувач зареєстрований.")

        elif choice == "2":
            username = input("Введіть ім'я користувача: ")
            password = input("Введіть пароль: ")
            user = find_user(username, password, users)
            if user:
                user_menu(user, admin.products)
            else:
                print("Невірне ім'я користувача або пароль.")

        elif choice == "3":
            username = input("Введіть ім'я адміністратора: ")
            password = input("Введіть пароль адміністратора: ")
            if username == admin.username and password == admin.password:
                admin_menu(admin)
            else:
                print("Невірне ім'я адміністратора або пароль.")

        elif choice == "4":
            break

        else:
            print("Невірний вибір. Спробуйте ще раз.")

def find_user(username, password, users):
    for user in users:
        if user.username == username and user.password == password:
            return user
    return None

def user_menu(user, products):
    while True:
        print("\n1. Показати список товарів")
        print("2. Додати товар у кошик")
        print("3. Показати кошик")
        print("4. Закінчити покупку")
        print("5. Вийти")
        choice = input("Оберіть опцію: ")

        if choice == "1":
            show_products(products)

        elif choice == "2":
            add_to_cart(user, products)

        elif choice == "3":
            show_cart(user)

        elif choice == "4":
            checkout(user)
            break

        elif choice == "5":
            break

        else:
            print("Невірний вибір. Спробуйте ще раз.")

def show_products(products):
    print("\nСписок товарів:")
    for i, product in enumerate(products, 1):
        print(f"{i}. {product.name} - {product.price} грн")

def add_to_cart(user, products):
    show_products(products)
    choice = input("Виберіть товар для додавання у кошик (введіть номер товару): ")
    try:
        choice = int(choice)
        if 1 <= choice <= len(products):
            user.cart.append(products[choice - 1])
            print("Товар додано у кошик.")
        else:
            print("Невірний номер товару.")
    except ValueError:
        print("Введіть коректний номер товару.")

def show_cart(user):
    total_price = sum(product.price for product in user.cart)
    print("\nКошик:")
    for i, product in enumerate(user.cart, 1):
        print(f"{i}. {product.name} - {product.price} грн")
    print(f"Загальна сума до оплати: {total_price} грн")

def checkout(user):
    total_price = sum(product.price for product in user.cart)
    print(f"Загальна сума до оплати: {total_price} грн")
    user.cart.clear()
    print("Покупка успішно завершена.")

def admin_menu(admin):
    while True:
        print("\n1. Додати товар")
        print("2. Видалити товар")
        print("3. Змінити інформацію про товар")
        print("4. Вийти")
        choice = input("Оберіть опцію: ")

        if choice == "1":
            add_product(admin.products)

        elif choice == "2":
            delete_product(admin.products)

        elif choice == "3":
            update_product(admin.products)

        elif choice == "4":
            break

        else:
            print("Невірний вибір. Спробуйте ще раз.")

def add_product(products):
    name = input("Введіть назву товару: ")
    price = float(input("Введіть ціну товару: "))
    products.append(Product(name, price))
    print("Товар додано.")

def delete_product(products):
    show_products(products)
    choice = input("Виберіть товар для видалення (введіть номер товару): ")
    try:
        choice = int(choice)
        if 1 <= choice <= len(products):
            del products[choice - 1]
            print("Товар видалено.")
        else:
            print("Невірний номер товару.")
    except ValueError:
        print("Введіть коректний номер товару.")

def update_product(products):
    show_products(products)
    choice = input("Виберіть товар для зміни (введіть номер товару): ")
    try:
        choice = int(choice)
        if 1 <= choice <= len(products):
            product = products[choice - 1]
            new_name = input("Введіть нову назву товару: ")
            new_price = float(input("Введіть нову ціну товару: "))
            product.name = new_name
            product.price = new_price
            print("Інформацію про товар оновлено.")
        else:
            print("Невірний номер товару.")
    except ValueError:
        print("Введіть коректний номер товару.")

if __name__ == "__main__":
    main()