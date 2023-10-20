#feladat_015
"""
Kérjük be a vezeték és keresztnevünket.
Írassuk ki fügvény segítségével a nevünket. 
Pl:
Be: 'Kérem a vezeték neved: Gazdag'
Be: 'Kérem a kereszt neved: Máté'
Ki, a nevem: Gazdag Máté
"""

vezetek = input(f'Kérem a vezetékneved: ')
kereszt = input(f'Kérem a keresztneved: ')

def nevf(vnev, knev):
    nevem = vnev + ' ' + knev
    return nevem

print(f'A nevem: {nevf(vezetek,kereszt)}')