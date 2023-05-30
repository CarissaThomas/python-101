def hello_func():
    return 'Hello Function.'

print(hello_func())

def hello_func_with_param(greeting):
    return '{} Function.'.format(greeting)

hello_func_with_param('Hi').upper()

def hello_func_with_default(greeting, name = 'You'):
    return '{}, {}.'.format(greeting)

hello_func_with_param('Hi').upper()

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

student_info('Math', 'Art', name='John', age = 22)