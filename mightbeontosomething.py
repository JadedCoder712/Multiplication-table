width = input("What is the width? ")
height = input("What is the height? ")

mylist = range(1, int(width) +1)
n = 0
end1="  "
 
#loop
while n <= int(height):
    n = n + 1
    for b in mylist:
        temp = b * n
        if temp < 10:
            print(b * n, end="   ")
        else:
            print(b * n, end="  ")
    print("")