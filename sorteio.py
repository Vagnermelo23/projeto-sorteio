import random

def sorteio():
    try:
    
        a = random.randint(1, 100)
    
        num_numeros_aleatorios = int(input("Quantos números aleatórios você deseja? "))
    
        numeros_aleatorios = [random.randint(1, 100) for i in range(num_numeros_aleatorios)]

        print(f"números aleatórios fornecida é: {numeros_aleatorios}")
    except ValueError:
        print("digite um numero")



sorteio()
