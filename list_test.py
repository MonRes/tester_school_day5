number = [1, 4, -3, 0]
empty = []

print ('Element o indeksie 1 to: ', number[1])
print ('Ilośc elementów na liście', len(number))

number[2] = 10
print (number[2])

for i in range(len(number)):
    print (number[i])

#preferowane w pythonie niż range
for value in number:
    print(value)

for char in 'Ala ma kota':
    print (char)