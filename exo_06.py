# Fonction calculate_average

def calculate_average(numbers):
    average = sum([number for number in numbers]) // len(numbers)
    return average


# Exemple d'utilisation de la fonction
numbers = [10, 20, 30, 40, 50]

average = calculate_average(numbers)
print("\nLa moyenne des nombres de la liste [numbers] est :", average)