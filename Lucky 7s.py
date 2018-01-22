import random

print("Welcome to lucky 7s! You start with $15. Each time you play, you place a bet of $1. Then you roll 2 dice. "
      "If you get a 7 then you win your bet back plus an additional $4. ")
print("Good Luck!")

dice2 = random.randint(1,6)

dice1 = random.randint(1,6)

print(dice1)
print(dice2)

money = 15
total = dice1 + dice2
if total == 7:
      money += 5
else:
      money -= 1


while 












