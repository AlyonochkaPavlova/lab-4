def is_leap_year(year):
    if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
        return False
    else:
        return True
year = int(input("Введите год: "))
if is_leap_year(year):
    print(f'Год {year} - високосный')
else:
    print('Это год не високосный')
