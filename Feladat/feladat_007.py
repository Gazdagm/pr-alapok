#feladat_007
#dk9 108-109 oldal
"""
gondolt_szám=4
ki:'gondoltam egy számra'
be: tipp
tipp alakítása egésszé 
elágazás
ha tipp = gondolt_szám:
ki: dicséret
elágazás vége
ki:búcsú
"""

gondolt_szám = 4
tipp = input('Gondoltam egy számra. Tippeld meg!')
tipp = int(tipp)
if tipp == gondolt_szám:
    print(f'Ügyes vagy!')
    print(f'Gratulálok')
else:
    print('Hosszan gondolkodtál rajta?:)')
    print('Nem érte meg.:(')
print('Pápá.')