user_name = input("Enter your name : ")

final_bill = 0
total_bill = 0

next_transaction ="yes"

while next_transaction == "yes":
	product_name = input("Enter product name : ")
	quantity = float(input("Enter quantity of " + product_name + ":"))
	unit_price = float(input(f"Enter price of {product_name} :"))
	total_bill = quantity * unit_price
	final_bill += total_bill

	next_transaction = input("Do you want to enter another product? Yes / No : ").lower()

print("Your total bill is NGN" , final_bill)


