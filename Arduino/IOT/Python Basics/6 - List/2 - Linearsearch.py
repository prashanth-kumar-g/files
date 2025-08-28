import random
print ("-"*60)
print ("Linear Search Program")
print ("-"*60)
n=int(input("Enter how many number "))
print("Enter", n , "numbers ")
num = []
for i in range(0, n):
    #num.append(int(input("Enter the Number ")))
    num.append(random.randint(0,100))
print("The Number == > ", num)
Sitem=int(input("Enter the search item "))
found=False
for i in range(0, n):
    if(num[i] == Sitem):
        found=True
        break
if (found == True):
    print("Element found at", i+1)
else:
    print("Element not found")
