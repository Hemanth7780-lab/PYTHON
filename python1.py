"""
#comparison operaters
a = 10
b = 20

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a <= b)
print(a >= b)

#age eligibility checker
age = int(input("enter your age:"))

print("eligible:", age >= 18)

#pass or fail checker
marks = int(input("enter marks:"))

print("pass:", marks >= 40)

#login validation
correct_username = "admin"
correct_password = "1234"

username = input("Enter username: ")
password = input("Enter password: ")

print(username == correct_username)
print(password == correct_password)

#logical operators
age = 25
citizen = True

print(age >= 18 and citizen == True)

age = 16
citizen = True

print(age >= 18 and citizen == True)

has_card = False
has_cash = True

print(has_card or has_cash)


is_logged_in = True

print(not is_logged_in)

#atm eligibility checker
balance = 1000
withdraw = 5000

print(withdraw > 0 and withdraw <= balance)

#student scholarship eligibility checker
marks = float(input("Enter marks:"))
attendance = float(input("enter attendance"))

eligible = marks >= 85 and attendance >= 75

print("scholarship eligible:", eligible)

#identity operators
a = None

print(a is None)
print(a is not None)

#bitwise operators
a = 5 
b = 3

print(a & b)
print(a | b)
print(a ^ b )
print(a << b)
print(a >> b)

#electric city bill calculator
units = int(input("Enter electricity units:"))

rate = 6

bill = units * rate

print("electricity bill:", bill)

#travel expense  calculator
travel = float(input("travel expense"))
food = float(input("food expense"))
hotel = float(input("hotel expense"))

total = travel + food + hotel 

print("total expense:", total)

#list in pyhton
#list is an ordered and changeable collection that can store 
marks = [80, 90, 75, 85]

print(marks)

#accessing elements in a list
marks = [80, 90, 75, 85]

print(marks[0])
print(marks[1])
print(marks[2])

num = [77, 69, 92, 79, 86, 42, 67]

print(num[2])
print(num[4])
print(num[6])

#change elements in a list
marks = [80, 90, 75]

marks[1] = 95

print(marks)

#add elements to a list 
marks = [80, 90, 75]

marks.append(85)

print(marks)

#remove elements from a list 
marks = [80, 90, 75]

marks.remove(90)

print(marks)

#insert elements in a list 
number = [10, 20, 30]

number.insert(1, 15)

print(number)

number = [10, 20, 30, 40]

number.insert(1, 15)
number.insert(2, 25)

print(number)

#extend method
a = [1, 2, 3]
b = [4, 5, 6]

a.extend(b)

print(a)

#clear method 
numbers= [10, 20, 30,]

numbers.clear

print(numbers)

#index method
numbers = [10, 20, 30, 40]

print(numbers.index(30))

#count method 
numbers = [10, 20, 30, 40, 50, 60]

print(numbers.count(20))

#sort method 
numbers = [40, 10, 30, 20]

numbers.sort()

print(numbers)

numbers.sort(reverse=True)

print(numbers)

#reverse method 
numbers = [10, 20, 30, 40]

numbers.reverse()

print(numbers)

#copy method
a = [1, 2, 3]

b = a.copy()

print(b)

#
numbers = [10, 20, 30, 40, 50]

print(numbers[1:4])
print(numbers[:3])
print(numbers[2:])
print(numbers[::-1])

#tuples in python
#tuple is a collection of multiple values that is ordered and cannot be changed after creation 
student = ("bhargavi", 98, "python" )

print(student[0])
"""

#access values in a tuple
student = ("bhargavi", 21, 85.5)

print(student[0])
print(student[1])
print(student[2])

#immutable nature of tuples
student = ("bhargavi", 21, 85.5)

print(student[0])

#tuples are immutable, meaning they cannot be changed after
numbers = (10, 20, 40, 30) 

print(numbers.index(20))
numbers = (20, 30, 40, 50)

print(numbers.index(30))

numbers = (10, 20, 30, 40)

print(len(numbers))
print(max(numbers))
print(min(numbers))
print(sum(numbers))

#sets in python 
#set is a collection of uniqe values that is unordered and 
numbers = {10, 20, 30, 20, 10}

print(numbers)

#why use set?

#suppose students have selected subject
subjects = {"python", "java", "python", "SQL", "java"}

print(subjects)

#add values to a set 
subjects = {"python", "java"}

subjects.add("SQL")

print(subjects)

#remove values from a set
subjects.remove("java")

print(subjects)

#sets do not allow duplicate valus
numbers = {1, 2, 2, 3, 3, 4}

print(numbers)
