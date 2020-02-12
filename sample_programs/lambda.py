x = int(input("Enter x:"))
y = int(input("Enter y:"))

product = lambda x , y : x * y
print("Product :", product(x, y))

# another example
add = lambda x, y: x + y

print("Sum :", add(x, y))
# Output: 8
