target = 100
list = [1, 100, 100, 100, 200]
count=0

to_delete = []
for idx, value in enumerate(list):
    if value == target:
        to_delete.append(idx)
for i in reversed(to_delete):
    del list[i]

print(list)