thisDict = {
  "name": "Black~vibes",
  "title": "Frontend Engineer",
  "stack": ["html", "css", "javascript", "React", "React Native"]
}

# you can access an item in a dictionary by refering to its key name
print(thisDict["name"])

# you can also use the get() method
print(thisDict.get("title"))

# the keys() method will return a list of all the keys in the dictionary
print(thisDict.keys())

#  the values() method returns a list of all the values in the dictionary
print(thisDict.values())

# the items() method will return each items in the dictionary as a tuple in a list
print(thisDict.items())