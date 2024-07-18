import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
useroption = input("Select anything from 'rock','paper' or 'scissors'")
if useroption == 'rock':
    print(rock)
elif useroption == 'scissors':
    print(scissors)
else:
    print(paper)
gameopt = ['rock','paper','scissors']
comoption = random.choice(gameopt)
print(comoption)
if comoption =='rock':
    print(rock)
elif comoption=='paper':
    print(paper)
else:
    print(scissors)

if useroption == comoption:
    print("Its a tie")
elif useroption == 'rock' and comoption == 'scissors':
    print("You win")
elif useroption == 'scissors' and comoption== 'paper':
    print("You win")
elif useroption=='paper' and comoption == 'rock':
    print("You win")
else:
    print("Computer win")