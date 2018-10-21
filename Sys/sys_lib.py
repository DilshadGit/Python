import sys

# print(dir(sys))

# create empty list
empty_list = []

for index, name in enumerate(dir(sys)):
	print(index, ' - ', name)
	# adding all names to the emtpy list
	empty_list.append(name)

print(empty_list)

