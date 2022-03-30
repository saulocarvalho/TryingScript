import random

for _ in range (1):
    valorGerado = random.randint(0,21)
    
    while True:
        try:
            resposta = int(input("Adivinhe qual o valor gerado: "))
        
            if resposta == valorGerado:
                print ("Parabens, voce acertou!!!")
                break
            if resposta < valorGerado:
                print ("Chutou baixo")
            if resposta > valorGerado:
                print ("Chutou alto")
        except ValueError: #trata o erro do int(input("texto")) // Interessante
            print("Por favor apenas numeros inteiros")

#Testar com pysimpleguy
