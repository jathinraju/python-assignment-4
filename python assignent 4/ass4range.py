#check whether the number is in given range
def ran(n) :
	if n in range(0,1000) :
		print(n ,"is in range only")
	else :
		print("the number is not in given range.")
y = int(input("enter a number to check in range r not"))
ran(y)