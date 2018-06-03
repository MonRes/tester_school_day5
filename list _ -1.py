numbers = [0, 4, 7, 9]

for i in range(len(numbers)-1, -1, -1):
    print(numbers[i])

for value in reversed(numbers):
    print(value)

for idx, value in enumerate(reversed(numbers)):
    print(idx, value)

for pair in enumerate(numbers):
    print(pair)