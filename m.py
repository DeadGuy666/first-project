meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "ROFL" : "una respuest-a a una broma",
            "SHEESH" : "ligera desaprobación",
            "CREEPY" : "aterrador, siniestro",
            "AGGRO" : "ponerse agresivo/enojado",
}
word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
if word in meme_dict.keys():
    print("Lo que significa tu palabra es:", meme_dict[word])
else:
    print("Perdone no encontramos su palabra")
