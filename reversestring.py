a=input("Enter string:")
print(a,"Is the given string")
print(len(a),"is the length of the given string")
b=""
print("The characters in the string are:")
for i in range(0,len(a)):
	print(a[i])
print("The characters in the reverse order of the string are:")
j=0
for i in range(len(a)-1,-1,-1):
	b+=a[i]
	j=j+1
print(b)