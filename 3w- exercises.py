#2
temp=input("choose temp to convert")
if temp=="cel":
    c = int(input("enter temp in celsius"))
    print("the temp is",(c*9)/5+32,"Fahrenheit")
elif temp=="fah":
    f = int(input("enter temp in fah"))
    print("the temp is", ((f-32)*5)/90, "Celsius")

#3
x=sorted(list,reverse=True)
print(x)

#4
print(len(list))

#5
new.insert(1,78)
print(new)

#6
del new[3]
print(new)

#7
num = int(input("Enter a number: "))
num2 = num % 2
if num2 > 0:
    print("This is an odd number.")
else:
    print("This is an even number.")

8
from math import pi
a = float(input("enter radius of circle"))
print ("the area is" +" "+ str(a) + str(pi * a**2))

9
n = "54.236"
print(float(n))
print(int(float(n)))

10
for i in range(0, 10):
    print('*', end="")
print("\n")

11
num = int(input("Enter a number: "))
sum_num = (num * (num + 1)) / 2
print("Sum of the first", num ,"positive integers:", int(sum_num))

12
height = float(input("Enter height in Feet: "))
weight = float(input("Enter weight in Kilogram: "))
print("The body mass is: ", round(weight / (height * height), 2))


