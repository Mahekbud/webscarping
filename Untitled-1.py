a = (1, 2, 3, {'a': 4, 'b': 5}, 6)

# Slice to get elements 2, 3, and 6
list_output = list(a[1:3]) + list(a[3].values()) + [a[4]]

print(list_output)
