# Create a function that takes a list as a parameter,
# and returns a new list with every second element from the orignal list
# It should raise an error if the parameter is not a list
# example: [1, 2, 3, 4, 5] should produce [2, 4]

raw_list = [1, 2, 3, 4, 5]

def copy_every_second_element_from_list(raw_list):
    if type(raw_list) != list:
        raise ValueError('Excepted a list')
    even_indexed_items = []
    even_indexed_items = raw_list[1::2]
    return even_indexed_items

print(copy_every_second_element_from_list(raw_list))
