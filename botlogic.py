import random

def generador(pass_length):
    characts = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    contra = ""

    for i in range(pass_length):
        contra += random.choice(characts)

    return contra


def gen_emoji():
    emoji = ["\U0001f600", "\U0001f642", "\U0001F606", "\U0001F923",":sunglasses:",":grapes:",":partying_face:",":metal:"]
    return random.choice(emoji)


def gira_una_moneda():
    giro = random.randint(0, 2)
    if giro == 0:
        return "Cara"
    else:
        return "Sello"
