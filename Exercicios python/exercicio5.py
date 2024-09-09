contador_positivos = 0

while True:
   
    numero = float(input("Digite um número (ou um número negativo para sair): "))
   
    if numero < 0:
        break
    
    contador_positivos += 1

print(f"A quantidade de números positivos digitados foi: {contador_positivos}.")
