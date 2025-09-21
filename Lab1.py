
item_names = []
item_prices = []

while True:
   
    item_name = input("Enter item name (or press Enter to stop): ")
    
  
    if not item_name:
        break
    
    
    while True:
        try:
            item_price = float(input(f"Enter the price for {item_name}: "))
            
            if 0 <= item_price <= 200:
                item_prices.append(item_price)
                item_names.append(item_name)
                break  
            else:
                print("Error: The price must be between 0 and 200.")
        except ValueError:
            print("Error: Invalid price. Please enter a number.")


if item_names:
    
    num_items = len(item_names)
    print(f"\nTotal number of items: {num_items}")

    
    average_price = sum(item_prices) / num_items
    print(f"Average price: ${average_price:.2f}")

    
    highest_price = max(item_prices)
    lowest_price = min(item_prices)
    

    highest_price_index = item_prices.index(highest_price)
    lowest_price_index = item_prices.index(lowest_price)

    highest_price_item = item_names[highest_price_index]
    lowest_price_item = item_names[lowest_price_index]

    print(f"Highest price item: {highest_price_item} (${highest_price:.2f})")
    print(f"Lowest price item: {lowest_price_item} (${lowest_price:.2f})")
else:
    print("\nNo items were entered.")

