import random
def binarySearch(alist, item):
    first = 0
    last = len(alist)-1
    found = False

    while first<=last and not found:
        midpoint = (first + last)//2
        if alist[midpoint] == item:
            return midpoint
        else:
            if item < alist[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1
    return -1
            
n=int(input("Enter how many number "))
print("Enter", n , "numbers ")
num = []
for i in range(0, n):
    num.append(random.randrange(0,100))
num.sort()
print(num)
Sitem=int(input("Enter the search item "))
posin = binarySearch(num, Sitem)
if (posin == -1):
    print("Element not found ")
else:
    print("Element found at ", posin+1)
