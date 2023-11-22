def oblicz_zuzycie_paliwa(dystans, spalanie):
    return (dystans / 100) * spalanie

def oblicz_koszty_paliwa(zuzycie_paliwa, cena_paliwa):
    return zuzycie_paliwa * cena_paliwa

# Pobranie danych od użytkownika
try:
    dystans = float(input("Podaj dystans pokonany przez samochód (w km): "))
    spalanie = float(input("Podaj średnie spalanie samochodu (w litrach na 100 km): "))
except ValueError:
    print("Wprowadź poprawne liczby.")
    exit()

# Cena paliwa (w złotych na litr)
cena_paliwa = 6.5

# Obliczenia
zuzycie_paliwa = oblicz_zuzycie_paliwa(dystans, spalanie)
koszty_paliwa = oblicz_koszty_paliwa(zuzycie_paliwa, cena_paliwa)

# Wyświetlenie wyników
print(f"Przewidziane zużycie paliwa: {zuzycie_paliwa:.2f} litrów")
print(f"Przewidziane koszty podróży: {koszty_paliwa:.2f} zł")
