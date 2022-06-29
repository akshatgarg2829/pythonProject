#
# print("Hello world")
# a = input()
# print(a)
#
# a = input("Enter your number:")
# print(a)
#
# a = input("Enter your name:")
# print("Hello",a,"How is your day going?")
# b = input()
# print("Okay fine.")
#

#
# l1 = [1,2,3,1.0,"Akshat"]
# print(l1)
# print(type(l1))
# print(type(l1[1]))
# print(type(l1[3]))
# print(type(l1[-5]))
# print(l1[-5])
# elem = int(input("Enter the number you want to append in the list:"))
# l2 = l1.append(elem)
# print(l1)



l1 = [3,3,1,1,1,1,2,1.0]
# elem = int(input("Enter the element you want ot insert in the list:"))
# l1.insert(2,elem)
# print(l1)

# remove function
# l1.remove(2)
# print(l1)
#
# # count function
#
# print(l1.count(1))
# print(len(l1))
# print(l1)
#
# # sort function
# l1.sort()
# print(l1)
#
# # reverse function
# l1.reverse()
# print(l1)

#
# l2 = [9,2,3,4,5,6]
# l1.append(56)
# l1.append(57)
# l1.append(59)
# l2.append(65)
# l2.append(66)
# l2.append(67)
# l1.append(l2)
# print(l1)

# # dictionary
# d2 = {
#     'akshat' : 2,
# }
# print(d2)
#
# #inserting an element in the dictionary
# d2["hello"] = 3
# d2["Bye"] = 4
# print(d2["hello"])
# print(d2)
#
# # deleting an element from the dictionary
# del d2["hello"]
# print(d2)


# loops
# for loop with range function
# for loop with one parameter
# for i in range(10):
#     print(i)

# for loop with two parameters
# for i in range(5,10):
#     print(i)

# for loop with three parameters
# for i in range(5, 10, 2):
#     print(i)


# for loop without range function
#
# l2 = [3, 4, 5, 6]
# d2 = {
#     "Hello" : 3
# }
# for i in l2:
#     print(i)
# for i in d2:
#     print(i)

# functions
# functions without parameters
def add():
    a = 5
    b = 6
    print(a + b)
add()

# functions with parameters

# def user_inputs():
#     name = input("Enter your name:")
#     age = int(input("Enter your age:"))
#     print("Your name is", name)
#     print("Your age is", age)
# user_inputs()

#
# def user(n, a):
#     print("Your name is", n)
#     print("Your age is", a)
# name = input("Enter your name:")
# age = int(input("Enter your age:"))
# user(name, age)


# function returning values

def user():
    name = input("Enter your name:")
    age = int(input("Enter your age:"))
    return name, age
name, age = user()
print("Your name is:", name)
print("Your age is:", age)