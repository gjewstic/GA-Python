# To Read A file
'''
my_file = open('data/hello.txt')
print(my_file.read())
my_file.close()
'''
# To Write A File (if file doesn't exist, it'll create it.  if it does, w will overwrite)
my_file = open('data/hello.txt', 'w')
my_file.write('Writing a new line of text to my text file')

my_file.close()


# Appending a file.  Use '\n' to start the appended text to a new line
my_file = open('data/hello.txt', 'a')
my_file.write('\nWriting a new line of text to my text file (append)')

my_file.close()


# the With keyword

with open('data/hello.txt', 'a') as file_object:
    file_object.write('\nWriting a new line of code with the WITH keyword')
