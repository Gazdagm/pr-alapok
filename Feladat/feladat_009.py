#feladat_009
"""
Kérjünk be két egész számot, szám1 és szám2.
Hasonlítsuk össze a két számot, és írassuk ki, hogy
a szám1 kisebb, mint szám2,
vagy a szám2 kisebb, mint a szám1,
vagy a szám1 egyenlő szám2-vel.
"""

szám1 = input('írj be egy számot!')
szám2 = input('írj be mégegy számot!')
szám1 = int(szám1)
szám2 = int(szám2)

"""
if szám1<szám2:
    print(f'Szám1 kisebb, mint szám2.')
elif szám2<szám1:
    print(f'A szám2 kisebb, mint a szám1.')
else szám1 == szám2:
    print(f'A két szám megegyezik.')
"""

"""
if szám1<szám2:
    print(f'Szám1 kisebb, mint szám2.')
if szám2<szám1:
    print(f'A szám2 kisebb, mint a szám1.')
if szám1 == szám2:
    print(f'A két szám megegyezik.')
"""

if szám1<szám2:
    print(f'Szám1 kisebb, mint szám2.')
elif szám2<szám1:
    print(f'A szám2 kisebb, mint a szám1.')
elif szám1 == szám2:
    print(f'A két szám megegyezik.')