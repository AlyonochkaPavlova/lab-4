color1 = input("Введите первый основной цвет (красный/синий/желтый): ").strip().lower()
color2 = input("Введите второй основной цвет (красный/синий/желтый): ").strip().lower()

primary_colors = {"красный", "синий", "желтый"}

if color1 not in primary_colors or color2 not in primary_colors:
    print("Ошибка: введены неправильные цвета.")
elif color1 == color2:
    print("Вы ввели одинаковые цвета!")
else:
    if sorted([color1, color2]) == ["красный", "синий"]:
        result_color = "фиолетовый"
    elif sorted([color1, color2]) == ["красный", "желтый"]:
        result_color = "оранжевый"
    elif sorted([color1, color2]) == ["синий", "желтый"]:
        result_color = "зеленый"
    print(f"Смешивание цветов {color1} и {color2} даст {result_color}.")
