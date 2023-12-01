# 1- Calcular primorial
# 2- Comprobar omirp
# 3- Comprobar abundante
# 4- Salir
# Escoja una de las opciones anteriores: 0
# Opción incorrecta. Vuelva a intentarlo: 1

op=int(input("Escoja una de las opciones anteriores: "))
def menu(op_user):
    print("1- Calcular primorial \n 2- Comprobar omirp \n 3- Comprobar abundante \n 4- Salir")
    op_user=int(input("Escoja una de las opciones anteriores: "))
    while op_user != 1 and  2 and  3 and  4:
        print("Opción incorrecta vuelve a intentarlo:")
    
menu(op)


def es_primo(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3,int(num**0.5) + 1,2):
        if num % i == 0:
            return False
    return True

def calcualr_primorial(n):
    primorial=1
    primo_cuenta=0
    num=2
    while primo_cuenta < n :
        if es_primo(num):
            primorial*= num
            primo_cuenta += 1
        num +=1
    return primorial

    
        
