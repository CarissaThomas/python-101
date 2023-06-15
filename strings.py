# Print welcome message
message = 'Hello World'
my_message = "Bobby's World"
my_message_with_double_quotes = 'Bobby"s World'
my_message_multiline = 'Bobby"s World was a good ' \
                       'cartoon in the 1990s'
greeting = 'Hello'
name = 'Michael'

length = len(message)
location = message[0]
first_word = message[0:5] # [:5] means the same thing
last_word = message[6:]

lower = message.lower()
upper = message.upper()
counter = message.count('Hello') # returns 1
index = message.find('World') # returns a 6
replacer = message.replace('World', 'Universe')
greeter = greeting + ', ' + name
greeter_complex = '{}, {}. Welcome!'.format(greeting, name)
greeter_f = f'{greeting}, {name.upper()}. Welcome!'
available_methods = dir(greeter_f)
string_helper = help(str)
string_lower = help(str.lower)

print(string_lower)

