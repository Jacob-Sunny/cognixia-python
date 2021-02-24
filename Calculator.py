#importing math package
import math
#method declerations
def add(num1,num2):
    return num1 + num1
def substract(num1,num2):
    return num1 -num2
def multipilcation(num1,num2):
    return num1 * num2
def division(num1,num2):
    return num1 / num2
def fifthFunction(num1,num2):
    pass
def squareRoot(num1):
    return math.sqrt(num1)

#method calls
first_number = 10
second_number = 10
squareNum = 49
print("Addition:",add(first_number,second_number))  
print("Subtraction:",substract(first_number,second_number))
print("Multiplication:",multipilcation(first_number,second_number))
print("Division(float)",division(first_number,second_number))
print("Square Root of 49:",squareRoot(squareNum))  