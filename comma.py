# write a function that takes a list value as an argument
# it should return a string seperated by a comma and 'and' inserted before the last item
# it should work with any list value passed to it
# the program ends when an empty list is passed

def getListValue(list_value):
    # Returns a string containing the elements of a list, separated by comma

    string = ''
    for i in range(len(list_value) - 1):
        string = string + list_value[i] + ', '

        # Add the element_to_add before last value
    string = string + 'and ' + list_value[-1]

    return string


list1 = ['apple', 'banana', 'kiwi', 'mango']
string = getListValue(list1)
print(string)
