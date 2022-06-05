# To join to sets together, you can use the union() method which returns a new set of the merged sets
set1 = {"apple", "orange"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

# or use the update() method which inserts the items in set2 to set1
set1.update(set2)
print(set1)