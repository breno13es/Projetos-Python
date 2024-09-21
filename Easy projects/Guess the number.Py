import random
import time

def guess(x):
    secret_num = random.randint(1,x) # Escolhe um numero entre 1 e "X"
    guess = 0
    while guess != secret_num: # Cria a while loop
        guess = int(input(f"guess lil bro 1 - {x}: "))
        if guess < secret_num: # Cria as condicionais
            print ("Sorry, you're too low")
            time.sleep(2)
        elif guess > secret_num:
            print("Slow a bit dearie")
            time.sleep(2)
        elif guess == secret_num:
            print("Hey pretty luck you have, hm?")# Parabeins
            time.sleep(3)
            print("Congrats bud you got it")
            time.sleep(3)


guess(10) #this changes the max of the expression as the "X"