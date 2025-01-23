words = ["python", "programmation", "langage", "ordinateur", "apprentissage"]

voyelles = ["a", "e", "i", "o", "u", "y"]

resultat = [(word, sum(1 for lettre in word if lettre in voyelles)) for word in words]
print(resultat)