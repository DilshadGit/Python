import sys

# print(dir(sys))
empty_list = []
create_file = open('lib_of_sys.txt', 'w')

for name in dir(sys):

	create_file.write(name + '\n')

create_file.close()

