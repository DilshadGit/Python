
class Book:

    def __init__(self, first_name, last_name, author, year):
        self.first_name = first_name
        self.last_name = last_name
        self.author = author
        self.year = year

    def full_name(self):
        return '{}.{}'.format(self.first_name, self.last_name)

    def email(self):
        return '{} {}@book.edu'.format(self.first_name, self.last_name)


obj_1 = Book('Claus', 'Timo', 'The Europe', 2014)
obj_2 = Book('Alan', 'Alex', 'Sun of Sand', 2001)

print(obj_1.first_name)
print(obj_1.email())
print(obj_1.full_name())

print('\nOverwrite the first name see what is change')
print('\n###########################################')
obj_1.first_name = 'Dilshad'

print(obj_1.first_name)
print(obj_1.email())
print(obj_1.full_name())
