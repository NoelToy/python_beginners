def Sum(a,b):
    c=a+b
    if(c%2==0):
        return True
    else:
        return False

var1=int(input("Enter the first number:"))
var2=int(input("Enter the second number:"))
if(Sum(var1,var2)):
    print("The sum is Even!")
else:
    print("The sum is Odd!!")