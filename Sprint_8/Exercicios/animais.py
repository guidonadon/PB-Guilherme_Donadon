animais = [
    "Macaco", "Cobra", "Tubarão", "Cachorro", "Ameba",
    "Rato", "Gato", "Papagaio", "Mula", "Caracol",
    "Peixe", "Urso", "Tigre", "Leão", "Lobo",
    "Mamute", "Dinossauro", "Boi", "Camarão", "Elefante"
]

animais.sort()

[print(animal) for animal in animais]

with open("animais.csv", "w", encoding="utf-8") as arquivo:
    arquivo.write("\n".join(animais))