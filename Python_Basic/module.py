import math
import calculator
num=int(input("Enter a number:"))
s=math.sqrt(num)
print("The square root of ",num," is ",s)
num1=int(input("Emter another number:"))
print("The sum of the number are:",end=' ')
calculator.add(num,num1)