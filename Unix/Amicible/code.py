import math
c=input("Enter number")
sum=1
sqrtNum=math.sqrt(c)
for i in range(1,c):
	if(c%i==0):
		print i