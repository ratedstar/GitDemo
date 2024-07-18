import random
import hangman_words
import hangman_art

choosenword = random.choice(hangman_words.word_list)
print(hangman_art.logo)
print(choosenword)
guess = print("Guess a letter")
