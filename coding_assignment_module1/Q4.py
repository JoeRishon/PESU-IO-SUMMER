#Question4
#Accepting number from user
num=int(input("Enter a number:"))
su=0
while(num>0):
    dig=num%10
    su=su+dig
    num=num//10
print("The total sum of digits is:",su)
