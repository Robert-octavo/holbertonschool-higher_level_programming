#!/usr/bin/python3
def no_c(my_string):
    if len(my_string) < 0:
        return (None)
    new_string = ""
    for i in my_string:
        if i == 'c' or i == 'C':
            new_string = new_string + ""
        else:
            new_string = new_string + i
    return (new_string)
print(no_c("Best School"))
print(no_c("Chicago"))
print(no_c("C is fun!"))