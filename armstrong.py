n=int(input("Enter the number:"))
a=list(map(int,str(n)))
b=list(map(lambda x:x**3, a))
if(sum(b)==n):
	print(" The number is Armstrong NUmber:")
else:
	print("The number is not an armstrong number:")


