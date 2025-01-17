import random

def generador(pass_length):
    characts = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    contra = ""

    for i in range(pass_length):
        contra += random.choice(characts)

    return contra
