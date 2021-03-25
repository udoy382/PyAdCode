#       error handaling
'''
while True:
    print("Press q to quit")
    a = input("Enter a number: ")
    if a == "q":
        break
    try:
        print("Tring...")
        a = int(a)
        if a>6:
            print("You entered a greater then 6")

    except Exception as e:
        print(f"Your input resulted an error {e}")

print("Thanks for playing this game!")
'''

#       different error
'''
try:
    a = int(input("Enter a number: "))
    c = 1/a
    print(c)
# except Exception as e:
#     print("Exception1 occured")
    # print(e)

except ValueError as e:
    print("Please enter a valid value")
    # print(e)

except ZeroDivisionError as e:
    print("Make sure you are not dividing by 0")
    # print(e)

print("Thanks for using this code!")
'''

#       creat a exception raise
'''
def increment(num):
    try:
        return int(num) + 1
    except:
        raise ValueError("This is not good - udoy")
a = increment('dfe34')
print(a)
'''

#       try with else, if try run without error so else print without not print
'''
try:
    i = int(input("Enter a number: "))
    c = 1/i
except Exception as e:
    print(e)
else:
    print("We were successful!")
'''

#       try with finally most importent finally run allwais
'''
try:
    i = int(input("Enter a number: "))
    c = 1/i
except Exception as e:
    # print(e)
    exit()
finally:
    print("We are done!")

print("Thanks for using the program")
'''

#       if __name__ == '__main__': ... most importent function
'''
def greet(name):
    print(f"Good morning {name}")

# print(__name__)

if __name__ == '__main__':
    n = input("Enter a name: ")
    greet(n)
'''

#       Local and Global variable
'''
a = 54 # Global Variabl
def func1():
    global a # Change global variable
    print(f"Print statment 1: {a}")
    a = 8 # Local Variable
    print(f"Print statment 2: {a}")

func1()
print(f"Print statment 3: {a}")
'''

#       enumerate function
'''
list1 = [1, 3, 54, False, 6.2, "Udoy"]
# index = 0
# for item in list1:
#     print(item, index)
#     index+=1

for index, item in enumerate(list1):
    print(item, index)
'''

#       list comprehension
'''
a = [3, 4, 5, 7, 6, 8, 23, 67, 1, 8, 6, 23, 75]
# b = []
# for item in a:
#     if item%2==0:
#         b.append(item)
# print(b)

#       shortcut to write the samme: for list

x = [i for i in a if i%2==0]
print(x)

#       for set
# t = [1, 1, 4, 4, 6, 77, 9, 9, 7,0]
# s = {i for i in t}
# print(s)
'''