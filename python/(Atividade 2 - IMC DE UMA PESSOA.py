

altura = float(input("Indique sua altura: "))
peso = float(input("Indique seu peso: "))

resultado = altura + altura
resultado_2 = resultado / peso

print(f"Seu IMC é {round(resultado_2, 3)}")

if resultado_2 >= 30:
    print("Cuidado com a sua altura!")
else:
    print("Tudo ok!")