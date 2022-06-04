# you can't edit a tuple
# but you can convert the tuple tp a list, edit it and change it back to a tuple

x = ("book", "ruler")
y = list(x)
y[0] = "math set"
x = tuple(y)

print(x)

# you can also add tuple to tuple
a = ("book",)
b = ("pencil",)
a += b
print(a)