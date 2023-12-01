# Ejercicio uno:
print("====================================================")
hora = int(input("Introduce las horas: "))
minutos = int(input("Introduce los minutos: "))
segundos = int(input("Introduce los segundos: "))
separador = input("Introduce el caracter separador: ")
print("\n")

hora_format = str(hora).zfill(2)
minutos_format = str(minutos).zfill(2)
segundos_format = str(segundos).zfill(2)

texto = "La hora introducida es: "
texto_2 = "Han transcurrido"
if hora == 1:
    texto_3 = "segundo desde la"
    texto_4 = "hora"
else:
    texto_3 = "segundos desde las"
    texto_4 = "horas"

convertir = (minutos * 60) + segundos

resultado = f"{texto} {hora_format}{separador}{minutos_format}{separador}{segundos_format}"
resultado2 = f"{texto_2} {convertir} {texto_3} {hora_format}"

print(resultado)
print(resultado2)
print("====================================================")

