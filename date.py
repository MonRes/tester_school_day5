MONTH_LENGTHS = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

year = 2016
month = 2
day = 29

if month != 2:
    max_day = MONTH_LENGTHS[month-1]
elif (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    max_day = 29
else:
    max_day = 28
if day < max_day:
    new_year, new_month, new_day = year, month, day + 1
elif month == 12:
    new_year = year
    new_month = month + 1
    new_day = 1
else:
    new_year, new_month, new_day = year, month + 1, 1

print('Następna data: ', (new_day, new_month, new_year))