from py2026_05_23.calculator.calc import Calculator
from py2026_05_23.calculator.exceptions import UnknownOperationException

def user_input():
    first_value = input("Введите первое число:")
    second_value = input("Введите второе число:")
    operation = input("Выберите операцию (+, -, *, /):")
    return first_value, second_value, operation

##ПРОВЕРКА НА ОШИБКИ

def validation(first_value, second_value, operation):  ##Тут типа проверка на ошибки??? Или я не понял...
    if operation not in ["+", "-", "*", "/"]:
        return False, UnknownOperationException("Ошибка: Неизвестная операция. Используйте +, -, *, /.")
    elif second_value == 0:
        return False, ZeroDivisionError("Ошибка: На ноль делить нельзя!")

    try:
        first_value = float(first_value)
        second_value = float(second_value)
    except ValueError as e:
        return False, ValueError("Ошибка: Введите число, а не текст.")
    #
    # return (first_value, second_value, operation)
    return True, None

##КАЛЬКУЛЯТОР

def use_calc():
    call_for_gods = validation()
    first_value = call_for_gods[0]
    second_value =  call_for_gods[1]
    operation =  call_for_gods[2]

    calculator_values = Calculator(variable_first = first_value, variable_second = second_value, math_operation = operation)
    operation_result = 0
    if operation == '+':
      operation_result = calculator_values.addition()
    elif operation == '-':
      operation_result = calculator_values.subtraction()
    elif operation == '/':
      operation_result = calculator_values.division()
    elif operation == '*':
      operation_result = calculator_values.multiplication()
    return operation_result


if __name__ == '__main__': ## Шо ито значит? Моя не понимать...
    print("Hello, user")
    first_value, second_value, operation = user_input()
    is_success, error = validation(first_value, second_value, operation)
    if not is_success:
        print("ошибка////")
    result = use_calc()
    print(f"Your answer is {use_calc()}")
