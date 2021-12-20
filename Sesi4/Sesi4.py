#f = open("test.txt") # open file in current directory
#f = open("C:/Hacktiv8/README.txt") # specifying full path

f = open("test.txt", encoding = 'utf-8')
# perform file operations
print(f.read())

with open("test.txt", 'w', encoding = 'utf-8') as f:
    f.write("my first file\n")
    f.write("This file\n\n")
    f.write("contains three lines\n")

f.close()

try:
    with open('file.log') as file:
        read_data = file.read()
except:
    print('Could not open file.log')

try:
    with open('file.log') as file:
        read_data = file.read()
except FileNotFoundError as error:
    print(error)
else:
    print('Executing the else clause.')


try:
    with open('file.log') as file:
        read_data = file.read()
except FileNotFoundError as error:
    print(error)
else:
    try:
        with open('file.log') as file:
            read_data = file.read()
    except FileNotFoundError as fnf_error:
        print(fnf_error)
finally:
    print('Cleaning up, irrespective of any exceptions.')
