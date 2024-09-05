# à compléter ici
def occurrence_caracteres(phrase):
    occurrences = {}
        
    for caractere in phrase:
        if caractere in occurrences:
            occurrences[caractere] += 1
        else:
            occurrences[caractere] = 1
    if not occurrences :
        print("le dictionnaire est vide")
    return occurrences

# tests

assert occurrence_caracteres("Bonjour à tous !") == {
    'B': 1, 'o': 3, 'n': 1, 'j': 1, 'u': 2, 'r': 1,
    ' ': 3, 'à': 1, 't': 1, 's': 1, '!': 1
}

assert occurrence_caracteres("ababbab") == {"a": 3, "b": 4}