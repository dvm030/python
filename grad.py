maths= int(input('Enter the marks scored in mathematics:'))
AC= int(input('Entert the marks scored in Analog Electronics:'))
ss= int(input('Enter the marks scored in Signals and Systems:'))

avg=(maths+AC+ss)/3

if(avg>=90):
	print("Grade A")
elif(avg>= 80 & avg<90):
	print("Grade B")
elif(avg>=70 & avg<80):
	print("Grade C")
elif(avg>=60 & avg<70):
	print("Grade D")
elif(avg>=50 & avg<60):
	print("Grade E")
else:
	 print("Fail")

