# you can extract values into variables, this is called unpacking
# the number of variables must match the number of values in the tuple
# if not, you must use and asterisk to collect the remaining variables

fruits = ("apple", "strawberry", "cherry")
(green, *red) = fruits
print(green)
print(red)