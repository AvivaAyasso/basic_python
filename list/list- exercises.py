1
list = []
list.append("aviva")
print(list)
list.append("betty")
print(list)
list.append("rivka")
print(list)
list.append("simch")
print(list)
print(len(list))
list.insert(1,"avi")
print(list)
print(list[2])
del list[4]
print(list)
name = sorted(list)
print(name)

2
ls1 = [1, 4, 7]
ls2 = [2, 5, 8]
ls3 = [3, 6, 9]

ls4 = [ls1, ls2, ls3]
for i in range(len(ls4)):

3
t1 = (1, 2, 3, 7, 9)
t2 = (4, 5, 6, 8, 11)
ls = [t1, t2]
ls1 = []
print(t1, t2)
print(t1[3], t2[3])
print(t1[2:4], t2[2:4])
print(ls)
ls.append(3)
print(ls)

#2
num = []
for i in range(1, 10):
    num.append(i)
print(num)
#3
name = []
for i in range(10):
    i = input("enter a name")
    name.append(i)
    name.sort()
print(name)

#4
l = []
sum = 0
for i in range(11):
    num = input("enter a number")
    l.append(int(num))
    sum += int(num)
print(sum)
above10 = 0
below10 = 0
max = l [0]
count = 0
count1 = 0
for i in l:
    print(i/11)
    if i > 10:
        above10 += 1
    else:
        below10 += 1
        max = i
if l % 2 == 0:
        count += 1
if l % 3 == 0:
        count1 += 1

print(above10, "above 10")
print(below10, "below 10")
print(max)
print(count)
print(count1)

#5




#6
l1 = []
l2 = []
for i in range(6):
    l1.append(int(input("enter a number")))
    l2.append(int(input("enter a number")))
for i in l1:
    for j in l2:
        if i == j:
            print(i, "in bout")

#7
shvil = []
sum = 0
for i in range(5):
    name = input("enter a name")
    dist = int(input("enter a number"))
    shvil.append([name, dist])
    sum += dist
    if dist > 10:
        print(list)
