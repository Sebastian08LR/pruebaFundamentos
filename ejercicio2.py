base = float(input("Ingrese el valor de la base del triangulo: "))
hight = float(input("Ingrese el valor de la altura del triangulo: "))

area = (base * hight) / 2

if area > 1000:
    print("---DATOS NO VÁLIDOS---")
else:
    print(f"El area del triangulo es igual a: {area}")
    