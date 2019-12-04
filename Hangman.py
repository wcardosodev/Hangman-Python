import GetWord

def Welcome():
    print("Please enter your name")
    name = input()
    print("Welcome to Hangman %s!\nPlease select your difficulty from the following options" % (name))
    print("Enter 1 for Easy, 2 for Medium and 3 for Hard")

    return input("")

def Select_Difficulty(difficulty):
    if (difficulty == str(1)):
        return "Easy"
    elif (difficulty == str(2)):
        return "Medium"
    elif (difficulty == str(3)):
        return "Hard"
    else:
        return False


def Max_Guesses(difficulty):
    if (difficulty == "Easy"):
        return 10
    elif (difficulty == "Medium"):
        return 6
    elif (difficulty == "Hard"):
        return 3

difficulty_input = Welcome()
while Select_Difficulty(difficulty_input) == False:
    print("Please enter a number between 1 and 3 to select your difficulty")
    difficulty_input = input("")
else:
    difficulty = difficulty_input
    print("You have chosen: %s" % (Select_Difficulty(difficulty_input)))

max_guesses = Max_Guesses(Select_Difficulty(difficulty_input))
print("Due to your difficulty you get %s guesses before you lose." % max_guesses)

got_word = False
while got_word == False:
    random_word = GetWord.Get_Random_Word()
    if difficulty_input == "1" and (len(random_word) <= 5):
        got_word = True
    elif difficulty_input == "2" and (len(random_word) <= 7 and len(random_word) > 4):
        got_word = True
    elif difficulty_input == "3" and (len(random_word) <= 10 and len(random_word) > 5):
        got_word = True


shown_word = "*" * len(random_word)
guesses_left = max_guesses
new_list = []
print("Your word is: %s" % (shown_word))

while guesses_left > 0:
    letter_list = []
    new_list = list(shown_word)

    print("Enter your guess")
    guess = input().lower()
    if random_word.find(guess) != -1:
        for i, value in enumerate(random_word):
            if value == guess:
                ##get the index of i add it to a list
                letter_list.append(i)

        i = 0
        while i < len(shown_word):
            if i in letter_list:
                new_list[i] = guess
            else:
                if new_list[i] == "*":
                    new_list[i] = "*"
            i += 1
        shown_word = "".join(new_list)
        print("%s is in the word" % guess)
        print("Your new word is: %s" % (shown_word))

        if shown_word == random_word:
            print("Congratulations, you guessed the word: %s" % (random_word))
            break
    else:
        guesses_left -= 1
        print("You guessed incorrectly. You have %s guesses left" % (guesses_left))
else:
    print("You lose, the word was %s" % (random_word))