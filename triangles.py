a = 2
b = 4
c = 4

if a>0 and b>0 and c>0:
    if a + b > c and a + c > b and b + c > a:
        print ("da się utworzyć trójkąt")
    else:
        print ("nie da się")
else:
    print("nie da się")

#lub preferowana wersja

if a <= 0 or b <= 0 or c <= 0:
    print ('nie da się utworzyć trójkąta - któras długość jest ujemna')
elif a + b > c and a + c > b and b + c > a:
    print ('Da się  utworzyć trójkąt')
else:
    print ('nie da się utworzyć trójkąta')

#mozna z powtarzającego się warunku utworzyć zmienną np. length_negative = a <= 0 or b<= 0 c <= 0