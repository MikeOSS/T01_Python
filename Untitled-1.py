# a = int(input("digite um número"))
# b = input("digite outro número")
# prox = a
# for i in b:
#     print(i, end = " ")
    
#     while prox > 0:
        
#         algarismo = prox % 10
#         prox = prox // 10
#         print(prox, end= "")
#         # if (int(i)==algarismo):
#         #     # print(algarismo, end = " ")
secret = 1234
primeiro = secret //1000
segundo= (secret % 1000)//100
terceiro= (secret % 1000) // 10
quarto = (secret % 1000) % 10




tentativa = input("Digite uma tentativa: ")
cont_alg = 0

m = "-"
c = "-"
d = "-"
u = "-"

for alg in tentativa:
