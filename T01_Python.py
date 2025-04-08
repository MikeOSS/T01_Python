import random

# gerando número aleatório
numero_ficticio = random.randint(1000, 9999)
# divisão dos números:
milhar = numero_ficticio // 1000
cent = (numero_ficticio % 1000) // 100
dez = (numero_ficticio % 100) // 10
unidade = (numero_ficticio) % 10

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


# contadores
cont = 10
cont_tentativas = 0
cont_algarismos = 0

while num_de_jogadas > 0:
    while (cont > 0):
        # contando as tentativas:
        tentativa = int(input(f'digite sua tentativa de código: '))
        # Tentativa de fazer o programa não reconhecer numeros fora do escopo e letras digitadas!

        while (tentativa < 1000 or tentativa > 9999):
            print('\t\t\t A T E N Ç Ã O!!\n')
            print('\t\tDigite um número válido entre 1000 e 9999!!\n')
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
        print("\nSeu código é: ", end="")
        if milhar == t_milhar:
            print(milhar, end=" ")
            cont_algarismos += 1
        else:
            print("_", end=" ")

        if cent == t_centena:
            print(cent, end=" ")
            cont_algarismos += 1
        else:
            print("_", end=" ")

        if dez == t_dezena:
            print(dez, end=" ")
            cont_algarismos += 1
        else:
            print("_", end=" ")

        if unidade == t_unidade:
            print(unidade)
            cont_algarismos += 1
        else:
            print("_")
        # contador de numeros faltantes
        cont_falt = 4 - cont_algarismos
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
            # verificando se o usuário acertou algum algarismo
            if (cont_algarismos > 0):
                print(f'\nVocê acertou {cont_algarismos} algarismos!\n')
                cont_algarismos = 0
            else:
                print('\nVocê não acertou nenhum algarismo. continue tentando!')
        if cont > 5:
            print(
                f"faltam {cont_falt} algarismos e {cont} tentativas\n")
        elif cont <= 5:
            # resuldado com dicas
            if milhar != t_milhar:
                if milhar < 5:
                    print("\no primeiro dígito é menor ou igual a 5")
                else:
                    print("\no primeiro dígito é maior ou igual a 5")

            if cent != t_centena:
                if cent >= 5:
                    print("\no segundo dígito é maior que 5")
                else:
                    print("\no segundo dígito é maior ou igual a 5")

            if dez != t_dezena:
                if dez < 5:
                    print("\no terciro dígito é menor que 5")
                else:
                    print("\no terceiro dígito é maior ou igual a 5")

            if unidade != t_unidade:
                if unidade < 5:
                    print("\no quarto dígito é menor que 5")
                else:
                    print("\no quarto dígito é maior ou igual a 5")
            print('\n')
            print(
                f"faltam {cont_falt} algarismos e {cont} tentativas\n")

    else:
        print(f"acabaram as tentativas\n")
        print('Você não consguiu acertar!\n')
        print(f"O código era {numero_ficticio}\n")
# vendo se o jogador quer jogar mais uma vez dps de ter acabado as tentativas ou ter ganhado o jogo
    if (cont < 1):
        more1 = int(input("jogar mais uma vez?? 1=SIM E 2=NÃO \n==>"))
        if (more1 == 1):
            num_de_jogadas += 1
            cont = 10
            cont_tentativas = 0
            cont_algarismos = 0
        elif (more1 == 2):
            num_de_jogadas = 0
else:
    print("fim de jogo")
