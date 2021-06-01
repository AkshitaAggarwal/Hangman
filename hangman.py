import random
words = ['rainbow','computer','friends','galaxy','stars','miniatures','gypsophila','stocks','billionaire','unicorn','hangman']

def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     /
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |
                   |
                   |
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |
                   |
                   |
                   |
                   -
                """
    ]
    return stages[tries]

def get_word():
    return random.choice(words)

def play(word):
    guessed = False
    guessedLetters = []
    wordCompletion = '*'*len(word)
    tries = 6
    name = input('Please enter your name ')
    print('Hey! ' + name +", Let's play hangman")

    while not guessed and tries > 0:
        print(display_hangman(tries))
        print('\n')
        print(wordCompletion)
        guess = input('Enter the guess: ').lower()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessedLetters:
                print('you already guessed the letter ' + guess)
            elif guess not in word:
                print(guess, 'is not in word')
                guessedLetters.append(guess)
                tries-=1
                print('you have {0} tries left'.format(tries))
            else:
                print('Bravo! ' +guess+ ' is in the word')
                guessedLetters.append(guess)
                word_as_list = list(wordCompletion)
                indices = []
                for i,letter in enumerate(word):
                    if guess == letter:
                        indices.append(i)
                for index in indices:
                    word_as_list[index] = guess
                wordCompletion = ''.join(word_as_list)
                if '*' not in wordCompletion:
                    guessed = True
        else:
            if guess == word:
                guessed = True
            else:
                print('Not a valid guess')
                tries-=1
                print('you have {0} tries left'.format(tries))

    if guessed:
        print("Congrats, you guessed the word! '" + word + "' You win!")
    else:
        print("Sorry, you ran out of tries. The word was " + word + ". Maybe next time!")

word = get_word()
play(word)
while input("Play Again? (Y/N) ").upper() == "Y":
        word = get_word()
        play(word)
