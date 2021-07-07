import random


with open('sowpods.txt','r') as texts:
    twxt=texts.readlines()
    word=random.choice(twxt)

print(word.strip())

