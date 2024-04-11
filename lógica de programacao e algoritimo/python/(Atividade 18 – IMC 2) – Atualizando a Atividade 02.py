altura = float(input("digite sua altura: "))
peso = float(input("digite seu peso:"))
imc = peso / (altura + altura)
imc = round(imc, 2)
print(" o imc é de {:.2f}".format(imc))
if imc <= 18.4:
    print("abaixo do peso")
elif imc <= 24.9:
    print("peso normal")
elif imc <= 29.9:
    print("sobrepeso")
elif imc <= 34.9:
    print("obesidade grau 1")
elif imc <= 39.9:
    print("obesidade grau 2")
elif imc >= 40.0:
    print("obesidade grau 3")