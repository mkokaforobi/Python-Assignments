
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]

product = 1

for position in range(len(numbers)):
	if position % 3 == 0:
		product = product * numbers[position]

print("Product = ", product)