thisDict = {
  "name": "Black~vibes",
  "title": "Frontend Engineer",
  "stack": ["html", "css", "javascript", "React", "React Native"],
  "age": None,
  "adviser": "my self",
  "disability": None
}

# the pop() method remove the item with the specified key
thisDict.pop("age")
print(thisDict)

# the popitem() method removes the last inserted item, (in versions before 3.7, a random item is removed instead)
thisDict.popitem()
print(thisDict)

# you can use the del keyword to delete an item with the specified key
del thisDict["adviser"]
print(thisDict)

# use the clear() method to remove all the items in the dictionary
thisDict.clear()
print(thisDict)