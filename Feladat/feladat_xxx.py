#feladat_014
"""
Kérjük be a vezeték és keresztnevünket.
Írassuk ki eljárás segítségével a nevünket. 
Pl:
Be: 'Kérem a vezeték neved: Gazdag'
Be: 'Kérem a kereszt neved: Máté'
Ki, a nevem: Gazdag Máté
"""

vezetek = input(f'Kérem a vezetékneved: ')
kereszt = input(f'Kérem a keresztneved: ')

def nev(vnev, knev):
    print(f'A nevem: {vnev} {knev}')

nev(vezetek,kereszt)
