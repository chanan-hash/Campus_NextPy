import functools

# 1.2.1
a = lambda x: 1
#returns the argument 1 allways
print(a(3))
print(a("s"))
print(a(2))
print(type(a(3)))

#1.2.2
b = lambda x: x
# returns the argument x
#b = lambda x: x*1
#b = lambda x: 0+x
print(b(1))
print(b(3))

#1.2.3
c = lambda x, y: x+y
print(c(1, 3))
print(c(2, 5))

#1.2.4
d = lambda x, y: y
# returns the argument y
print(d(1, 3))
print(d(5, 2))

#1.2.5

def function(num, item):
    return num + 1
# add 1 to a number

password = input("Enter Your password (integers only): ")

lst = list(map(int, password))
# the map making list of int (number) from the password

magic = functools.reduce(function, lst)
# the reduce add to the first number of the password the function "function" (adding 1), the times of the number in the list after the first number
# 1+1+1 (because we have three nubmer after the first number)
result = (lambda x: x % 4 == 0)(magic)
# cheking if the new number can be divided by four (4)

if result:
    print("Correct password!")
else:
    print("Wrong password.")

# correct answer 1234
