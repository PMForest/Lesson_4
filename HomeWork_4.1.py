"""1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами."""

def staff():

    try:
        time = int(input("enter the time: "))
        salary = int(input("enter the salary: "))
        bonus = int(input("enter the bonus: "))
        res = time * salary + bonus
        print(f'staff salaries {res}')
    except ValueError:
        print('Not a number')
staff()