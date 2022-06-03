# changing a range of items
fruits = ["apple", "orange", "mango", "strawberry", "plantain"]
fruits[1:3] = ["banana", "guava"]
print(fruits)

# insert item without replacing any of the existing items
# it only accepts two arguments, the index and the value to be inputed in
utensils = ["cup", "spoon"]
utensils.insert(1, "fork")
print(utensils)

# append item
fruits2 = ["grape"]
fruits2.append("cherry")
print(fruits2)

# extend
fruits3 = ["pine", "cherry"]
extra = ("pear", "berry")
fruits3.extend(extra)
specie = {
  "name": "musa",
  "class": "sp"
}
fruits3.extend(specie)
print(fruits3)

# the remove() method removes the specified item
fruits4 = ["apple", "orange"]
fruits4.remove("apple")
print(fruits4)

# the pop() method removes the specified index
# without the index, it removes the last item
fruits5 = ["apple", "orange", "cherry"]
fruits5.pop(2)
fruits5.pop()
print(fruits5)

# del can be used to delete a list completely
fruits6 = ["berry", "cherry", "eggplant"]
del fruits6
  # print(fruits6)

# the clear() method empties a list
fruits7 = ["grape"]
fruits7.clear()
print(fruits7)