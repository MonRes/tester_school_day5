a = 3
b = 3
c = 1

if a+b>c and a>0 and b>0 and c>0:
    print ('podane liczby mogą być bokami trójkąta')

elif a+c>b and a>0 and b>0 and c>0:
    print ('podane liczby moga być bokami trójkąta')

elif b+c>a and a>0 and b>0 and c>0:
    print ('podane liczby mogą być bokami trójkąta')

else:
    print ('to nie jest trójkąt')