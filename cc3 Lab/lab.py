discounts = {"MONDAY": 0.10, "WEDNESDAY": 0.20, "FRIDAY": 0.05}
children = 150
teenager = 200
adults = 250
seniors = 180 
total_tickets = 0
total_sales = 0.0

while total_tickets < 100:
    age = int(input("Enter customer age: "))
    day = input("Enter the day of the week: ").upper()
    discount_rate = discounts.get(day, 0.0)
    if age < 12:
        base_price = children   
    elif age < 18:
        base_price = teenager
    elif age < 60:
        base_price = adults
    else:
        base_price = seniors

    discount_amount = base_price * discount_rate
    final_price = base_price - discount_amount
    discount_percentage = discount_rate * 100
    print("\nCustomer Age: {}".format(age))
    print("Day of the Week: {}".format(day.capitalize()))
    print("Ticket Price: {:.0f} pesos".format(base_price))
    print("Discount Applied: {:.0f}%".format(discount_percentage))
    print("Final Price: {:.0f} pesos".format(final_price))

    total_tickets += 1
    total_sales += final_price
    again = input("\nDo you want to process another ticket? (yes/no): ").lower()
    if again != "yes":
        break
print("\n--- Sales Summary ---")    
print("Total Tickets Sold: {}".format(total_tickets))
print("Total Sales: {:.0f} pesos".format(total_sales))  
