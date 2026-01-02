# ============================================
# Vending Machine Utility App
# ============================================
#Module Leader: Dr.Febin


class VendingMachine:
    def __init__(self):
        # Items dictionary: each item has a code, name, category, price, and quantity
        self.items = {
            "A1": {"Name": "Soda",          "Category": "Cold Drink", "Price": 1.50, "Quantity": 10},
            "A2": {"Name": "Chips",         "Category": "Snack",      "Price": 1.00, "Quantity": 5},
            "A3": {"Name": "Candy",         "Category": "Snack",      "Price": 0.75, "Quantity": 20},
            "A4": {"Name": "Gum",           "Category": "Snack",      "Price": 1.00, "Quantity": 15},
            "A5": {"Name": "Snicker",       "Category": "Chocolate",  "Price": 1.25, "Quantity": 10},

            "B1": {"Name": "Water",         "Category": "Cold Drink", "Price": 1.00, "Quantity": 25},
            "B2": {"Name": "Mango Juice",   "Category": "Cold Drink", "Price": 1.75, "Quantity": 10},
            "B3": {"Name": "Red Bull",      "Category": "Energy",     "Price": 1.50, "Quantity": 10},
            "B4": {"Name": "Mountain Dew",  "Category": "Cold Drink", "Price": 1.25, "Quantity": 5},
            "B5": {"Name": "Lays",          "Category": "Snack",      "Price": 1.00, "Quantity": 10},

            "C1": {"Name": "Pepsi",         "Category": "Cold Drink", "Price": 1.50, "Quantity": 10},
            "C2": {"Name": "Doritos",       "Category": "Snack",      "Price": 1.00, "Quantity": 10},
            "C3": {"Name": "Iced Tea",      "Category": "Cold Drink", "Price": 1.50, "Quantity": 12},
            "C4": {"Name": "Chocolate Milk","Category": "Cold Drink", "Price": 1.75, "Quantity": 8},
            "C5": {"Name": "Protein Bar",   "Category": "Healthy",    "Price": 2.00, "Quantity": 10},

            "D1": {"Name": "Orange Juice",  "Category": "Cold Drink", "Price": 1.80, "Quantity": 10},
            "D2": {"Name": "Salted Peanuts","Category": "Healthy",    "Price": 1.25, "Quantity": 15},
            "D3": {"Name": "Cup Noodles",   "Category": "Snack",      "Price": 2.50, "Quantity": 6},
            "D4": {"Name": "KitKat",        "Category": "Chocolate",  "Price": 1.20, "Quantity": 12},
            "D5": {"Name": "Popcorn",       "Category": "Snack",      "Price": 1.50, "Quantity": 10}
        }

    def display_menu(self):
        """Display all items grouped by category."""
        print("\n===== VENDING MACHINE MENU =====")
        # Collect all categories
        categories = {}
        for code, item in self.items.items():
            category = item["Category"]
            if category not in categories:
                categories[category] = []
            categories[category].append((code, item))

        # Print items grouped by category
        for category, items in categories.items():
            print(f"\n--- {category.upper()} ---")
            for code, item in items:
                print(f"{code}: {item['Name']} - ${item['Price']:.2f} ({item['Quantity']} left)")

    def get_valid_code(self):
        """Ask the user for an item code and validate it."""
        while True:
            code = input("\nEnter the item code (or 'q' to quit): ").upper()
            if code == "Q":
                return None
            if code in self.items:
                item = self.items[code]
                if item["Quantity"] > 0:
                    return code
                else:
                    print("Sorry, that item is out of stock. Please choose another item.")
            else:
                print("Invalid code. Please try again.")

    def handle_payment(self, price):
        """
        Handle money input from the user.
        Returns the change if payment is successful, or None if cancelled.
        """
        print(f"The price is ${price:.2f}.")
        inserted = 0.0

        while inserted < price:
            try:
                more = input(f"Insert money (you have inserted ${inserted:.2f}) or type 'c' to cancel: ")
                if more.lower() == "c":
                    print("Transaction cancelled. Returning any inserted money.")
                    return None
                amount = float(more)
                if amount <= 0:
                    print("Please insert a positive amount.")
                else:
                    inserted += amount
            except ValueError:
                print("Please enter a valid number.")

        change = inserted - price
        return change

    def suggest_item(self, selected_code):
        """Suggest a related item based on category."""
        selected_item = self.items[selected_code]
        selected_category = selected_item["Category"]

        # Find another item in the same category with stock
        for code, item in self.items.items():
            if code != selected_code and item["Category"] == selected_category and item["Quantity"] > 0:
                return code, item

        # If nothing found in same category, return None
        return None, None

    def dispense_item(self, code, change):
        """Dispense the item and show messages."""
        item = self.items[code]
        item["Quantity"] -= 1
        print(f"\nDispensing {item['Name']}...")
        print("Enjoy your item!")
        print(f"Your change is: ${change:.2f}")

    def run(self):
        """Main loop of the vending machine."""
        print("Welcome to the Vending Machine!")

        while True:
            self.display_menu()

            code = self.get_valid_code()
            if code is None:
                print("Thank you for using the vending machine. Goodbye!")
                break

            item = self.items[code]
            price = item["Price"]

            change = self.handle_payment(price)
            if change is None:
                # Payment cancelled
                continue

            self.dispense_item(code, change)

            # Suggest another item
            suggestion_code, suggestion = self.suggest_item(code)
            if suggestion:
                print(f"\nYou might also like: {suggestion['Name']} ({suggestion_code}) for ${suggestion['Price']:.2f}")

            # Ask if the user wants to buy another item
            again = input("\nWould you like to buy another item? (yes/no): ").strip().lower()
            if again != "yes":
                print("Thank you for your purchase. Goodbye!")
                break


if __name__ == "__main__":
    machine = VendingMachine()
    machine.run()
