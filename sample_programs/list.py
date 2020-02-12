a = list("123")
print("list a:", a)

odd = [1, 3, 5]
# Output: [1, 3, 5, 9, 7, 5]
print(odd + [9, 7, 5])
# Output: ["re", "re", "re"]
print(["re"] * 3)

odd.insert(1, 3)
# Output: [1, 3, 9]
print(odd)
odd[2:2] = [5, 7]
# Output: [1, 3, 5, 7, 9]
print(odd)
print(odd.reverse())

pow2 = [2 ** x for x in range(10)]
print(pow2)

for fruit in ['apple', 'banana', 'mango']:
    print("I like", fruit)
