#Question 3
#Accepting list of numbers from user
a=input("Enter comma separated numbers in ascending order\n")
l=list(a.split(","))
fl=[int(i) for i in l]
#Accepting the number to be searched
num=int(input("Enter a number to be searched\n"))
#performing binary search assuming list has sorted elements
found=0
loc=0
low=0
high=(len(fl)-1)
while(low<=high):
	mid=low+((high-low)//2)
	if(fl[mid]==num):
		found=1
		loc=mid+1
		break
	elif(fl[mid]>num):
		high=mid-1
	else:
		low=mid+1
if(found==1):
	print("Number :",num," is found at location :",loc)
else:
	print("Number :",num," is not found in the list")

	

