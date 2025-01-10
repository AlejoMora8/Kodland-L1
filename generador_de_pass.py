import random
dic="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
long=int(input("Decida la longitud de su contraseña:"))
contra=""
for i in range(long):
    contra += random.choice(dic)

print("Tu contraseña generada es:",contra)
