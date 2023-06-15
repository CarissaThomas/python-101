def hello_func():
    return 'Hello Function.'

print(hello_func())

def hello_func_with_param(greeting):
    return '{} Function.'.format(greeting)

hello_func_with_param('Hi').upper()

def hello_func_with_default(greeting, name = 'You'):
    return '{}, {}.'.format(greeting)

hello_func_with_param('Hi').upper()

def student_info(*args, **kwargs): # args = tuple, kwarg = dictionary
    print(args)
    print(kwargs)

student_info('Math', 'Art', name='John', age = 22)

courses = ['Math', 'Art']
info = {'name': 'Jonn', 'age': 22}

student_info(*courses, **info)

month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31,30,31,30,31]

def is_leap(year):
    return  year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
    if not 1 <= month <= 12:
        return 'Invalid Month'

    if month == 2 and is_leap(year):
        return 20

    return month_days[month]

print(days_in_month(2020, 2))