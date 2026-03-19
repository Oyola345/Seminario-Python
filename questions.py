import random

words = {
    "1 - Estructuras": ["funcion", "bucle"],
    "2 - Datos": ["cadena", "entero", "lista"],
    "3 - Otras": ["python", "programa", "variable"]
}

used_words = {
    "1 - Estructuras": [],
    "2 - Datos": [],
    "3 - Otras": []
}

puntaje_total = 0
rondas = 0
jugar = True

while jugar:
    rondas+=1
    print(list(words.keys()))
    categ = int(input("Ingrese el número de categoría que quiere jugar: "))
    match categ:
        case 1:
            categ = "1 - Estructuras"
        case 2:
            categ = "2 - Datos"
        case 3:
            categ = "3 - Otras"
        case _:
            print("Categoría no válida. Se seleccionará una categoría al azar.")
            categ = random.choice(list(words.keys()))
    
    if len(words[categ])==0:
        words[categ] = random.sample(used_words[categ],len(used_words[categ])) #copiar palabras usadas y permutarlas
        print(words[categ])
        used_words[categ] = []
    
    word = words[categ][0]    #si la categoria tiene al menos un elemento siempre sera accesible la posición 0
    words[categ].remove(word)
    used_words[categ].append(word)
    
    guessed = []
    attempts = 6
    print("¡Bienvenido al Ahorcado!")
    print()
    puntaje = 0
    while attempts > 0:
        # Mostrar progreso: letras adivinadas y guiones para las que faltan
        progress = ""
        for letter in word:
            if letter in guessed:
                progress += letter + " "
            else:
                progress += "_ "
        print(progress)  # Verificar si el jugador ya adivinó la palabra completa
        if "_" not in progress:
            print("¡Ganaste!")
            puntaje += 6
            break
        print(f"Intentos restantes: {attempts}")
        print(f"Letras usadas: {', '.join(guessed)}")
        letter = input("Ingresá una letra: ").lower()
        if len(letter) == 1 and letter.isalpha():
            if letter in guessed:
                print("Ya usaste esa letra.")
            elif letter in word:
                guessed.append(letter)
                print("¡Bien! Esa letra está en la palabra.")
            else:
                guessed.append(letter)
                attempts -= 1
                puntaje -= 1
                print("Esa letra no está en la palabra.")
        else:
            print("Entrada no válida")
        print()
    else:
        puntaje = 0
        print(f"¡Perdiste! La palabra era: {word}")
    print()
    puntaje_total += puntaje
    print(f"Puntaje: {puntaje}")
    print(f"Puntaje global: {puntaje_total}")
    rta = ""
    while (rta != "no" and rta != "si"):
        rta = input("¿Desea seguir jugando? Responda si/no: ")
        match rta:
            case "si":
                pass
            case "no":
                jugar = False
    print()
print(f"¡Buena partida! Ha hecho {puntaje_total} puntos y jugó {rondas} rondas.")