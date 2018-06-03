n = 65
i = 0

square = False
current_sqr = i ** 2

while current_sqr <= n :
    if current_sqr== n:
        square = True
    i += 1
    current_sqr = i ** 2
if square:
    print ('n jest kwadratem')
else:
    print ('n nie jest kwadratem')