# La fonction sum() additionne deux nombres et prend en paramètre la valeur a & b
def sum(a, b):
    return a + b

# La fonction substraction() soustrait deux nombres et prend en paramètre la valeur a & b
def subtraction(a, b):
    return a - b

a = int(input("\nEntrez la valeur de a : "))
b = int(input("Entrez la valeur de b : "))

print(f"\nLa somme de {a} + {b} est égal à {sum(a, b)}.")

print(f"La soustraction de {a} - {b} est égal à {subtraction(a, b)}.")