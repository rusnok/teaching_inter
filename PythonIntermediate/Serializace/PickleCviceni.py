import pickle
a = [1, 3, 4, 'asdf']

file_ukazatel = open("data_binarni", 'wb')
pickle.dump(a, file_ukazatel)
file_ukazatel.close()

file_ukazatel = open("data_textove", 'a')
file_ukazatel.writelines("asdf")
file_ukazatel.writelines("dalsi radky")

file_ukazatel.close()