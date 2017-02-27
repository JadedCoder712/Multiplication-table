#input:

x = input("What is the width?")
y = input("What is the height?")

#realtalk:

somenumbers = range(1, int(x))

"""
two = lambda a: (a * 2)
three = lambda b: (b * 3)
four = lambda c: (c * 4)
five = lambda d: (d * 5)
six = lambda e: (e * 6)
seven = lambda f: (f * 7)
eight = lambda g: (g * 8)

first = somenumbers
first = [g * 1 for g in somenumbers]
second = [g * 2 for g in somenumbers]
"""
multiple = [ [g * h for g in somenumbers] for h in range(1, int(x) + 1)]

print(multiple)
