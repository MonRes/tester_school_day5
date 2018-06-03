list1 = [1, 3, 5]
list2 = ['a', 'b', 'c']
list3 = []

for i in range(len(list1)):
    list3.append(list1[i])
    list3.append(list2[i])

print(list3)

list4 = []
for i, value in enumerate(list1):
    list4.append(value)
    list4.append(list2[i])
print(list4)

list5 = []
for first, second in zip (list1, list2):
    list5.append(first)
    list5.append(second)

print(list5)