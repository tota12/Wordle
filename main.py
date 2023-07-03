import random
with open('words.txt') as f:
    words = [line.strip() for line in f.readlines()]

word = random.choice(words)

# print("debug: the word is ", word)

# count the right letters
def right_letters(word, guess):
    right_letters = []
    for x in guess:
        if x in word and x not in right_letters:
            right_letters.append(x)
    return right_letters


# count the right letters in the right position
def right_position(word, guess):
    right_position = []
    for i in range(len(word)):
        if word[i] == guess[i]:
            newLetter = (guess[i], i)
            right_position.append(newLetter)
    return right_position


#guess the word
tries = 0;
print("Welcome to the game of Wordle!")
while tries <6:
    guess = input("Guess the 5-letter word: ")
    if (guess.isalpha() and len(guess) == 5):
        guess = guess.lower()
        if guess in words:
            if guess == word:
                print("You got the right word!")
                tries = 6
            else:
                tries = tries+1
                if tries == 6:
                    print("You lost! The word was ", word)
                else:
                    print(f"wrong word, you have {6-tries} tries left")
                    print("You got these letters right ",right_letters(word, guess))
                    print("You got these letters in the right position ",right_position(word, guess))
        else:
            print("This word is not in the dictionary")
    else:
        print("You entered a non-alphabetic character or a word with length other than 5")
