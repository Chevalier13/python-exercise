numero = int(input("Digite um número para exibir a tabuada: "))

print(f"Tabuada do {numero}:")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")
