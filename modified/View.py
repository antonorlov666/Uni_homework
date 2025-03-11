# View

def inputs(): #функция вводов
    return (int(input("Введите число a: ")),
            int(input("Введите число b: ")),
            input("Введите операцию (+, -, *, /, ^, V, %, NOD, sin, cos, sqr_trian, sqr, crcl(d), pyr, kyb): "))

def display_result(result): # функция для вывода результатов
    print(f"Результат: {result}")

def display_error(message): #функция для вывода ошибок
    print(f"Ошибка: {message}")