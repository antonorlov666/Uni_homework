# Model

import math

def summ(a, b): #функция сложения
    return a + b

def sub(a, b): #функция вычитания
    return a - b

def mult(a, b): #функция умножения
    return a * b

def div(a, b): #функция деления
    if b == 0: #проверка на дурака
        raise ValueError("Please, buy this: https://prosv.ru/product/matematika-3-klass-uchebnik-v-2-ch-chast-2601/?utm_source=google.com&utm_medium=organic&utm_campaign=google.com&utm_referrer=google.com")
    return a // b

def deg(a, b): #функция степени
    return a ** b

def root(a): #функция квадратного корня
    return math.sqrt(a)

def sin(a): #функция синуса
    return math.sin(a)

def cos(a): #функция косинуса
    return math.cos(a)

def per(a, b): #функция процента
    return a//100*b

def NOD(a, b): #функция НОД
    return math.gcd(a, b)



