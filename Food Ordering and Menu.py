# Food Ordering and Billing System

food_menu = {
    "pizza": 200,
    "burger": 100,
    "pasta": 150,
    "tea": 50
}

orders = {}
total_bill = 0


def show_menu():
    print("\n--- FOOD MENU ---")
    for item, price in food_menu.items():
        print(f"{item.capitalize()}: ₹{price}")


def order_food():
    global total_bill
    show_menu()

    item = input("Enter food item: ").lower()

    if item in food_menu:
        try:
            qty = int(input("Enter quantity: "))
            if qty <= 0:
                print("Quantity must be greater than 0!")
                return

            if item in orders:
                orders[item] += qty
            else:
                orders[item] = qty

            total_bill += food_menu[item] * qty
            print(f"{item.capitalize()} x{qty} added!")

        except ValueError:
            print("Invalid quantity!")

    else:
        print("Item not available!")


def generate_bill():
    print("\n----- FINAL BILL -----")

    if not orders:
        print("No items ordered!")
        return

    for item, qty in orders.items():
        price = food_menu[item]
        print(f"{item.capitalize()} x{qty} = ₹{price * qty}")

    print("----------------------")
    print("Total Amount: ₹", total_bill)


def menu():
    while True:
        print("\n--- SYSTEM MENU ---")
        print("1. Order Food")
        print("2. Generate Bill")
        print("3. Exit")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                order_food()
            elif choice == 2:
                generate_bill()
            elif choice == 3:
                print("Thank you! Visit Again 😊")
                break
            else:
                print("Invalid choice!")

        except ValueError:
            print("Please enter a number!")


menu()