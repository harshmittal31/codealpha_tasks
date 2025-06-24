import random

#list of words
word_list = ["apple", "tiger", "house", "plant", "smart"]

# Choose a random word from the list
secret_word = random.choice(word_list)

# Step 3: Create variables to keep track of the game
guessed_letters = []
tries_left = 6
display_word = ["_"] * len(secret_word)

print(" Welcome to Hangman!")
print("Guess the word: ", " ".join(display_word))

# Game loop
while tries_left > 0 and "_" in display_word:
    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("❌ Please enter a single alphabetic character.")
        continue

    if guess in guessed_letters:
        print("⚠️ You've already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("✅ Correct!")
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                display_word[i] = guess
    else:
        tries_left -= 1
        print("❌ Wrong! Tries left:", tries_left)

    print("Word: ", " ".join(display_word))

# Game result
if "_" not in display_word:
    print("🎉 Congratulations! You guessed the word:", secret_word)
else:
    print("💀 Game Over! The word was:", secret_word)
