# thisList = ["orange", "grape", "pear"]
# for fruit in thisList :
#   print(fruit)

# Loop Through the Index Numbers
fruits = ["pear", "berry"]
for i in range(len(fruits)) :
  print(i)

# while loop
fruits = ["pear", "berry"]
i=0
while i < len(fruits):
  print(fruits[i])
  i += 1

# List comprehension

# filtering
fruits = ["pine", "eggplant" "banana"]
newList = [x for x in fruits if x != "apple"]
print(newList)