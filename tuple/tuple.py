# items cannot be added or removed when a tuple has been created
# when you only have one item in a tuple, you must include a comma after the item, otherwuse, 
# it won't be recognised as a tuple

tupleList = ("cake",)
testTuple = ("cake")
print(type(tupleList)) #returns tuple
print(type(testTuple)) # str