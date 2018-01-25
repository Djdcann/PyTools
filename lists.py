def square(x):
    return x**2

# stuff that you should know about python lists
# declare list
l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# first 4 items
print l[:4]
# every item after 4
print l[4:]
# list from indexes 4 stop at 6
print l[4:6]
# Look at the last element
print l[-1]
# Select every second entry
print l[::2]
# Reverse a copy of the list
print l[::-1]

print map(square, l)

