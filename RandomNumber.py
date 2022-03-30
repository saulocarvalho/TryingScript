import random
stop = "nao"
continua = "sim"
#counter = 0

print ('Digite SIM se deseja continuar, caso contrario digite NAO')

while True:
    resposta = input("Deseja continuar?").lower() #Lower é interessante, pois indepente de lowercase ou uppercase, ele transforma em lower case, deixando assim mais fácil e lógico
#counter = counter + 1 // O modo de usar counter é interessante caso eu queira contar as repetições para parada do código
    if resposta == stop:
        print ("obrigado!")
        break
    if resposta == continua:
        for _ in range (1):
                value = random.randint(0,21) #randint gera números inteiros 
                print(value)
    if resposta != continua:
        print ("Por favor insira um valor valido")

#Testar com pysimpleguy
