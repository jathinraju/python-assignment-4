#find factorial of a number
def factorial(n):
	if n==0 or 1:
		return 1
	else:
		return n*factorial(n-1)
n=int(input("enter a number :"))
print(factorial(n))