import random,time

print("Welcome to the word jumble!")

words = ["python", "java", "javascript", "html", "css","data","science", "machine", "learning", "artificial", "intelligence"]

def jumble_word():
    word=random.choice(words)
    wordToList=list(word)
    random.shuffle(wordToList)
    return "".join(wordToList),word
x = jumble_word()
print("The jumbled word is: ", x)

score = 0
rounds = 5
for i in range(1, rounds + 1):
    jumbled_word , word = jumble_word()
    print(f"Round {i}:")
    print("The jumbled word is: ", jumbled_word)
    hint = input("Do you want a hint? (yes/no): ").lower()
    if hint == "yes":
        print(f"first letter of the word is: {word[0].upper()}")
    guess = input("Your guess: ").lower()
    if guess == word:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! The correct word was: {word}")
print(f"Your final score is: {score}/{rounds}")
time.sleep(10)

