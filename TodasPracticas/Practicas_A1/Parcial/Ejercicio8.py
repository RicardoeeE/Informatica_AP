#Mostar  numeros oblongos entre n1  y n2
# Oblongo producto igal de dos numeos cosnecutivos
# N1 y n2 n1>1 y n2>n1
#f(x) limite inferior que debe cumplir y devolver 
# es oblogno true false
def pedir_num(min):
    num = int(input(f"Dame un numero mayor que {min} "))
    while num<=min:
        num = int(input(f"Dame un numero mayor que {min} "))
    return num

# def es_oblongo(num):
#     n = 1
#     oblongo == False
#     while n<num and (not oblongo):
#         if n*(n+1) == num:
#             oblongo = True
#         n+=1
#     return oblongo

n1 = pedir_num(1)
n2 = pedir_num(n1)

print(f"Los numeros oblognso entre {n1} y {n2} son: ")
n=0
for num in range(n1,n2+1):
    if es_oblongo(num) ==True:
        n+=1
        print(num,end=" ")

if n>0:
    print(f"En total son {num}")
else:
    print(f"No se ha encontrado ningun numero oblongo")

