
def main():
  import random
  dicesum=0
  dicesize=int(input('How many sides does you die have?\n'))
  dice_rolls= int(input('How many dice will you roll?\n'))
  for i in range(0, dice_rolls):
    roll = random.randint(1,dicesize)
    if roll ==1:
      print(f'Oopsies. You rolled a {roll}..Snake Eyes.rzzt')
    elif roll == dicesize:
      print(f'You rolled a {roll}! Critical success')
    else:
      print(f'You rolled a {roll}')
    dicesum+=roll
  print(f'You have rolled {dicesum}')

if __name__== "__main__":
  main()