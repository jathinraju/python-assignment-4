# to find maximum of three numbers
def three(a,b,d) :
	if a>b and a>d :
		print(a," is maximum")
	elif b>a and b>d :
			print(b," is maximum")
	else :
		print(d," is maximum")
x = int(input("enter a number x :"))
y = int(input("enter a number y :"))
z = int(input("enter a number z :"))
three(x,y,z)
