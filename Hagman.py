import random
def hangman():
    words = ['snake', 'volcana', 'computer', 'banana','hangman','monkey','happy','sad','angry','hello','supercalifragilisticexpialidocious','pneumonoultramicroscopicsilicovolcanoconiosis','documents']

    worselected = random.choice(words)
    guessed_letters = ["_" * len(worselected)]

    max_attempts = 6
    attempts = 0
    guessed_letters=[]
    print("*"*50)
    print("Welcome to Super Simple Hangman Game!")
    print(" ".join(guessed_letters))
    while attempts < max_attempts:
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        guessed_letters.append(guess)
        if guess in worselected:
            print(f"Good guess! {guess} is in the word.")
        else:
            attempts += 1
            print(f"Sorry, {guess} is not in the word. Attempts left: {max_attempts - attempts}")
        display_word = [letter if letter in guessed_letters else "_" for letter in worselected]
        print(" ".join(display_word))
        if "_" not in display_word:
            print("Congratulations! You've guessed the word:", worselected)
            break

hangman()

