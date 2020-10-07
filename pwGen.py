# Password Generator made by Nelson Santos

import random

characters = 'abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&@.;*^'


def Exit():
    print("Exit?: [Y/N]")
    answer = input()

    if(answer == "y" or answer == "Y"):
        print("Thanks for using my app!")

    elif (answer == "n" or answer == "N"):
        Password_Generator(characters)

    else:
        print("Invalid Character, try again")
        Exit()


def Password_Generator(characters):

    pass_ammo = input("Enter the ammount of passwords you want to generate: ")
    pass_ammo = int(pass_ammo)
    print("RECOMENDED PASSWORD LENGTH IS ABOVE 11 CHARACTERS!")
    pass_length = input("Enter the length of the password:")

    pass_length = int(pass_length)

    for p in range(pass_ammo):
        password = ''
        for character in range(pass_length):
            password += random.choice(characters)
        print("Your password is: " + str(password))
    Exit()


Password_Generator(characters)
