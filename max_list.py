list = [0, 3, 7, 6, 4, 5, 2, 1]


for idx, value in enumerate(list):
    if idx == 0:
        current_min = value
        current_max = value
    elif current_max < value:
        current_max = value
    elif current_min > value:
        current_min = value

print ('Max is: ', current_max)
print ('Min is: ', current_min)