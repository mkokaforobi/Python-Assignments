array_word = ["aba", "xyz", "121", "level", "hello", "aa"]

count = 0

for word in array_word:
	if len(word) >= 2 and word[0] == word[-1]:
		count = count + 1

print("Number of matching strings = ", count)
