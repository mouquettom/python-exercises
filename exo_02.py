students = {
    'Alice': {
        'Mathematiques': 90,
        'Francais': 80,
        'Histoire': 95
    },
    'Bob': {
        'Mathematiques': 75,
        'Francais': 85,
        'Histoire': 70
    },
    'Charlie': {
        'Mathematiques': 88,
        'Francais': 92,
        'Histoire': 78
    }
}

while True:
    student = input("\nEntrez le nom de l'étudiant : ")

    if student not in students:
        print(f"L'étudiant {student} n'existe pas dans la liste.")
        continue

    for matiere in students[student]:
        print(f"Note de {student} en {matiere} : {students[student][matiere]}")
    break
