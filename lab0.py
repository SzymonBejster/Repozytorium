def dodawanie(x, y):
    return x + y

def odejmowanie(x, y):
    return x - y

def mnozenie(x, y):
    return x * y

def dzielenie(x, y):
    if y != 0:
        return x / y
    else:
        return "Nie można dzielić przez zero."

def potegowanie(x, y):
    return x ** y


print("Wybierz operację:")
print("1. Dodawanie")
print("2. Odejmowanie")
print("3. Mnożenie")
print("4. Dzielenie")
print("5. Potęgowanie")


wybor = input("Wprowadź numer operacji (1/2/3/4/5): ")


liczba1 = float(input("Podaj pierwszą liczbę: "))
liczba2 = float(input("Podaj drugą liczbę: "))


if wybor == '1':
    print(f"Wynik dodawania: {dodawanie(liczba1, liczba2)}")
elif wybor == '2':
    print(f"Wynik odejmowania: {odejmowanie(liczba1, liczba2)}")
elif wybor == '3':
    print(f"Wynik mnożenia: {mnozenie(liczba1, liczba2)}")
elif wybor == '4':
    print(f"Wynik dzielenia: {dzielenie(liczba1, liczba2)}")
elif wybor == '5':
    print(f"Wynik potęgowania: {potegowanie(liczba1, liczba2)}")
else:
    print("Nieprawidłowy wybór. Wybierz numer od 1 do 5.")
