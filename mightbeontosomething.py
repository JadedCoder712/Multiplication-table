width =  10 #input("What is the width?")
height = 8 #input("What is the height?")

mylist = range(1, int(width) +1)
n = 5

 
#loop
while n <= int(height):
      n = n + 1
      for b in mylist:
        b = b * n
        for b in mylist:
            print(, end="  ")        #, end = " ")
