import math
cc = 1
num = float
num1 = float
num2 = float

while(cc > 0):
    print("Выберите действие: ")
    print("1. Сложение ")
    print("2. Вычитание ")
    print("3. Умножение ")
    print("4. Деление ")
    print("5. Возведение в степень")
    print("6. Квадратный корень")
    print("7. Факториал")
    print("8. Синус")
    print("9. Косинус")
    print("10. Тангенс")
    print("11. Выход")
    print(" ")
    oper = int(input())

    if  (oper == 1):
        print(" ")
        print("Введите первое число:")
        num1 = float(input())
        print("Введите второе число:")
        num2 = float(input())

        num = num1 + num2
        print( str(num1) + " + " + str(num2) + " = " +  str(num) )
        print(" ")
    
    elif (oper == 2):
        print(" ")
        print("Введите первое число:")
        num1 = float(input())
        print("Введите второе число:")
        num2 = float(input())

        num = num1 - num2
        print( str(num1) + " - " + str(num2) + " = " + str(num) )
        print(" ")
    
    elif (oper == 3):
        print(" ")
        print("Введите первое число:")
        num1 = float(input())
        print("Введите второе число:")
        num2 = float(input())

        num = num1 * num2
        print(str(num1) + " * " + str(num2) +  " = " + str(num))
        print(" ")

    elif (oper == 4):
        print(" ")
        print("Введите первое число:")
        num1 = float(input())
        print("Введите второе число:")
        num2 = float(input())

        if (num2 == 0):
            print("Деление на 0 невозможно")
        else:
            num = num1 / num2
            print(str(num1) + " / " + str(num2) + " = " + str(num))
        print(" ")

    elif (oper == 5):
        print(" ")
        print("Введите первое число:")
        num1 = float(input())
        print("Введите степень:")
        num2 = float(input())

        num = num1 ** num2
        print("Число " + str(num1) + " в степени "+ str(num2) + " равно " + str(num))
        print(" ")
    
    elif (oper == 6):
        print(" ")
        print("Введтие число:")
        num = float(input())

        print("Квадратный кроень числа " + str(num) + " равен: ")
        print(math.sqrt(num))
        print(" ")

    elif (oper == 7):
        print(" ")
        print("Введите число: ")
        num1 = float(input())
        num2 = num1

        factorial = 1
        while num1 > 1:
            factorial *= num1
            num1 -= 1
        
        print("Факторил числа " + str(num2) + " равен: ")
        print(factorial)
        print(" ")

    elif (oper == 8):
        print(" ")
        print("Введите  угол в радианах: ")
        num = float(input())
        
        print("Синус равен: ")
        print(math.sin(num))
        print(" ")

    elif (oper == 9):
        print(" ")
        print("Введите  угол в радианах: ")
        num = float(input())
        
        print("Косинус равен: ")
        print(math.cos(num))
        print(" ")

    elif (oper == 10):
        print(" ")
        print("Введите  угол в радианах: ")
        num = float(input())
        
        print("Тангенс равен: ")
        print(math.tan(num))
        print(" ")


    elif (oper == 11):
        print(" ")
        print("бб")
        break

    else:
        print(" ")
        print("Неверная операция. ")
        print(" ")
