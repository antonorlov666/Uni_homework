# Controller

#Импорт из других фалов системы
from Model import *
from View import *



def main(): #основная(рабочая) функция
    while True: #бесконечный цикл (что бы не нужно было каждый раз перезапускать программу)
        a, b, operation = inputs()
        try:
            if operation == "+": #сложение
                result = summ(a, b)
            elif operation == "-":
                result = sub(a, b)#вычитание
            elif operation == "*":
                result = mult(a, b)#умножение
            elif operation == "/":
                result = div(a, b)#деление
            elif operation == "^":
                result = deg(a, b)#степень
            elif operation == "V":
                result = root(a)#корень
            elif operation == "%":
                result = per(a, b)#процент
            elif operation == "NOD":
                result = NOD(a, b)#НОД
            elif operation == "sin":
                result = sin(a)#синус
            elif operation == "cos":
                result = cos(a)#косинус
            else:
                raise ValueError("Несуществующая операция.") #обработка ошибки
            display_result(result)
        except Exception as e:
            display_error(str(e))

# Запуск программы
if __name__ == "__main__":
    main()