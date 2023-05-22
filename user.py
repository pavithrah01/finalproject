import re
class User:
    def __init__(self, full_name, phone_number, email, address, password):
        self.full_name = full_name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.password = password
        self.order_history = []

    def place_new_order(self):
        food_menu = {
            1: "Tandoori Chicken (4 pieces) [INR 240]",
            2: "Vegan Burger (1 Piece) [INR 320]",
            3: "Truffle Cake (500gm) [INR 900]"
        }
        print("Food Menu:")
        for item_number, item_description in food_menu.items():
            print(f"{item_number}. {item_description}")

        order_items = []
        while True:
            try:
                selected_items = input("Enter the numbers of the items you want to order (separated by commas): ")
                order_items = [int(item) for item in selected_items.split(",")]
                break
            except ValueError:
                print("Invalid input. Please enter numbers separated by commas.")

        selected_food_items = [food_menu[item] for item in order_items]
        print("Selected Food Items:")
        for item in selected_food_items:
            print(item)

        place_order = input("Do you want to place the order? (yes/no): ")
        if place_order.lower() == "yes":
            self.order_history.append(selected_food_items)
            print("Order placed successfully!")
        else:
            print("Order cancelled.")

    def view_order_history(self):
        print("Order History:")
        for order in self.order_history:
            print(", ".join(order))

    def update_profile(self):
        print("Update Profile:")
        self.full_name = input("Full Name: ")
        self.phone_number = input("Phone Number: ")
        self.email = input("Email: ")
        self.address = input("Address: ")
        self.password = input("Password: ")


def register():
    print("Register on the application")
    full_name = input("Full Name: ")
    phone_number = input("Phone Number: ")
    while not validate_phone_number(phone_number):
        print("Invalid phone number! Please enter a valid phone number.")
        phone_number = input("Phone Number: ")
    email = input("Email: ")
    while not validate_email(email):
        print("Invalid email! Please enter a valid email address.")
        email = input("Email: ")
    address = input("Address: ")
    password = input("Password: ")
    while not validate_password(password):
        print(
            "Invalid password! Please enter a password with at least 8 characters, including at least one uppercase letter, one lowercase letter, and one digit.")
        password = input("Password: ")
    user = {
        "full_name": full_name,
        "phone_number": phone_number,
        "email": email,
        "address": address,
        "password": password
    }
    users.append(user)
    print("Registration successful!")

def validate_phone_number(phone_number):
    # Phone number regex pattern: accepts 10 digits, with optional '+' at the start
    pattern = r'^\+?\d{10}$'
    return re.match(pattern, phone_number) is not None

def validate_email(email):
    # Email regex pattern
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

def validate_password(password):
    # Password regex pattern: at least 8 characters, including at least one uppercase letter, one lowercase letter, and one digit
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$'
    return re.match(pattern, password) is not None

def login(users):
    print("Login:")
    email = input("Email: ")
    password = input("Password: ")
    for user in users:
        if user.email == email and user.password == password:
            return user
    return None


def main():
    users = []
    while True:
        print("\nWelcome to the Application!")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            user = register()
            users.append(user)
            print("Registration successful!")

        elif choice == "2":
            user = login(users)
            if user:
                while True:
                    print("\nOptions:")
                    print("1. Place New Order")
                    print("2. Order History")
                    print("3. Update Profile")
                    print("4. Logout")
                    user_choice = input("Enter your choice: ")

                    if user_choice == "1":
                        user.place_new_order()

                    elif user_choice == "2":
                        user.view_order_history()

                    elif user_choice == "3":
                        user.update_profile()

                    elif user_choice == "4":
                        break

                    else:
                        print("Invalid choice. Please try again.")

            else:
                print("Invalid email or password. Please try again.")

        elif choice == "3":
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == '__main__':
    main()
