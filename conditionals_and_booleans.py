if True:
    print('Is true')

if False:
    print('Is false')

lang = 'Python'

if lang == 'Python':
    print('Is true')

# ==
# =!
# >
# <
# >=
# <=
# is

if lang == 'Python':
    print('Is true')
else:
    print('Is false')

#no switch case, use this
if lang == 'Python':
    print('Is true')
elif lang == 'Java':
    print('Is Java')
elif lang == 'C#':
    print('Is C#')
else:
    print('Is false')

user = 'Admin'
logged_in = True

if user == 'Admin' and logged_in:
    print('Admin page')
else:
    print('Bad creds')

if user == 'Admin' or logged_in:
    print('Admin page')
else:
    print('Bad creds')

if not logged_in:
    print('Not logged in')
else:
    print('Welcome')

# the same object in memory
a = [1,2,3]
b = [1,2,3]

print(a == b) # true
print(a is b) # false
print(id(a)) # shows id in memory
print(id(b))

# evals to false
    # False
    # None
    # Zero of any numeric type
    # Empty sequence
    # Empty mapping
    # Empty string 




