# Create a function that takes a filename and a string as parameter,
# it should write the string to the file 3 times
# example: when called with "tree.txt" and "apple",
# it should write "appleappleapple" to the file "tree.txt".
# the function should not raise an error on any output problem, for example
# denied permission
file_name = 'second.txt'
string = 'apple'

def write_string_3times_to_file(file_name, string):
    try:
        file = open(file_name, 'w')
        file.write(string * 3)
        file.close()
    except:
        pass

write_string_3times_to_file(file_name, string)
