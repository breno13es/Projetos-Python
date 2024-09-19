import random #importar o random, se não você não consegue usar.
import time

def Jokenpo():
    Options = ["p", "e", "r"] ## Primeiro você cria uma lista com as opções desejadas.
    Computer_choice = random.choice(Options)  # Pede pro computador escolher um deles.
    Player_choice = input("Choose (R)ock, (P)aper, (E)xcisor: ")  # Ai você pergunta ao jogador a opção.
    if Computer_choice == "p" and Player_choice == "e":  # Cria as funções com as consequencias.
        print("You won, i had choose Paper")
    if Computer_choice == "r" and Player_choice == "p":
        print("You won, i had choose Rock")
    if Computer_choice == "e" and Player_choice == "r":
        print("You won, i had choose Excisor")
    elif Computer_choice == Player_choice:
        print("It's an draw")
    elif Computer_choice == "r" and Player_choice == "e":
        print("you lost bud, i had choose Rock")
    elif Computer_choice == "p" and Player_choice == "r":
        print("you lost bud, i had choose Paper")
    elif Computer_choice == "e" and Player_choice == "p":
        print("you lost bud, i had choose Excisor")

Proposal = input("Wanna play a game? Y or N: ")
if Proposal.upper() == "Y":
    Jokenpo()
    time.sleep(3)
elif Proposal.upper() == "N":
    print("womp womp chicken")
    time.sleep(3)
else:
    print("It's to complicated to your lil brain, isn't?")
    time.sleep(3)