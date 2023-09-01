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

#Write your code below this line 👇

# Rock beats scissors, scissors beat paper, and paper beats rock.

your_choice = int(input("Enter 0 for rock, 1 for paper and 2 for scissors. "))
computer_choice = random.randint(0,2)
print(computer_choice)

if your_choice == computer_choice:
    print("It's Draw!")
elif your_choice == 0 and computer_choice == 2:
    print("You Win!")
elif your_choice < computer_choice:
    print("You Loose!")
elif your_choice == 2 and computer_choice == 0:
    print("You Loose!")
else:
    print("You Win!")



