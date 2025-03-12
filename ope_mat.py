# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.

numb1 = int(input("Digite o primeiro número: "))
numb2 = int(input("Digite o segundo número: "))

operacao = input ("Digite a operação desejada: (+, -, *, /)")

if operacao == "+":
    print(numb1 + numb2)
elif operacao == "-":
    print(abs(numb1 - numb2))
elif operacao == "*":
    print(numb1 * numb2)
elif operacao == "/":
    print(numb1 / numb2)
else:
    print("Operação inválida")
