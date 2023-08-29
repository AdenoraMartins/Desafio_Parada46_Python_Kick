nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

def decadas (idade):
    print (f"{nome}, você já viveu aproximadamente {(idade // 10)} décadas!")

decadas(idade)
