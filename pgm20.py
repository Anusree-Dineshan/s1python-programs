#def functions
def add(x,y):
	"""This functions adds two numbers"""
	return x+y
def subtract(x,y):
	"""This functions subtracts two numbers"""
	return x-y
def multiply(x,y):
	"""This functions multiply two numbers"""
	return x*y
def divide(x,y):
	"""This functions divides two numbers"""
	return x/y
def pow(x,y):
	"""This functions computes power of the numbers"""
	return x**y
def mod(x,y):
	"""This function computes modulus operator"""
	return x%y
# take input from the user
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Power")
print("6.Modulus")

choice = input("Enter choice(1/2/3/4/5/6):")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if choice=='1':
	print(num1,"+",num2,"=",add(num1,num2))
elif choice=='2':
	print(num1,"-",num2,"=",subtract(num1,num2))
elif choice=='3':
	print(num1,"*",num2,"=",multiply(num1,num2))
elif choice=='4':
	print(num1,"/",num2,"=",divide(num1,num2))
elif choice=='5':
	print(num1,"^",num2,"=",pow(num1,num2))
elif choice=='6':
	print(num1,"%",num2,"=",mod(num1,num2))
else:
	print("Invalid input")
