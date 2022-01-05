def prime(low,high):
	for num in range(low,high+1):
		if(num>1):
			for i in range(2,num):
				if(num%i==0):
					break
				else:
					print(num)
					break
LOW=int(input("Enter lower range:"))
HIGH=int(input("Enter higher range:"))
prime(LOW,HIGH)

