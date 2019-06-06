#QUESTION 1
#Accepting comma seperated values
a=input("Enter comma-seperated values\n")
#Convert to list of strings
l1=a.split(",")
#Convert to list of numbers
fl=[]
for i in l1:
	fl.append(int(i))
#Tuple of numbers
tu=tuple(fl)
print("List -:",fl)
print("Tuple -:",tu) 


