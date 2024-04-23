import pickle

data = {
    'a': [1, 2.0, 3, 4 + 6j],
    'b': ("Alice has a cat", "Python programming is great"),
    'c': [False, True, False]
}

#with open('data.pickle', 'wb') as f:
#    pickle.dump(data, f)

f = open('data.pickle', 'wb')
pickle.dump(data, f)
f.close()


del data
try:
    print(data['a'])
except NameError:
    print("data uz neexistuji")


with open('data.pickle', 'rb') as f:
    print(pickle.load(f))

#print(data['a'])