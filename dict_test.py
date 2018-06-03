marks = {'John': 5.0, 'Sue': 3.0}

print(marks['John'])
marks['Sue'] = 4.0
marks['Anne'] = 3.0
print(marks)

for key in marks:
    print(key, marks[key])

for name, mark in marks.items():
    print(name, mark)

for mark in marks.values():
    print(mark)