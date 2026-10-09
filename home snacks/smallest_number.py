numbers = [25, 7, 45, 12, 89, 34]

smallest = numbers[0]

for number in numbers:
	if number < smallest:
		smallest = number

print("Smallest = ", smallest)