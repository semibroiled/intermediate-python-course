
def main():
  import random
  dicesum=0
  dice_rolls=2
  for i in range(0, dice_rolls):
    roll = random.randint(1,6)
    print(f'You rolled a {roll}')
    dicesum+=roll
  print(f'You have rolled {dicesum}')

if __name__== "__main__":
  main()