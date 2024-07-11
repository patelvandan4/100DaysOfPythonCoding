import random
print("Welcome to the random coin generator.")
coin = random.randint(0, 1)
if coin == "1":
    print("Heads")
else:
    print("Tails")