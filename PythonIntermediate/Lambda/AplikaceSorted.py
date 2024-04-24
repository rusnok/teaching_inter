pairs = [(1, 10), (2, 9), (3, 8)]
pairs_sorted = sorted(pairs, key=lambda x: x[1])

print(pairs_sorted)

a = min(pairs)  # (1, 10)
a = min(pairs, key=lambda x: x[1] )
a = max(pairs)
a = max(pairs, key=lambda x: x[1])  # (1, 10)
a = max(pairs, key=lambda x: x[0] * x[1])
print(a)

print(sorted([0, 3, 6, 4, 1], reverse = True))
print(sorted([0, 3, 6, 4, 1]))
