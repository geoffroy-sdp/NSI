def delta_encoding(valeurs):
    # Au cas où le tableau serait vide
    if not valeurs:
        return 'Le tableau est vide'
    
    # La première valeur est celle que l'on retourne directement
    premiere_valeur = valeurs[0]
    
    # Initialiser la liste des différences
    differences = []
    
    # Parcourir la liste à partir du deuxième élément
    for i in range(1, len(valeurs)):
        diff = valeurs[i] - valeurs[i - 1]
        differences.append(diff)
    
    return (premiere_valeur, differences)

# tests

assert delta_encoding(
    [1_000_000, 1_000_042, 1_000_040, 1_000_055, 1_000_010]
) ==  (1000000, [42, -2, 15, -45])

assert delta_encoding([42]) == (42, [])