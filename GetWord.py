import random

def Get_Random_Word():
    lines = open("./words_list.txt")
    word = lines.read().split()

    random_word = random.choice(word)
    return random_word