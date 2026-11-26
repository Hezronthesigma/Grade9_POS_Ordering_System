

products = {
	1: {"name": "Chickenjoy", "price": 2.99},
	2: {"name": "Jolly Spaghetti", "price": 1.99},
	3: {"name": "Yumburger", "price": 1.49},
	4: {"name": "Peach Mango Pie", "price": 1.29}
}


def show_menu():
	print("Product Menu:")
	for pid, info in products.items():
		print(f"{pid}. {info['name']} - ${info['price']:.2f}")


def main():
	order = {}

	while True:
		show_menu()
		try:
			choice = int(input("Select a product by number (0 to finish): "))
		except ValueError:
			print("Invalid input. Please enter a number.")
			continue

		if choice == 0:
			break
		if choice not in products:
			print("Product not found. Try again.")
			continue

		try:
			qty = int(input(f"Enter quantity for {products[choice]['name']}: "))
		except ValueError:
			print("Invalid quantity. Please enter a number.")
			continue
		if qty <= 0:
			print("Quantity must be positive.")
			continue

		order[choice] = order.get(choice, 0) + qty

	print("\nOrder Summary:")
	total = 0.0
	for pid, qty in order.items():
		name = products[pid]['name']
		price = products[pid]['price']
		subtotal = price * qty
		total += subtotal
		print(f"{name} x{qty} = ${subtotal:.2f}")

	print(f"Total: ${total:.2f}")


if __name__ == "__main__":
	main()
