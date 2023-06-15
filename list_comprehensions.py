nums = [1,2,3,4,5,6,7,8,9,10]

# List Comprehensions vs Lists

my_list = []
for n in nums:
    my_list.append(n)
print(my_list)

my_list_comprehension = [n for n in nums]
print(my_list)

my_list = []
for n in nums:
    my_list.append(n*n)
print(my_list)

my_list_comprehension = [n*n for n in nums]
print(my_list)

my_list_comprehension = map(lambda n: n*n, nums)
print(my_list)

my_list = []
for n in nums:
    if n%2 == 0:
        my_list.append(n)
print(my_list)

my_list_comprehension = [n for n in nums if n%2 == 0]
print(my_list)

my_list_comprehension = filter(lambda n: n%2 == 0, nums)
print(my_list)

my_list = []
for letter in 'abcd':
    for num in range(4):
        my_list.append((letter, num))
print(my_list)

my_list_comprehension = [(letter, num) for letter in 'abcd' for num in range(4)]

# Dictionary Comprehensions
names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']

my_dict = {}
for name, hero in zip(names, heros):
    my_dict[name] =  hero
print(my_dict)

my_dict = {name: hero for name, hero in zip(names, heros) if name != 'Peter'}

# Set Comprehensions
nums = [1,1,2,1,3,4,3,4,2]

my_set = set()
for n in nums:
    my_set.add(n)
print(my_set)

my_set = {n for n in nums}

