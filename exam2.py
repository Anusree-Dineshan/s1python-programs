def pal(n):
	s=0
	temp=n
	while(n>0):
		r=n%10
		s=s*10+r
		n=n//10
	if(temp==s):
		print("Number is palindrome")
	else:
		print("Number is not palindrome")
f=int(input("Enter the number:"))
pal(f)