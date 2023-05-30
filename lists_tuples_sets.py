# Lists
empty_list = []
empty_list = ()
courses = ['History', 'Math', 'Physics', 'CompSci']
courses_2 = ['Art', 'PE']
nums = [1, 5, 2, 4, 3]

length = len(courses)
indexer = courses[0]
last_item = courses[-1] # last item in list

courses.append('art') # add to list

courses.insert(0, 'art')
courses.insert(0, courses_2) # list inside a list

courses.extend(courses_2) # add multiple values to list

courses.remove('Math')
courses.pop() # removes last item in list and returns the value

courses.reverse()
courses.sort() # automtically sorts alphabetically or numerically
courses.sort(reverse=True)
sorted(courses) # returns a sorted version of the list

minimum = min(nums)
maxx = max(nums)
summ = sum(nums)

courses.index('CompSci')
isInList = 'Math' in courses

for item in courses:
    print(item)

for index, item in enumerate(courses):
    print(index, item)

for index, item in enumerate(courses, start=1):
    print(index, item)

course_str = ', '.join(courses)
split_list = courses.str.split(' - ')

# Tuples (Cant be modified)
empty_tuple = ()
empty_tuple = tuple()
tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
tuple_2 = tuple_1

tuple_1[0] = 'Art' # will get error, cant be changed

#Sets (unordered with no duplicates)
empty_set = set()

a_set = {'History', 'Math', 'Physics', 'CompSci', 'Math'}
isInSet = 'Math' in a_set

a_set_with_art = {'History', 'Math', 'Art', 'CompSci'}

a_set.intersection(a_set_with_art)
a_set.difference(a_set_with_art)
a_set.union(a_set_with_art)







