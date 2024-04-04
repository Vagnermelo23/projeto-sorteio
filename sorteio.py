import random

def sorteio():
    try:
        # Gere um número aleatório entre 1 e 100
        a = random.randint(1, 100)
    
        # Obtenha a entrada do usuário para o número de números aleatórios
        num_numeros_aleatorios = int(input("Quantos números aleatórios você deseja? "))
    
        # Gere o número especificado de números aleatórios
        numeros_aleatorios = [random.randint(1, 100) for i in range(num_numeros_aleatorios)]
    
        # Imprima o resultado
        print(f"números aleatórios fornecida é: {numeros_aleatorios}")
    except ValueError:
        print("digite um numero")


# Chame a função
sorteio()
