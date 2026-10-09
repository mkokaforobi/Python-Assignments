print("       		       Multiplication Table			 ")
print("1	2	3	4	5	6	7	8	9")      
print("-------------------------------------------------------------------")

for index in range (1,10):
	for count in range (1,10):
		result = count * index
		print(result,  end="\t ")

	print()
	
