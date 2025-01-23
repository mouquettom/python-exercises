def square(a):
    return a**2

while True:
    a = ""
    while not a.isdigit():
        a = input("\nEntrez la valeur de a : ")
        if not a.isdigit():
            print("Le paramètre doit être un nombre !")
        continue

    a = int(a)
    print(f"Le carré du nombre {a} est {square(a)}.")
    break