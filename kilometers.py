#program to convert kilometers into miles
# program creted by Dr. D.V. Manjunatha
# input the distance in kilometers

kilometers= float(input("Enter the distance in kilometers"))

#  consider the conversion factor

conversion= 0.621371

# code
miles= kilometers*conversion

print("%0.2f kilometer is equal to %0.2f miles" %(kilometers, miles))

