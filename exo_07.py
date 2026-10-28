def square(a):
    return a**2


if __name__ == "__main__":
    a = ""
    while not a.isdigit():
        a = input("\nEntrez la valeur de a : ")
        if not a.isdigit():
            print("Le paramètre doit être un nombre !")

    a = int(a)
    print(f"Le carré du nombre {a} est {square(a)}.")
