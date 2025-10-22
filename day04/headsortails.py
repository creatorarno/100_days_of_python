import random

call = input("Heads (H) or Tails (T): ")

coin = ['H', 'T']

random_coin = random.choice(coin)

if call == random_coin:
    print("You won!")
else:
    print("You lost!")