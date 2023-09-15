# feladat_001

"""
Kérjük be a billentyűzetről a nevünket, és írassuk ki a képernyőre!
A billentyűzetről mindig szöveget (string-et) olvasunk be!
type(változó) --- visszaadja a változó típusát
"""

'''
nev = input('Kérek egy nevet: ')
print(f'A megadott név a következő: {nev}')
'''

vnev = input('Kérek egy vezeték nevet: ')
knev = input('Kérek egy kereszt nevet: ')
print(f'A megadott név a következő: {vnev} {knev}')

print(f'A vnev változó típusa: {type(vnev)}')
print(f'A knev változó típusa: {type(knev)}')

