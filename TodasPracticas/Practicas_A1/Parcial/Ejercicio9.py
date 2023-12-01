# def factorial(num):
#     while num >= 1:
#         factorial = num*num
#         num-=1
#     return factorial

# print(factorial(500))
a=1
num = int(input("Dame un numero "))
while num > 1:
    while (num-1) < num:
        factorial = num*(num-1)
        num-=1
    num-=1
print(a)