#2
temp=input("choose temp to convert")
if temp=="cel":
    c = int(input("enter temp in celsius"))
    print("the temp is",(c*9)/5+32,"Fahrenheit")
elif temp=="fah":
    f = int(input("enter temp in fah"))
    print("the temp is", ((f-32)*5)/90, "Celsius")