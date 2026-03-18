import random

words = {
    "1 - Estructuras": ["funcion", "bucle"],
    "2 - Datos": ["cadena", "entero", "lista"],
    "3 - Otras": ["python", "programa", "variable"],
}

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
word = random.choice(words[categ])
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
    letter = input("Ingresá una letra: ")
    if len(letter) == 1 and letter.isalpha():
        if letter.isupper:
            letter = letter.lower()
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
print(f"Puntaje: {puntaje}")
