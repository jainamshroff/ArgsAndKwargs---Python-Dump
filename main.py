# args and kwargs

def function_name_print(a, b, c, d):
    print(a, b, c, d)


function_name_print("Jainam", "Nimish", "Sheetal", "Mayana")

# What is a new name has to be entered at once, we have to change function which is
# not a good practice when considering large amount of data

def function_args(normal, *args):
    for item in args:
        print(item)
    print("Normal Argument: ", normal)

list = ["Jainam", "Shroff", "Sheetal", "Nimish", "Vishwesh"]
function_args("Magan", *list)

# we send the list as whole as the argument thus while adding something in list
# we won't have to modify the function itself
# the function will be of the form tuple by default
# we can write args as anything, basically the theme is that we can send the list itself
# We can also pass normal argument along with pointer arguments

# Now what is kwargs?

# when we try to pass normal argument after args than it throws an error
# Always keep normal argument before args
# pattern will be normal, *args, **kwargs

# **kwargs are used to send dictionary along with list along with some normal argument
# thus we can handle lists and dictionaries as whole and access it inside the function
