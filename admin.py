class FoodItem:
    def __init__(self, name, quantity, price, discount, stock):
        self.food_id = None  # FoodID will be generated automatically
        self.name = name
        self.quantity = quantity
        self.price = price
        self.discount = discount
        self.stock = stock

class Admin:
    def __init__(self):
        self.food_items = []  # List to store food items

    def generate_food_id(self):
        # Generate a unique FoodID
        if not self.food_items:
            return 1
        else:
            last_id = self.food_items[-1].food_id
            return last_id + 1

    def add_food_item(self):
        name = input("Enter the name of the food item: ")
        quantity = input("Enter the quantity of the food item: ")
        price = float(input("Enter the price of the food item: "))
        discount = float(input("Enter the discount for the food item: "))
        stock = int(input("Enter the stock amount of the food item: "))

        food_id = self.generate_food_id()
        food_item = FoodItem(name, quantity, price, discount, stock)
        food_item.food_id = food_id
        self.food_items.append(food_item)
        print("Food item added successfully!")

    def edit_food_item(self):
        food_id = int(input("Enter the FoodID of the item to edit: "))
        for item in self.food_items:
            if item.food_id == food_id:
                name = input("Enter the new name of the food item: ")
                quantity = input("Enter the new quantity of the food item: ")
                price = float(input("Enter the new price of the food item: "))
                discount = float(input("Enter the new discount for the food item: "))
                stock = int(input("Enter the new stock amount of the food item: "))

                item.name = name
                item.quantity = quantity
                item.price = price
                item.discount = discount
                item.stock = stock
                print("Food item edited successfully!")
                return
        print("Food item not found!")

    def view_all_food_items(self):
        if not self.food_items:
            print("No food items found.")
        else:
            for item in self.food_items:
                print(f"Food ID: {item.food_id}")
                print(f"Name: {item.name}")
                print(f"Quantity: {item.quantity}")
                print(f"Price: {item.price}")
                print(f"Discount: {item.discount}")
                print(f"Stock: {item.stock}")
                print("------------------------")

    def remove_food_item(self):
        food_id = int(input("Enter the FoodID of the item to remove: "))
        for item in self.food_items:
            if item.food_id == food_id:
                self.food_items.remove(item)
                print("Food item removed successfully!")
                return
        print("Food item not found!")


# Sample usage:
admin = Admin()

# Adding food items
admin.add_food_item()
admin.add_food_item()
admin.add_food_item()

# Viewing all food items
admin.view_all_food_items()

# Editing a food item
admin.edit_food_item()

# Removing a food item
admin.remove_food_item()

# Viewing all food items after modifications
admin.view_all_food_items()
