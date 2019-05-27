import os
CHATFILEPATH = os.path.abspath("C:\\Users\yodeb\Desktop\haptik-assignments\data\chats.txt")
REGEX = ""


import itertools

a = list(itertools.combinations_with_replacement("abcd", 2))
print(a)