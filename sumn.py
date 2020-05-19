# program to find sum of natural numbers
# Written by Dr. D.V. Manjunatha
num=5

if (num<0):
	print("Enter the Positive nummber")
else:
	sum=0
while(num>0):
	sum+=num
	num-=1
print(" the sum is >>>", sum)

