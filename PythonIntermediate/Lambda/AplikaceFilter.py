items = [1, 2, 3, 4, 5]
odds = list(filter(lambda x: x % 2 == 1, items))
print(odds)

items = [1, 2, 3, 4, 5]
odds = list(filter(lambda x: x % 2, items))
print(odds)

print([x for x in items if x % 2 == 1])

def pavel(x):
    return x % 2 == 1

pavel = lambda x: x % 2 == 1
odds = list(filter(pavel, items))
print(odds)