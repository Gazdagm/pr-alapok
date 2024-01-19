#Listák metódusai: Rendezés

nyelvek = ['Python', 'C', 'C++', 'Java']

keresett_elem = "C#"

if keresett_elem in nyelvek:
    print(nyelvek.index(keresett_elem))
else:
    print(f"Nincs a listában a {keresett_elem}.")

szamlalo = 0
for elem in nyelvek:
    if elem == :
        szamlalo = szamlalo + 1
    print(f"A python elem ennyiszer fordult elő. {szamlalo}")