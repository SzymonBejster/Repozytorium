
x = float(input("Podaj pierwszą liczbę (x): "))
y = float(input("Podaj drugą liczbę (y): "))
z = float(input("Podaj trzecią liczbę (z): "))


if x > y:
    x, y = y, x
if y > z:
    y, z = z, y
if x > y:
    x, y = y, x


print("od najmniejszej do największej:")
print(f"x: {x}")
print(f"y: {y}")
print(f"z: {z}")
