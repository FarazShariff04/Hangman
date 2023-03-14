import random
def hangman():
    word = random.choice(["car" , "laptop" , "tiger" , "superman" , "thor" , "pokemon" , "avengers" , "savewater" , "earth" , "annable" ])
    validletters = 'abcdefghijklmnopqrstuvwxyz'
    turns = 10
    guessmade = ''

    while len(word) > 0:
        main = ""
        misseed = 0

        for letter in word:
            if letter in guessmade:
                main = main + letter
            else:
                main = main + "_" + " "

        if main == word:
            print("YOU WON!!")
            print(main)
            break

        print("Guess any letter " , main)
        guess = input()

        if guess in validletters:
            guessmade = guessmade + guess
        else:
            print("Please enter valid letter ")
            guess = input()

        if guessmade not in word:
            turns = turns -1
            if turns == 9:
                print("9 turns left")
                print("  --------  ")
            if turns == 8:
                print("8 turns left")
                print("  --------  ")
                print("     O      ")
            if turns == 7:
                print("7 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
            if turns == 6:
                print("6 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
                print("    /       ")
            if turns == 5:
                print("5 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
                print("    / \     ")
            if turns == 4:
                print("4 turns left")
                print("  --------  ")
                print("   \ O      ")
                print("     |      ")
                print("    / \     ")
            if turns == 3:
                print("3 turns left")
                print("  --------  ")
                print("   \ O /    ")
                print("     |      ")
                print("    / \     ")
            if turns == 2:
                print("2 turns left")
                print("  --------  ")
                print("   \ O /|   ")
                print("     |      ")
                print("    / \     ")
            if turns == 1:
                print("1 turns left")
                print("Last breaths counting, Take care!")
                print("  --------  ")
                print("   \ O_|/   ")
                print("     |      ")
                print("    / \     ")
            if turns == 0:
                print("You loose")
                print("You let a kind man die")
                print("  --------  ")
                print("     O_|    ")
                print("    /|\      ")
                print("    / \     ")
                break


name = input("Enter you're name: ")
print("DISCLAIMER")
print("This game is only for children between 3 and 12")
age = input("Enter you're age: ")
age = int(age)
if age < 3:
    print("you're under age")
    exit()
if age > 12:
    print("This game is made for children")
    exit()
print("Welcome" , name + " to hangman game ")
hangman()
print()
