#1
import math
num = int(input("enter a number"))
print(math.pow(num, 2))

#2
age = int(input("enter your age"))
print("in 20 years u will be:",age+20,"years old")

#3
price = int(input("enter a price"))
print(price*1.17)

#4
num1 = int(input("enter a number"))
num2 = int(input("enter a number"))
print(num1+num2,num1-num2,num1*num2,num1/num2)

#5
import datetime

x = datetime.datetime.now()
A = datetime.datetime.now()

print(x.strftime("%x"))
print(x.strftime("%A"))

#6
a = int(input("enter a number"))
b = int(input("enter a number"))
c = int(input("enter a number"))
d = int(input("enter a number"))

avg = (a+b+c+d)/4
print(avg)

#7
nails = int(input("enter nails numbers"))
box = int(nails/40)
print(box)

#8
distance = int(input("Enter a distance in kilometers"))
speed = int(input("Enter speed in km"))

hourtime = int(distance/speed)
minutetime = int(distance/speed)*60
print("minut", minutetime,"hours",hourtime)

#10
phone = (input("enter phone number without the first digit"))
print("the number is",'0' + phone)

11
count1 = 0
count2 = 0
for i in range(0, 52):
     if i % 2 == 0:
         count1 += 1
     if i % 4 == 0:
        count2 += 1
print("evenNumber:", count1)
print("unevenNumbers%4:", count2)

12
num = int(input("enter a number"))
if num < 50:
    print("the number is smaller then 50")
else:
    print("the number bigger then 50")

13
a = int(input("enter a number"))
b = int(input("enter a number"))
c = int(input("enter a number"))
if a > b and a > c:
    print(a)
elif b > a and b > c:
    print(b)
elif c > a and c > b:
    print(c)
if a < b and a < c:
    print(a)
elif b < a and b < c:
    print(b)
elif c < a and c < b:
    print(c)

14
num = int(input("enter a number"))
if num % 2 == 0:
    print(num)

15
num = int(input("enter a number"))
if num < 40:
    if num % 2 == 0:
        print(num)

16
num = int(input("enter a number"))
if num > 100:
    print(num * 5)
elif num < 100:
    print(num * 10)
elif num == 100:
    print(num + 10)

17
age = int(input("enter your age"))
height = float(input("enter your height"))
name = input("enter your name")
if age >= 18:
    print("Your age fits the requirements")
    if height > 1.56:
        print("Your height fits the requirements")
        if name[0] == 'a' or name[0] == 'b':
            print("Your name fits the requirements")
        else:
            print("Your name dont fits the requirements")
    else:
        print("Your height dont fits the requirements")
else:
    print("Your age dont fits the requirements")


if age >= 18:
    print("ok")
else:
    print("not good")
if height > 1.56:
    print("ok")
else:
    print("not good")
if name[0] == 'a' or name [0] == 'b':
    print("ok")
else:
    print("not good")

import sys
print("Python version")
print(sys.version)
print("Version info.")
print(sys.version_info)

name = input("enter a name")
# n = len(name)
for i in name:
    print(i,end= " ")
        # name[i], end=" ")

for i in range (1,100):
    if i % 7 == 0:
        print("boom")
    elif '7' in str (i):
        print("boom")
    else:
        print(i)