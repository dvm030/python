string=input("Enter the string")
char=0
word=1
for i in string:
	char=char+1
	if(i==''):
		word=word+1
print("number of wors in the string:")
print(word)
print("Number of charectors in the string:")
print(char)

