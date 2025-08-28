import random
while True:
    print ("1---------> Creating a List")
    print ("2---------> Repitation of List")
    print ("3---------> Length of List")
    print ("4---------> Concatenation of List")
    print ("5---------> Membership opperation of List")
    print ("6---------> Iteration of List")
    print ("7---------> Slicing of List1")
    print ("8---------> Minimum of List1")
    print ("9---------> Maximum of List1")
    print ("10---------> deleting of List elements ")
    print ("11---------> Exit")
    ch=int(input("Enter your choice\n"))
    if ch==1:
        list1=[]
        list2=[]
        n = int(input("Enter the List Size\n"))
        print ("Enter the first List Elements ")
        for i in range(0,n):
            list1.append(random.randrange(0,100))
        print ("Enter the Second List Elements ")
        for i in range(0,n):
            list2.append(random.randrange(0,100))
        print("-"*60)
        print (list1)
        print (list2)
        print("-"*60)
    if ch==2:
        r=int(input("Enter the number for repitation of List1*"))
        print("-"*60)
        print("Repitation of list1*%d is =>"%(r),(list1*r))
        print("-"*60)
    if ch==3:
        print ("Length of List1 is =>", len(list1))
        print ("Length of List2 is =>", len(list2))
    if ch==4:
        print("-"*60)
        print ("concetination two list is",list1+list2)
        print("-"*60)
    if ch==5:
        m=int(input("Enter the element to searched in the list"))
        print("-"*60)
        print ("Membership Operation %s in list1 =>" %(m),(m in list1))
        print("-"*60)
    if ch==6:
        print("Iteration operation for list1")
        print("-"*60)
        for i in list1:
            print (i)
        print("-"*60)
    if ch==7:
        a=int(input("Enter Starting Index of List1 =>"))
        b=int(input("Enter Ending Index of List1 =>"))
        print("-"*60)
        print ("Slicing operation list1[%d:%d]" %(a,b),(list1[a:b]))
        print("-"*60)
    if ch==8:
        print("-"*60)
        print ("Minimum item in list1 => ", min(list1))
        print("-"*60)
    if ch==9:
        print("-"*60)
        print ("Maximum item in list1 => ", max(list1))
        print("-"*60)
    if ch==10:
        print (list1)
        x=int(input("Enter the Index of List1 to delete => "))
        print("-"*60)
        print ("deleting element of list1[%s]" %(x), ( list1.remove(x)))
        print (list1)
        print("-"*60)
        
