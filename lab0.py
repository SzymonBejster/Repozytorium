def poleprostokata(dlugosc, szerokosc):
    return dlugosc * szerokosc

def obwodprostokata(dlugosc, szerokosc):
    return 2 * (dlugosc + szerokosc)


dlugosc_boku = float(input("Podaj długość boku prostokąta: "))
szerokosc_boku = float(input("Podaj szerokość boku prostokąta: "))


pole = poleprostokata(dlugosc_boku, szerokosc_boku)
obwod = obwodprostokata(dlugosc_boku, szerokosc_boku)


print(f"Pole prostokąta: {pole}")
print(f"Obwód prostokąta: {obwod}")
