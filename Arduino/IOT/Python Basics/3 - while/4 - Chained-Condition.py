while True:
    print ("1 -- >Addition of Numbers")
    print ("2 -- >Mutiplication of Numbers")
    print ("3-- >Substraction of Numbers")
    print ("4 -- >Division of Numbers")
    choice = int(input("Enter your Choice"))
    if choice == 1:
        print ("Addition of two Numbers")
        a = int(input("Enter the 1st number\n"))
        b = int(input("Enter the 2nd number\n"))
        c = a+b
        print ("-"*60)
        print (c)
        print ("-"*60) 
    elif choice == 2:
        print ("Multiplication of two Numbers")
        a = int(input("Enter the 1st number \n"))
        b = int(input("Enter the 2nd number \n"))
        c = a*b
        print ("-"*60)
        print (c)
        print ("-"*60)
    else:
        print ("Invalid Choice")

    
