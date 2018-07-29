var1=int(input("Enter the first number:"))
var2=int(input("Enter the second number:"))
opr=input("Enter the operator:")
if(opr=='+'):
    var3=var2+var1
    print("The sum of ", var1, "and ", var2, " is:", var3)
elif(opr=='-'):
    var3=var1-var2
    print("The difference of ", var1, "and ", var2, " is:", var3)
elif(opr=='*'):
    var3=var2*var1
    print("The product of ", var1, "and ", var2, " is:", var3)
elif(opr=='/'):
    var3=var1/var2
    print("The quotient of ", var1, "and ", var2, " is:", var3)
else:
    print("Please enter a valid operator!!")
