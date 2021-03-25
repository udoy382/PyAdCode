# -------------------------------------
# Python chapter 12 practice set
# -------------------------------------

#  (1) handle file not found error
'''
def readFile(filename):
    try:
        with open(filename, "r") as f:
            print(f.read())
    except FileNotFoundError:
        print(f"File {filename} is not found")


readFile("1.txt")
readFile("2.txt")
readFile("3.txt")
'''

#  (2)
'''
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for index, item in enumerate(my_list):
    if index==2 or index==4 or index==6:
        # print(index, item)
        print(f"The {index+1}th element is {item}")
'''

#  (3) make a multiplaction table
'''
num = int(input("Enter you number: "))

table = [num*i for i in range(1, 11)]
print(table)
'''

#  (4) display a/b
'''
a = int(input("Enter number a: "))
b = int(input("Enter number b: "))

try:
    print(a/b)
except:
    print("Infinite")
'''

#  (5) make a multiplaciton table in file
'''
num = int(input("Enter you number: "))

table = [num*i for i in range(1, 11)]
print(str(table))

with open("table.txt", "a") as f:
    f.write(str(table))
    f.write('\n')
'''