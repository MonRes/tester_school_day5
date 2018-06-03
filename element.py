a = 2
b = 20
c = 4


delta = b ** 2 - 4 * a * c

if delta < 0:
    print ('nie ma pierwiastków')
elif delta == 0:
    print (-b / (2*a))
else:
    x1 = (-b + delta ** 1/2) / (2 * a)
    x2 = (-b - delta ** 1/2) / (2 * a)
    print ('Rozwiązania: ', x1, x2)