import random
import hangman_words
import hangman_art
word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
#Testing code
print(hangman_art.logo)
print(f'Pssst, the solution is {chosen_word}.')  
#TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
display = []
lives = 6
disp =0
int = len(chosen_word)
word_length = len(chosen_word)
for _ in range(word_length):
    display += "_"
end_game = False
while not end_game :
    guess = input("Guess a letter: ").lower()
#TODO-2: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
    for position in range(word_length):
        letter = chosen_word[position]
    #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
            lives -= 1
            if lives == 0:
                end_game = True
                print("You Lose")
    if '_' not in display:
        end_game = True
        print("You win")
#TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.
    print(hangman_art.stages[lives])