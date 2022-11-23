import numpy as np
ganancia = 0
frecuency = {"E": 0.1202, "T": 0.091, "A": 0.0812, "O": 0.0768, "I": 0.0731, "N": 0.0695, "S": 0.0628, "R": 0.0602, "H": 0.0592, "D": 0.0432, "L": 0.0398, "U": 0.0288, "C": 0.0271, "M": 0.0261, "F": 0.023, "Y": 0.0211, "W": 0.0209, "G": 0.0203, "P": 0.0182, "B": 0.0149, "V": 0.0111, "K": 0.0069, "X": 0.0017, "Q": 0.0011, "J": 0.001, "Z": 0.0008}
palabras = 9
numero_corridas = 5000
cantidad_letras = 20
reward = {
    1: 5,
    2: 10,
    3: 15,
    4: 20,
    5: 25,
    6: 35
}

def choose_letters():
    return np.random.choice(list(frecuency.keys()), cantidad_letras, p = [frecuency[key] for key in frecuency])

def read_words():
    f = open("words.txt", "r")
    words = np.array([element.upper() for element in f.read().splitlines()])
    return words
    
lista_palabras = read_words()

def choose_words():
    return np.random.choice(lista_palabras, 9, replace=False)


cantidad_personas = []
margen = 100

for i in range(numero_corridas):
    count = 1
    win = False
    while not win:
        ingreso = count * 5
        perdida_total = 0
        for i in range(count):
            
            perdida = 0
            letras = choose_letters()
            selected_words = choose_words()

            for letra in letras:
                for i in range(len(selected_words)):
                    word = selected_words[i]
                    if letra in word:
                        selected_words[i] = word.replace(letra, '')
            palabras_encontradas = 0
            for i in selected_words:
                if i == '':
                    palabras_encontradas += 1
            if palabras_encontradas  >= 1 and palabras_encontradas < 6:
                for key in reward:
                    if key == palabras_encontradas:
                        perdida += reward[key]
            elif palabras_encontradas >= 6:
                perdida += reward[6]
            
            perdida_total += perdida

        if ingreso - perdida > margen:
            win = True
        else:
            count += 1
    cantidad_personas.append(count)

print(cantidad_personas)