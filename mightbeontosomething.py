width =  10 #input("What is the width?")
height = 8 #input("What is the height?")

mylist = range(1, int(width) +1)
n = 0
end1="  "
 
#loop
while n <= int(height):
    n = n + 1
    for b in mylist:
        if mylist[3] >= 10:
            print(b * n, end=end1)
        else:
            print(b * n, end=" ")
    print("")
    
    
    """
    if endnumber >=10:
        then end= " "
        
        """
        
        