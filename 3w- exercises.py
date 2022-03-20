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