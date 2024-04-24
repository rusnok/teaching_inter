from functools import reduce
a = [list(range(3)),['a', 'b'],list(range(3))]
print(a)

b = reduce(lambda x, y: x+y, a)
print(b)

c = list(map(lambda x: x[-1], a))
print(c)

a = [list(range(3)),[10, 20],list(range(3))]
print(a)
a2 = reduce(lambda x, y: x+y, a)
print(a2)
a3 = reduce(lambda x, y: x+y, a2)
print(a3)

a = [list(range(3)),[10, 20],list(range(3))]
print(a)
print(sum(list(map(lambda x: sum(x), a))))
