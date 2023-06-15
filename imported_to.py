# from import_modules_standard_library import * (imports everything, not commonly used)
from import_modules_standard_library import find_index, test
import sys
import random
import math
import datetime
import calendar
import os

sys.path.append('/PathTo/MyModule') # Not recommended, best to add to the python environment variable

courses = ['History', 'Math', 'Physics', 'CompSci']

index = find_index(courses, 'Math')
print(index)

# you can always import modules from the same directory
# import from python environment path, add modules here using terminal
    # nano ~/.bash_profile
    # export PYTHONPATH="/PathTo/MyModule'"
# also possible for the path to be added using PyCharm: Run ---> Configuration ---> Edit environment variables

print(sys.path) # where python looks for modules on import

random_course = random.choice(courses)
print(random_course)

rads = math.radians(99)
print(rads)

today = datetime.datetime.today()
print(today)

print(calendar.isleap(2017))

print(os.getcwd())

print(os.__file__) # Gets file directory


