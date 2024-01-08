# Python program to convert Decimal to binary number
rem1=0
num=(int(input("Enter the number to convert: ")))
while(num>0):
    rem=num%2
    num=num//2
    rem1=rem1*10+rem
rem2=0
rem2=str(rem1)
size=len(rem2)
reverse=rem2[size::-1]
print(reverse)
