import random

word_bank = ['rizz', 'ohio', 'jazz', 'buzz', 'tiktok', 'python']

word = random.choice(word_bank).lower()
print(word)
print("Let's play a word guessing game!")

guessed_word = ['_'] * len(word)
attempts = 10
guessed_letters = set()

while attempts > 0:
    print('\nCurrent word: ' + ' '.join(guessed_word))
    print(f'Attempts remaining: {attempts}')
    
    guess = input('Guess a letter: ').lower()
    
    if not guess.isalpha() or len(guess) != 1:
        print("Invalid input. Please enter a single alphabetic character.")
        continue
    
    if guess in guessed_letters:
        print(f"You've already guessed '{guess}'. Try another letter.")
        continue
    
    guessed_letters.add(guess)
    
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
        print('Great guess!')
    else:
        attempts -= 1
        print('Wrong guess!')
    
    if '_' not in guessed_word:
        print('\nCongratulations! You guessed the word:', word)
        break
else:
    print("\nYou've run out of attempts! The word was:", word)
