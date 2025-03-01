import string
loltxt="C:\\destination\\Rauan_Tuken_PP2\\lab6\\lol.txt"
with open(loltxt) as lol:
    data=lol.read()
print(len(list(data.split("\n"))))