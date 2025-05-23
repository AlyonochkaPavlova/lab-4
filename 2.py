number = int(input("Введите номер места: "))
if number > 0 and number <= 25:
    if number % 2 == 0:
        type_place = 'Верхнее'
    else:
        type_place = 'Нижнее'
    location = 'Купе'
elif number >= 37 and number <= 52:
    # Боковые места
    if number % 2 == 0:
        type_place = 'Верхнее'
    else:
        type_place = 'Нижнее'
    location = 'Боковое'
else:
    print("Некорректный номер места")
    exit()
print(f"{type_place}, {location}")
