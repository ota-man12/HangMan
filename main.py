import random
import hangman_word_list
import hangman_art

# Display Hangman Title

print(hangman_art.logo)

chosen_word = random.choice(hangman_word_list.word_list)
word_length = len(chosen_word)
lives = 6

# Testing code uncomment
# print(chosen_word)

# Display underscores instead of chosen word
display = []
for _ in range(word_length):
    display += "_"
print(display)

# Looping through the list until we reach the end
end_of_game = False
while not end_of_game:
    # Guessed letter to be checked against the chosen word and be added to the correct place if correct letter is chosen
    # and displayed in the correct place
    guess = input('Guess a letter: ').lower()

    # Check if user is guessing an already guessed letter or blank
    if guess in display:
        print(f"You have already guessed {guess}")
    elif guess == "":
        print("Have have not ended a letter ")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    # Reducing lives for when the user choose incorrectly until reached 0 to end the game.
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print(f"You lose the correct word was {chosen_word}")

    if "_" not in display:
        end_of_game = True
        print("You WIN!!!!!")

    # Print the hangman according to the stages
    print(hangman_art.stages[lives])
