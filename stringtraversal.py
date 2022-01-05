a=input("Enter string:")
print(a,"Is the given string")
print(len(a))
print("The characters in the string are:")
for i in range(0,len(a)):
	print(a[i])
print("The characters in the reverse order of the string are:")
for i in range(len(a)-1,-1,-1):
	print(a[i])