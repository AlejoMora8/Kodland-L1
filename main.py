meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "ROFL": "una respuesta a una broma",
            "SHEESH" : "ligera desaprobación",
            "CREEPY" : "aterrador, siniestro",
            "AGGRO" : "ponerse agresivo/enojado"
            }

print("Hola")
bucle=int(input("Cuantas palabras no entienes?"))
for i in range(bucle) :
    
    word = input("Escribe una palabra que no entiendas (¡con mayúsculas!):")
    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print("Esa palabra no esta en el diccionario")