import os
#print(os.listdir())
filename = "sample1.txt"
def create_file():
    with open(filename,"w") as file:
        file.write("This is a sample file")
def read_file():
    with open(filename,"r") as file:
        f = file.read()
        f = f.split()
        print('\n'.join(f))
read_file()
