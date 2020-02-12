from functools import reduce

# Here the results of previous two elements are added to the next element and
# this goes on till the end of the list like (((((5+8)+10)+20)+50)+100).
li = [5, 8, 10, 20, 50, 100]
result = reduce((lambda x, y: x + y), li)
print(result)