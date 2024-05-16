import os
os.listdir()
def gen_file_names(directory):
    file_names = os.listdir(directory)
    for f in file_names:
        yield f

for s in gen_file_names("."):
    print(s)