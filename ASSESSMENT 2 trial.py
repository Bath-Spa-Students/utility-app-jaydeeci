print("*********************************")
print("Welcome to Vending Machine Bravo!")
print("*********************************")
print("If you would like to make a selection, please insert the appropriate currency into the machine.")
1

class VendingMachine:
    def __init__(self):
        self.drinks = {
            '1': {'name': 'Coke', 'price': 1.00, 'quantity': 10},
            '2': {'name': 'Masafi', 'price': 0.50, 'quantity': 15},
            '3': {'name': 'Orange Juice', 'price': 2.00, 'quantity': 12},
            '4': {'name': 'Pepsi', 'price': 1.00, 'quantity': 10},
            '5': {'name': 'Pocari Sweat', 'price': 2.50, 'quantity': 20}
        }

        self.food = {
            '1': {'name': 'Doritos', 'price': 1.00, 'quantity': 15},
            '2': {'name': 'Ferrero Rocher', 'price': 2.25, 'quantity': 20},
            '3': {'name': 'Tuna Sandwich', 'price': 3.00, 'quantity': 10},
            '4': {'name': 'Croissant', 'price': 3.00, 'quantity': 12},
            '5': {'name': 'Takis', 'price': 2.50, 'quantity': 15}
        }

    def display_drinks(self):
        print("Available Drinks:")
        for code, item in self.drinks.items():
            print(f"{code}: {item['name']} - ${item['price']} - Quantity: {item['quantity']}")

    def display_food(self):
        print("Available Food Items:")
        for code, item in self.food.items():
            print(f"{code}: {item['name']} - ${item['price']} - Quantity: {item['quantity']}")

    def select_item(self, menu):
        code = input(f"Enter the item code to purchase from {menu}: ")
        if menu == 'drinks':
            return self.drinks.get(code)
        elif menu == 'food':
            return self.food.get(code)
        else:
            return None

    def process_payment(self, selected_item):
        if selected_item:
            price = selected_item['price']
            print(f"Price of {selected_item['name']}: ${price}")
            amount = float(input("Please enter the amount: $"))
            if amount >= price:
                change = amount - price
                print(f"Thank you for your purchase! Your change is: ${change:.2f}")
                selected_item['quantity'] -= 1
            else:
                print("Insufficient amount. Please insert more money.")
        else:
            print("Invalid item code. Please try again.")

    def start(self):
        while True:
            print("\nDRINKS MENU")
            self.display_drinks()
            drink_choice = self.select_item('drinks')
            self.process_payment(drink_choice)

            print("\nFOOD MENU")
            self.display_food()
            food_choice = self.select_item('food')
            self.process_payment(food_choice)

            choice = input("Would you like to buy more items? (y/n): ")
            if choice.lower() != 'y':
                break

if __name__ == "__main__":
    vending_machine = VendingMachine()
    vending_machine.start()