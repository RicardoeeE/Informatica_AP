"""
Menos 10.000 ------ 5%
      10.000 -20.000 ------ 15%
      20.000 -35.000 ------ 20%
      35.000 -60.000 ------ 30%
Mas   60.000 ------ 45%
"""
a = 10000
b = 20000
c = 35000
d = 60000

imp_a = 5
imp_b = 15
imp_c = 20
imp_d = 30
imp_e = 45

imp_b

rentaUser = int(input("Dime que cantidad ganas y te doy el impuesto a pagar: "))

if(rentaUser > a ):
    print("Has de pagar el 5% ")
elif rentaUser > a and rentaUser < b:
    print("Has de pagar el 15%")
elif rentaUser > b and rentaUser < c:
    print("Has de pagar el 20%")
elif rentaUser > c and rentaUser < d:
    print("Has de pagar el 30%")
elif rentaUser > d:
    print("Has de pagar el 45%")