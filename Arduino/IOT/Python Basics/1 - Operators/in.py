a = 10
b = 20
list = [1, 2, 3, 4, 5 ];


if ( a in list ):
   print ("Line 1 - a is available in the given list")
else:
   print ("Line 1 - a is not available in the given list")

if ( b not in list ):
   print ("Line 2 - b is not available in the given list")
else:
   print ("Line 2 - b is available in the given list")

a = 2
if ( a in list ):
   print ("Line 3 - a is available in the given list")
else:
   print ("Line 3 - a is not available in the given list")

c = "Hello"
H = "H"
if ( H in c ):
   print ("Line 4 - H is available in the given String")
else:
   print ("Line 4 - H is not available in the given String")
   
   
H = "M"
if ( H not in c ):
   print ("Line 4 - M is available in the given String")
else:
   print ("Line 4 - M is not available in the given String")
