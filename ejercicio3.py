sumVoltajes = 0

for i in range (3):
    sumVoltajes += float(input(f"Ingrese el voltaje {i+1}: "))

promVoltajes = sumVoltajes / 3

if promVoltajes > 220:
    print(f"El promedio de los voltajes es {round(promVoltajes)}\n\t ---PELIGRO---")
elif (promVoltajes < 220 and promVoltajes > 115):
    print(f"El promedio de los voltajes es {round(promVoltajes)}\n\t ---ALTO VOLTAJE---")
else:
    print(f"El promedio de los voltajes es {round(promVoltajes)}\n\t ---VOLTAJE CORRECTO---")

