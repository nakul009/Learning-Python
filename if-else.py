if 9 > 0:
    print("I m here")
else:
    print("I m not here")
if 9 > 10:
    print("I m also here")
else:
    print("I am also not here")

# Relational Operators in Python  > , < , >= , <= , != , == #
print(3 >= 3)
print(4 != 3)
print(5 == 5)

# Nested If - Else in Python #

marks = 50
marksinPython = 90
if(marks > 33):
    if(marksinPython > 89):
        print("Congrats You passed exam with good python skills")
    print("Congrats You passed the exam with Grade A")


# Logical Operators in Python   and,or #

if(5 > 2 and 3 > 2):
    print("I am using Logical operators")
else:
    print("I am not using it")

if(5 > 2 and 3 < 2):
    print("I am using Logical operators")
else:
    print("I am not using it")

if(5 > 2 or 3 < 2):
    print("I am using  OR Logical operators")
else:
    print("I am not using it")


# Loops in Python for, while #
for i in range(0, 5):
    print("Hey")
x = [10, 20, 30]
for i in range(0, len(x)):
    print(x[i])
tuple4 = (22, 33, 44)
for i in range(0, len(tuple4)):
    print(tuple4[i])
for i in range(100, 0, -10):
    print(i)

# while  Loop #

y = 5
while y < 8:
    print(y)
    y = y+1

# Break  , Pass , Continue #
for i in range(0, 100):
    if(i == 5):
        break
    elif(i == 2):
        print("%d" %i + "yes i am here")
    else:
        pass
