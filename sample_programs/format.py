from math import sqrt
a = int(input("Enter a range of numbers : "))
for i in range(0, a):
    print("Square of {0} is {1}".format(i, i*i))
    print("Squareroot of {0} is {1}".format(i, sqrt(i)))