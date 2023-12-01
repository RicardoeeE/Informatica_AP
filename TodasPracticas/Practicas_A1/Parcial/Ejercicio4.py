"""
• Desarrollar un programa que permita calcular el importe correspondiente al alquiler de películas en un video
club. Para ello:
• Se pedirá al usuario, el número de películas que va a alquilar comprobando que sea mayor que cero.
• Se calculará el importe a pagar teniendo en cuenta la siguiente tabla de tarifas:
• Menos de 3 películas: 2.15 euros/película
• 3 - 5 películas: 1.75 euros/película
• 6 - 10 películas: 1.25 euros/película
• Más de 10: 1 euro/película
• Se mostrará por pantalla el importe en euros y céntimos. Si alguna cantidad es cero, no se mostrará por
pantalla.
"""

num_pelis = 0
def imp_pagar(num_pelis):
    if num_pelis < 3:
        costePorPeli = 2.15
    elif num_pelis > 3 and num_pelis < 5:
        costePorPeli = 1.75
    elif num_pelis < 6 and num_pelis < 10:
        costePorPeli = 1.25
    else:
        costePorPeli = 1
    return costePorPeli

a = int(input("Dame el numero de pelis que te llevas "))
print(imp_pagar(a))

