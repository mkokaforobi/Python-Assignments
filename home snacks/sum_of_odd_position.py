numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

total = 0

for position in range(len(numbers)):
	if numbers[position]  % 2 != 0:
		total = total + numbers[position]

print("Sum of odd positions = ", total)