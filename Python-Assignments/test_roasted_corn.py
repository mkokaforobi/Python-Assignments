from roasted_corn import roasted_corn

corn = roasted_corn()

print("--- string_length ---")
print(corn.string_length("semicolon"))
print(corn.string_length(""))
print(corn.string_length("a b!"))

print("--- first_and_last_two ---")
print(corn.first_and_last_two("semicolon"))
print(corn.first_and_last_two("on"))
print(corn.first_and_last_two("o"))
print(corn.first_and_last_two(""))
print(corn.first_and_last_two("abc"))

print("--- add_ing ---")
print(corn.add_ing("abc"))
print(corn.add_ing("string"))
print(corn.add_ing("on"))
print(corn.add_ing(""))
print(corn.add_ing("ing"))

print("--- remove_odd_index_characters ---")
print(corn.remove_odd_index_characters("semicolon"))
print(corn.remove_odd_index_characters("abcdef"))
print(corn.remove_odd_index_characters("a"))
print(corn.remove_odd_index_characters(""))

print("--- repeat_string ---")
print(corn.repeat_string("hello", 3))
print(corn.repeat_string("hi", 4.5))
print(corn.repeat_string("hi", 0))
print(corn.repeat_string("hi", 3.0))
print(corn.repeat_string("", 5))

print("--- square_each ---")
print(corn.square_each([2, 3, 4, 5, 7]))
print(corn.square_each([]))
print(corn.square_each([-2, -3]))
print(corn.square_each([0]))

print("--- sum_of_squares ---")
print(corn.sum_of_squares([2, 3, 4, 5, 7]))
print(corn.sum_of_squares([]))
print(corn.sum_of_squares([-2, 2]))
print(corn.sum_of_squares([6]))
