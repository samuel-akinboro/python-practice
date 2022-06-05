# you can remove an item by using the remove()
# Note: if the item to remove does not exist, it will raise an error

setList = {"orange", "apple", "banana", "strawberry"}
setList.remove("orange")
print(setList)

# you can also make use of the discard() method
# Note: it doesn't throw an error when the item doesn't exist
setList.discard("apple")
print(setList)

# pop also removes the last item
setList.pop()
print(setList)

# the clear() method empties the set
setList.clear()
print(setList)

# del is used to delete the set
del setList
# print(setList)
