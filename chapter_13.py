#  lambda function.
'''
# def func(a):
#     return a+5

func = lambda a: a+5
square = lambda x: x*x
sum = lambda a, b, c: a+b+c

x = 3
print(func(x)) # prints 8
print(square(x)) # prints 9
print(sum(x, 1, 2)) # prints 6
'''

#  .join method. list, tuple all allow
'''
l = ["Camera", "Laptop", "Phone", "ipad", "Hard Disk", "Nvidia Graphic 3080 card"]

sentence = " and ".join(l)
print(sentence)
print(type(sentence))
'''

#  .formet function.
'''
name = "Harry"
channel = "CodeWithHarry"
type = "Coding"
# a = f"This is {name}"

# a = "This is {}".format(name)

# a = "This is {} and channel is {}".format(name, channel)
# a = "This is {0} and his {2} channel is {1}".format(name, channel, type)
a = "This is {} and his {} channel is {}".format(name, channel, type)
print(a)
'''

#  map filtaring.
'''
def square(num):
    return num*num

l = [1, 2, 4]

# Method 1
l2 = []
for item in l:
    l2.append(square(item))
print(l2)

# Method 2
print(list(map(square, l)))
'''

#  filter.
'''
def greater_than_5(num):
    if num > 5:
        return True
    else:
        return False

g10 = lambda num: num>70

l = [1, 2, 3, 4, 5, 65, 87, 54, 36, 87, 43, 77]
print(list(filter(greater_than_5, l)))
print(list(filter(g10, l)))
'''

# reduce.
'''
from functools import reduce

sum = lambda a, b: a+b

l = [1, 2, 3, 4]

value = reduce(sum, l)
print(value)
'''