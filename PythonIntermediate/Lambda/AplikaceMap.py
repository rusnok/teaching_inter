items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, items))
print(squared)

print([x**2 for x in items])

squared = map(lambda x: x ** 2, items)
print(squared)

# nutne pretypovani z map objectu
squared = list(map(lambda x: x ** 2, items))
print(squared)