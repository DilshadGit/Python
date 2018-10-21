import os
import sys

print(' To find the operating system of current machine sys.platrom:')
print('Your operatingsys is: ', sys.platform)
print(os.name)

print('\n', 'A list of strings that specifies the search path for modules.')
print(sys.path)

print('\n', 'A list of callables that take a path argument to try to create \
		a finder for the path')
print(sys.path_hooks)

print('\n', 'A dictionary acting as a cache for finder objects.')
print(sys.path_importer_cache)

print('\n', 'A string giving the site-specific directory prefix where \
		the platform independent Python files are installed')
print(sys.prefix)