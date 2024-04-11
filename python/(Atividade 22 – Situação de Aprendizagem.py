letra = 's'
while letra == 's':

    valor = float(input("Digite um número para a conversão: "))
    taxa = float(input("A taxação  atual: "))
    print ("[1] Inversão de dolar para real")
    print ("[2] Inversão de real para dolar")
    inf = float(input("Digite a alternativa escolhida: "))

    if inf == 1:
        print ("USD:", valor / taxa )
    else:
        print ("R$", taxa * valor)

    letra = input("Deseja continuar? [S/N]: ")