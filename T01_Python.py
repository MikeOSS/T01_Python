import random

# gerando número aleatório e separando por partes:
# numero_secreto = random.randint(1000, 9999)

# primeiro = numero_secreto //1000
# segundo= (numero_secreto % 1000)//100
# terceiro= (numero_secreto % 1000) // 10
# quarto = (numero_secreto % 1000) % 10

# print(numero_secreto)
# print(primeiro)
# print(segundo)
# print(terceiro)
# print(quarto)

# Tela inicial:
print("\n" * 5)
print(" " * 10 + "=> Bem vindo Ao Jogo SECRETO!!! <=" )
print("\n" * 2)
print("Você tem 10 tentativas para acertar o número secreto entre [1000 e 9999] \nA partir da 5a. tentativa o jogo irá te ajudar, dando dicas")
print(" " * 20 + "<<< Tecle Algo >>>")
input()

#Tela principal 
numero_ficticio = 4789 # número padrão para pensarmos em como fazer dps com o random
# divisão dos números:
milhar = numero_ficticio // 1000
cent = (numero_ficticio % 1000) // 100 
dez = (numero_ficticio % 100)// 10
unidade = (numero_ficticio) % 10

cont = 10
cont_tentativas = 0
cont_algarismos = 0
while (cont > 0):
    num1='_'
    num2="_" 
    num3="_"
    num4="_"
    #contanto as tentativas:
    cont_tentativas += 1
    tentativa = int(input(f'digite sua tentativa de código:{num1} '))
    # dividindo o número que usuário digitou
    t_milhar = tentativa // 1000
    t_centena = (tentativa % 1000) // 100
    t_dezena = (tentativa % 100) // 10
    t_unidade = tentativa % 10 
    

    if(tentativa == numero_ficticio): # Tela de vitória direto1
        cont = 0
        print('\n' * 5)
        print(' ' * 15 + "P Á R A B E N S ! ! !")
        print("\n"* 5)
        print(f'\t Você acertou o código: {t_milhar} {t_centena} {t_dezena} {t_unidade} \nem {cont_tentativas} tentativas')
        print("\n" * 2)
        print(' ' * 50 + "<<< tecle algo >>>")
        input()

    else: 
        if milhar == t_milhar:
                num1=milhar
        else:
            if cent == t_centena:
                num2 == cent
            else: 
                if dez == t_dezena:
                    num3 == dez
                else:
                    if unidade == t_unidade:
                        num4 == unidade
                    else:
                        print(f"{num1} {num2} {num3} {num4}")
                        cont -= 1
else:
    print(f"acabaram as tentativas")
# vendo se o jogador quer jogar mais uma vez dps de ter acabado as tentativas ou ter ganhado o jogo
if(cont < 1):
    more1 = int(input("jogar mais uma vez?? 1=SIM E 0=NÃO \n==>"))
    if(more1 == 1):
        cont = 10    
    