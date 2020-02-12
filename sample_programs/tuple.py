# Empty tuple
my_tuple = ()
print(my_tuple)  # Output: ()
del my_tuple

# Tuple having integers
my_tuple = (1, 2, 3)
print(my_tuple)  # Output: (1, 2, 3)

# tuple with mixed data types
my_tuple = (1, "Hello", 3.4)
print(my_tuple)  # Output: (1, "Hello", 3.4)

# nested tuple
my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
print(my_tuple)  # Output: ("mouse", [8, 4, 6], (1, 2, 3))

my_tuple1 = 3, 4.6, "dog"
print(my_tuple1)   # Output: 3, 4.6, "dog"

# tuple unpacking is also possible
a, b, c = my_tuple1

print(a)      # 3
print(b)      # 4.6
print(c)      # dog

# Creating a tuple having one element
my_tuple2 = ("hello",)
print(type(my_tuple2))  # <class 'tuple'>

# Parentheses is optional
my_tuple2 = "hello",
print(type(my_tuple2))  # <class 'tuple'>

my_tuple3 = ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')
print(my_tuple3[1:4])  # Output: ('r', 'o', 'g')
print(my_tuple3[:-7])  # Output: ('p', 'r')
print(my_tuple3[7:])  # Output: ('i', 'z')
print(my_tuple3[:])  # Output: ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')
