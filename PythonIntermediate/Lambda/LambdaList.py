def prvni_a_delka(x):
    return (x[0], len(x))

print(prvni_a_delka(['a', 3, 4, 6, 3]))

prvni_a_delka = lambda x: (x[0], len(x))
print(prvni_a_delka(['a', 3, 4, 6, 3]))

