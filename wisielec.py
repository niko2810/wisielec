print("********** GRA W WISIELCA **********")

import random
import time

def hangman(word):
    wrong = 0
    stages = ["",
              "_______     ",
              "|     |     ",
              "|     O     ",
              "|    /|\    ",
              "|    / \    ",
              "|           ",
              "|___________"]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    while wrong < len(stages)-1:
        print("\n")
        msg = "Odgadnij literę: "
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = "$"
        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("WYGRAŁEŚ !!!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong]))
        print("Przegrałeś! Miałeś odgadnąć: {}.".format(word))

wordlist = ["truskawka", "ołówek", "długopis", "kot", "gumka", "lampa",
            "kalendarz", "słownik", "laptop"]
randwordindex = random.randint(0,len(wordlist)-1)

hangman(wordlist[randwordindex])

time.sleep(10)
