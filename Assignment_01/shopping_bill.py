customer_name = input("Enter customer name: ")

product1 = input("Enter first product name: ")
price1 = float(input("Enter first product price: "))

product2 = input("Enter second product name: ")
price2 = float(input("Enter second product price: "))

product3 = input("Enter third product name: ")
price3 = float(input("Enter third product price: "))

total_amount = price1 + price2 + price3

if total_amount > 3000:
    discount = total_amount * 0.10
else:
    discount = 0

final_amount = total_amount - discount

print("\n========== SMART SHOPPING BILL ==========")
print(f"Customer Name: {customer_name}")
print("-----------------------------------------")
print(f"{product1}: Rs. {price1}")
print(f"{product2}: Rs. {price2}")
print(f"{product3}: Rs. {price3}")
print("-----------------------------------------")
print(f"Total Amount: Rs. {total_amount}")
print(f"Discount: Rs. {discount}")
print(f"Final Payable Amount: Rs. {final_amount}")
