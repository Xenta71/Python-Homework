def month_to_season(n):
    if n in{3,4,5}:
        return "Весна"
    elif n in{6,7,8}:
        return "Лето"
    elif n in{9,10,11}:
        return "Осень"
    elif n in{12,1,2}:
        return "Зима"
    else:
        return "Неверный номер месяца"


try:
    n = int(input("Введите номер месяца (1-12): "))
    print(month_to_season(n))
except ValueError:
    print("Пожалуйста, введите целое число от 1 до 12: ")
