# a = int(input("dame un numero mayor que cero y menor que 100: "))
# while a < 0 or a > 100:
#     a = int(input("dame un numero mayor que cero y menor que 100 ESTA VEZ VALIDO "))
# multiplos=[]
# for x in range(1,a):
#     if x % 5 == 0:
#         multiplos.append(x)
    

# strA= str(a)
# suma=sum(multiplos)
# longitud=len(multiplos)
# mediaAritmetica= suma/longitud
# strMediaAritmetica=str(mediaAritmetica)
# print("La media de lo numeros multipos de 5 en este rango 1 y "+strA+" es: "+ strMediaAritmetica)
media = 0.0
verdadero = -1
a = int(input("dame un numero mayor que cero y menor que 100: "))
while a < 0 or a > 100:
    a = int(input("dame un numero mayor que cero y menor que 100 ESTA VEZ VALIDO "))
for x in range(1,a+1):
    if x % 5 == 0:
        verdadero + 1
        print(x) 
        media += x
        # print(media)
longitud = verdadero
artimetica = float(media / longitud)
print(media)
print(artimetica)