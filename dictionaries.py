# dictionaries, can hold many different kinds of data types

student = {'name': 'John', 'age': '25', 'courses': ['Math', 'CompSci'], 1: 'number'}
value = student['name']

null_key = student.get('pickle')
valid_key = student.get('name')
default_key = student.get('name', 'Not Found')

student['phone'] = '555-5555' # adds the property if it doesnt exist
student['name'] = 'Jane'
student.update({'name': 'Jane', 'age': 26, 'phone': '666-6666'})

del student['age']
age = student.pop('age')

length = len(student)

keyss = student.keys()
valuess = student.values()
itemss = student.items()

for key, value in student.items():
    print(key, value)


