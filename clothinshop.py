
section = {
    'Shirt': 1500,
    'Half-Shirt': 800,
    'Punjabi': 1300,
    'T-shirt': 400,
    'Pant': 900,
    'Underwear': 200
}

print("Welcome to Filoix Clothing Shop!")
print("\nAvailable Products with Prices:")
for item, price in section.items():
    print(f"{item}: {price} BDT")

order_total = 0


item_1 = input("\nPlease choose the product you want to buy: ").strip().title()
if item_1 in section:
    order_total += section[item_1]
    print(f"Your Item-1 '{item_1}' has been added to your order.")
else:
    print(f"Sorry, Item-1 '{item_1}' is out of stock.")


another_order = input("\nWould you like to order something else? (Yes/No): ").strip().lower()
if another_order == "yes":
    item_2 = input("Enter the name of the second item you would like to buy: ").strip().title()
    if item_2 in section:
        order_total += section[item_2]
        print(f"Item-2 '{item_2}' has been added to your order.")
    else:
        print(f"Sorry, Item-2 '{item_2}' is not available right now.")


if order_total > 0:
    print(f"\nTotal amount to pay: {order_total} BDT")
else:
    print("\nNo items were purchased. Thank you for visiting Filoix!")
