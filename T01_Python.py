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
print(" " * 10 + "=> Bem vindo Ao Jogo SECRETO!!! <=")
print("\n" * 2)
print(
    "Você tem 10 tentativas para acertar o número secreto entre [1000 e 9999] \nA partir da 5a. tentativa o jogo irá te ajudar, dando dicas")
print(" " * 20 + "<<< Tecle Algo >>>")
input()
num_de_jogadas = 1
# Tela principal
numero_ficticio = 4789  # número padrão para pensarmos em como fazer dps com o random
# divisão dos números:
milhar = numero_ficticio // 1000
cent = (numero_ficticio % 1000) // 100
dez = (numero_ficticio % 100) // 10
unidade = (numero_ficticio) % 10
# contadores
cont = 10
cont_tentativas = 0
cont_algarismos = 0

while num_de_jogadas > 0:
    while (cont > 0):
        num1 = '_'
        num2 = "_"
        num3 = "_"
        num4 = "_"
        # contando as tentativas:
        tentativa = int(input(f'digite sua tentativa de código: '))
        # Tentativa de fazer o programa não reconhecer numeros fora do escopo e letras digitadas!
        while (tentativa < 1000 or tentativa > 9999):
            print('\t\t\t A T E N Ç Ã O!!\n')
            print('\t\tDigite um número válido entre 1000 e 9999!!\n')
            print('\t\t\t<<<tecle algo>>>')
            input()
            tentativa = int(input(f'digite sua tentativa de código: '))
        while (not int(tentativa)):
            print('\t\t\t A T E N Ç Ã O!!\n')
            print('\t\tDigite apenas números!!!\n')
            print('\t\t\t<<<tecle algo>>>')
            input()
            tentativa = int(input(f'digite sua tentativa de código: '))

        cont_tentativas += 1
        # dividindo o número que usuário digitou
        t_milhar = tentativa // 1000
        t_centena = (tentativa % 1000) // 100
        t_dezena = (tentativa % 100) // 10
        t_unidade = tentativa % 10
        # faz o numero aparecer na tela quando acertado e conta os algarismos certos
        if milhar == t_milhar:
            cont_algarismos += 1
            num1 = milhar
        if cent == t_centena:
            cont_algarismos += 1
            num2 = cent
        if dez == t_dezena:
            cont_algarismos += 1
            num3 = dez
        if unidade == t_unidade:
            cont_algarismos += 1
            num4 = unidade  # PROBLEMA : QUANDO COLOCO SÓ O 9 ELE RECONHECE COMO ÚLTIMO ALGARISMO!

        cont -= 1
        # quando acertou o numero
        if (t_milhar == milhar and t_centena == cent and t_dezena == dez and t_unidade == unidade):
            cont = 0
            print('\n' * 5)
            print(' ' * 15 + "P Á R A B E N S ! ! !")
            print("\n" * 5)
            print(
                f'\t Você acertou o código: {t_milhar} {t_centena} {t_dezena} {t_unidade} \nem {cont_tentativas} tentativas')
            print("\n" * 2)
            print(' ' * 50 + "<<< tecle algo >>>")
            input()
        else:
            # verificando se u usuário acertou algum algarismo
            if (cont_algarismos > 0):
                print(f'Você acertou {cont_algarismos} algarismos!')
                cont_algarismos = 0
            else:
                print('\nVocê não acertou nenhum algarismo. continue tentando!')
            print('\n')
            print(
                f"\nSeu código é: {num1} {num2} {num3} {num4}\n\nfaltam {cont} tentativas\n")
    else:
        print(f"acabaram as tentativas\n")
        print('Você não consguiu acertar!\n')
        print(f"O código era {numero_ficticio}\n")
# vendo se o jogador quer jogar mais uma vez dps de ter acabado as tentativas ou ter ganhado o jogo
    if (cont < 1):
        more1 = int(input("jogar mais uma vez?? 1=SIM E 0=NÃO \n==>"))
        if (more1 == 1):
            num_de_jogadas += 1
            cont = 10
            cont_tentativas = 0
            cont_algarismos = 0
        elif (more1 == 2):
            num_de_jogadas = 0
else:
    print("fim de jogo")

