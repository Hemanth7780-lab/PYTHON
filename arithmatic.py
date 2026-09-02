#Arithmatic
a = 10
b = 20
print("Addition:", a + b)
print("subtraction:", a - b)
print("multiplication:", a * b)
print("division:", a / b)
print("floor division:", a // b )
print("remainder:", a % b)
print("power:", a ** b )

#simple calculator
a = int(input("enter first number"))
b = int(input("enter second number" ))

print("Addition:", a +b) 
print("subtraction:", a - b)
print("multiplication:", a * b)
print("division:", a / b)

#student mark calculator
name = input("enter student name:")

m1 =int(input("enter python marks:"))
m2 =int(input("enter java marks:"))
m3 =int(input("enter sql marks:"))
        

t = m1 + m2 + m3
average = t/3                                                 

print("\n----- student report -----")
print("name:", name )
print("total:", t)
print("average:", average)

#shopping bill calculator
price1 = float(input("enter product 1 price:"))
price2 = float(input("enter product 2 price:"))
price3 = float(input("enter product 3 price:"))

total = price1 + price2 + price3

discount = total * 0.10
final_amount = total - discount
 print
print("discount:",discount)
print("total amount:", amount)
print









#salary calculator
basic = float(input("enter basic salary:"))

hra = basic * 0.20
da = basic *0.10

gross_salary  basic + hra + da

print("basic salary:", basic)
print("hra:", hra)
print("da:", da)
print("gross_salary:", gross_salary)
