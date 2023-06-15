my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# list[start:end:step]

my_list[0]
my_list[-10]

my_list[0:6] # 0-5
my_list[-7:-2]
my_list[1:-2] # 1-7
my_list[1:] # 1 - end
my_list[:-1] # 0 - 8
my_list[:] # whole list

# step
my_list[2:-1:2] # 2, 4, 6, 8
my_list[-1:2:-1] # 9, 8, 7, 6, 5, 4, 3
my_list[:-1] # entire list in reverse

# slicing strings
# the same syntax as lists is used for strings
sample_url = 'http://test.com'


# Reverse the Url
sample_url[::1]


