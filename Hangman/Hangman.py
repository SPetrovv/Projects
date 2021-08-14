import random # in case we use a list with words

#with open('wordlist.txt', 'r') as f:
#   words = f.readlines( )
#word = random.choice(words)[:-1]


word = 'Secret'

allowed_errors = 7
guesses = []
done = False

while not done:
    for letter in word:
        if letter.lower() in guesses:
            print(letter, end=' ')
        else:
            print('_', end=' ')
    print("")

    guess = input(f"Allowed  Errors Left {allowed_errors}, Next guess: ")
    guesses.append(guess.lower())

    if guess.lower() not in word:
        allowed_errors -= 1
        if allowed_errors == 0:
            break

    done = True
    for letter in word:
        if letter.lower() not in guesses:
            done = False
if done:
    print(f"You found the word! It was {word}!")
else:
    print(f"Game over , the word was {word}")