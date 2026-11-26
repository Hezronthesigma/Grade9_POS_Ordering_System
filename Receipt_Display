from datetime import datetime
from Menu import products


def display_receipt(order, products):
    total = 0.0

    print("\n--- ORDER RECEIPT ---")
    print("Date:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    if not order:
        print("No items purchased.")

    for product_id, quantity in order.items():
        product = products[product_id]
        subtotal = product["price"] * quantity
        total += subtotal
        print(
            f"{product['name']} x {quantity}: "
            f"${subtotal:.2f}"
        )

    print("---------------------")
    print(f"Total: ${total:.2f}")
    print("Thank you for your order!")


def main():
    order = {}

    while True:
        print("\nMenu:")
        for product_id, product in products.items():
            print(f"{product_id}. {product['name']} - ${product['price']:.2f}")

        try:
            choice = int(input("Enter a product number (0 to finish): "))
        except ValueError:
            print("Please enter a number.")
            continue

        if choice == 0:
            break
        if choice not in products:
            print("That product is not on the menu.")
            continue

        try:
            quantity = int(input("Enter quantity: "))
        except ValueError:
            print("Please enter a whole number for the quantity.")
            continue

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            continue

        order[choice] = order.get(choice, 0) + quantity

    display_receipt(order, products)


if __name__ == "__main__":
    main()
