a = int(input("digite um número"))
b = input("digite outro número")
prox = a
for i in b:
    print(i, end = " ")
    
    while prox > 0:
        
        algarismo = prox % 10
        prox = prox // 10
        print(prox, end= "")
        # if (int(i)==algarismo):
        #     # print(algarismo, end = " ")