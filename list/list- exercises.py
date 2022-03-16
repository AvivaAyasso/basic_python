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