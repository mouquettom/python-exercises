# La fonction addition() additionne deux nombres et prend en paramètre la valeur a & b
def addition(a, b):
    return a + b

# La fonction subtraction() soustrait deux nombres et prend en paramètre la valeur a & b
def subtraction(a, b):
    return a - b


if __name__ == "__main__":
    a = int(input("\nEntrez la valeur de a : "))
    b = int(input("Entrez la valeur de b : "))

    print(f"\nLa somme de {a} + {b} est égale à {addition(a, b)}.")

    print(f"La soustraction de {a} - {b} est égale à {subtraction(a, b)}.")
