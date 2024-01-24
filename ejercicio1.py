sumVoltajes = 0

for i in range (5):
    sumVoltajes += float(input(f"Ingrese el voltaje {i+1}: "))

promVoltajes = sumVoltajes / 5

if promVoltajes > 220:
    print(f"El promedio de los voltajes es {promVoltajes}\n\t ---ALTO VOLTAJE---")
else:
    print(f"El promedio de los voltajes es {promVoltajes}\n\t ---VOLTAJE CORRECTO---")
