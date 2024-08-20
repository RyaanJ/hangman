import random

animals = ['dog', 'cat', 'elephant', 'giraffe', 'lion', 'tiger', 'bear', 'wolf', 'fox', 'rabbit', 'deer', 'zebra', 'monkey', 'kangaroo', 'panda', 'koala']
fruits = ['apple', 'banana', 'orange', 'grape', 'strawberry', 'blueberry', 'watermelon', 'kiwi', 'peach', 'pear', 'mango', 'pineapple', 'cherry', 'plum', 'lemon']
countries = ['usa', 'canada', 'mexico', 'brazil', 'argentina', 'chile', 'peru', 'england', 'france', 'germany', 'italy', 'spain', 'russia', 'china', 'japan']


category = int(input("Select a category by entering a number from 1-3 from the following options: animals (1), fruits (2), countries (3): "))
word = None
listword = None
unknown_word = []
lives = None
previous_guesses = []
hangman = r'''
           -----
           |   |
           O   |
          /|\  |
          / \  |
               |'''

if category == 1:
    print("You chose animals!")
    word = random.choice(animals)
elif category == 2:
    print("You chose fruits!")
    word = random.choice(fruits)
elif category == 3:
    print("You chose countries!")
    word = random.choice(countries)

for i in range(len(word)):
    unknown_word.append("_")

print(f"Starting off, your word is {len(unknown_word)} letters long and looks like this currently: {''.join(unknown_word)}")
listword = list(word)
lives = len(word) + 1
while "_" in unknown_word and lives > 0:
    guess = input("Take a guess and choose any letter! Or you can try guessing the word itself!: ")
    if guess in listword:
        for i in range(len(listword)):
            if guess in previous_guesses and listword.count(guess) == previous_guesses.count(guess):
                print("Try another letter!")
                break
            elif guess == listword[i]:
                unknown_word[i] = listword[i]
                print(f"Your word is {len(unknown_word)} letters long and looks like this currently: {''.join(unknown_word)}.")
                previous_guesses.append(guess)
                
            else:
                continue
    elif guess.lower() == word.lower():
        break
    elif guess not in listword:
        lives -= 1
        print(f"Not quite there, try again! Warning: You now have {lives} attempts remaining.")
    
    
          
        

if lives > 0:
    print(f"Congrats! You Figured out what the word is! The word is {word}")
else:
    print(f"Ran out of attempts, You lost. The word was {word}. Better luck next time..")
    print(hangman)





'''
print(word)
print(unknown_word)
print(listword)
'''