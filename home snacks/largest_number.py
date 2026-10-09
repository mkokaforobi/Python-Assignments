numbers = [25, 7, 45, 12, 89, 34]

largest = numbers[0]

for number in numbers:
	if number > largest:
		largest = number

print("Largest =", largest)