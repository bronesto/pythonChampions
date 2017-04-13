
def Menu():
	print("\t\tMenu Screen\n\n")
	print("1 - CREATE\n")
	print("2 - EDIT\n")
	print("3 - DELETE\n")
	print("4 - SEARCH\n")
	print("5 - PRINT OUT\n")
	print("6 - WRITE FILE\n\n")
	print("0 - LOG OUT\n")
	command = input('Enter your command: ') 
	command = eval(command)
	return command