import math
import random
print ("------- Numberic Data Type------- ")
var1 = float(input("Enter the number Value 1--> "))
var2 = float(input("Enter the number Value 2--> "))
var3 = float(input("Enter the number Value 3--> "))

print ("-"*60)
print ("Absolute value of",var1," is ", abs(var1))
print ("-"*60)
print ("Ceiling value of",var3," is ", math.ceil(var3))
print ("-"*60)
print ("method exp() returns exponential of Value 1:", math.exp(var1))
print ("-"*60)
print ("math.pow(100, 2) : ", math.pow(100, 2))
print ("-"*60)
print ("round(80.23456, 2) : ", round(80.23456, 2))
print ("-"*60)
print ("Random numbers using random() : ", random.random())
print ("-"*60)
print ("Random numbers with range : ", random.randrange(0,200))
print ("-"*60)
print ("choice([1, 2, 3, 5, 9]) : ", random.choice([1, 2, 3, 5, 9]))
print ("-"*60)
print ("choice('A String') : ", random.choice('A String'))


