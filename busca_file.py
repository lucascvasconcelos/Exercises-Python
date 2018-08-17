import os

path = "."
dirs = os.walk(path)
print(dirs)

word = input("Informe o nome do arquivo que deseja buscar: ")

def searchFile (word):
    """A função consiste em buscar arquivos 
    a partir de uma palavra passada"""
    for _,_, file in dirs:
        for f in file:
            if word in f:
                print(type(f))
                print (f)

searchFile(word)  