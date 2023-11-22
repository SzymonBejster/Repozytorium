
litera = input("Wprowadź literę: ")


if litera.isalpha():
    if litera.islower():
        print("Wprowadzona litera jest mała.")
    elif litera.isupper():
        print("Wprowadzona litera jest duża.")
