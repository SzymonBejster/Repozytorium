
wiek = int(input("Wprowadź wiek klienta: "))


if wiek < 4:
    cena_biletu = 0
elif 4 <= wiek <= 18:
    cena_biletu = 10
else:
    cena_biletu = 20


print(f"Cena biletu: {cena_biletu} zł")
