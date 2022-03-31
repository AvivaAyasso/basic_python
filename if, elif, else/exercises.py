#משתנה זה פוינטר(מצביע על..), לא יוצר העתק!
#יש שתיי סוגי משתנים מיוטובול ואן מיוטובול. אן מטיובל ניתן לשנות ומיוטובול לא ניתן לשנות
#אינט סטירג פולוט הם מסוג אן מיוטבובול

#קוד ללוה שמסכמת את כל המספרים בין 0 ל32 אבל שהסכום גדול מ-20 תדפיסו כמה אברים היה צריך לחבר כדי להערך הגדול מ-20


#11
count1 = 0
count2 = 0
for i in range(0, 52):
     if i % 2 == 0:
         count1 += 1
     if i % 4 == 0:
        count2 += 1
print("evenNumber:", count1)
print("unevenNumbers%4:", count2)

#12
num = int(input("enter a number"))
if num < 50:
    print("the number is smaller then 50")
else:
    print("the number bigger then 50")

#13
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

#14
num = int(input("enter a number"))
if num % 2 == 0:
    print(num)

#15
num = int(input("enter a number"))
if num < 40:
    if num % 2 == 0:
        print(num)

#16
num = int(input("enter a number"))
if num > 100:
    print(num * 5)
elif num < 100:
    print(num * 10)
elif num == 100:
    print(num + 10)

#17
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
if name[0] == 'a' or name[0] == 'b':
    print("ok")
else:
    print("not good")

#19
for i in range (1,100):
    if i % 7 == 0:
        print("boom")
    elif '7' in str (i):
        print("boom")
    else:
        print(i)

#Find the highest of two numbers
num = int(input("enter a bunmber"))
num1 = int(input("enter a secand number"))
if num > num1:
    print("The highest number is :",num)
else:
    print("The highest number is: ",num1)

#Find the highest number out of three numbers
num = int(input("enter a bunmber"))
num1 = int(input("enter a secand number"))
num2 = int(input("enter a third number"))
if num > num1 and num > num2:
    print("The highest number is:",num)
elif num1 > num2:
    print("The highest number is :",num1)
else:
    print("The highest number is:",num2)

#Find the highest number out of three numbers or if the numbers are equal
num = int(input("enter a bunmber"))
num1 = int(input("enter a secand number"))
num2 = int(input("enter a third number"))
if num > num1 and num > num2:
    print("The highest number is: ",num)
elif num1 > num2:
    print("The highest number is :",num1)
elif num == num1 == num2:
    print("the numbers'r equal")
else:
    print("The highest number is :",num2)

#Calculation of payment in the parking lot by the hour
hour = int(input("Enter the length of time you will be in the parking lot"))
if hour <= 3:
    print("The amount to be paid is", 20*hour, "NIS")
elif hour > 3 and hour < 5 :
    print("The amount to be paid is :", 15*hour, "NIS")
elif hour > 5 and hour < 24:
    print("The amount to be paid is :", 10*hour, "NIS")
else:
    print("The amount to be paid is :", 5*hour, "NIS")

#Calculation of payment in the parking lot by the hour including discount
hour = int(input("Enter the length of time you will be in the parking lot"))
year = int(input("Enter the year of the car"))
electric = input("Is the vehicle electric?")
pay = 0

if hour <= 3:
    pay = hour*20
elif hour > 3 and hour < 5:
    pay = hour*15
elif hour > 5 and hour < 24:
    pay = hour*10
else:
    pay = hour*5

if year ==2022 and electric == ("yes"):
    print("The amount to be paid is :",pay-(pay*0.20),"NIS")
elif year ==2022:
    print("The amount to be paid is :",pay-(pay*0.15),"NIS")
else:
    print("The amount to be paid is :",pay-(pay*0.10),"NIS")
