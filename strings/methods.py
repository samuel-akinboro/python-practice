text = "hello world"

# capitalize()	Converts the first character to upper case
print(text.capitalize())

# casefold()	Converts string into lower case
sample = "HeLLO woRLD"
print(sample.casefold())

# count()	Returns the number of times a specified value occurs in a string
print(text.count("l"))

# endswith()	Returns true if the string ends with the specified value
sample2 = "test.js"
print(sample2.endswith(".js"))

# find()	Searches the string for a specified value and returns the position of where it was found
# If the value is not found, the find() method returns -1, but the index() method will raise an exception
print(text.find("l"))

# join()	Joins the elements of an iterable to the end of the string
myTuple = ["John", "Peter", "Vicky"]
x = ",".join(myTuple)
print(x)