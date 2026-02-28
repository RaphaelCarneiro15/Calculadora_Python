import math

def SOMA(x, y):
    resultado = float(x) + float(y)
    print(f"O resultado da soma de {x} + {y} é : {resultado}")

def SUB(x, y):
    resultado = float(x) - float(y)
    print(f"O resultado da subtração de {x} - {y} é : {resultado}")

def MULT(x, y):
    resultado = float(x) * float(y)
    print(f"O resultado da multiplicação de {x} * {y} é : {resultado}")

def DIV(x, y):
    resultado = float(x) / float(y)
    print(f"O resultado da divisão de {x} / {y} é : {resultado}")

def POT(x, y):
    resultado = math.pow(x, y)
    print(f"O resultado da potência de {x} elevado à {y} é: {resultado}")

def RAIZ(x):
    resultado = math.sqrt(x)
    print(f"O resultado da raiz quadrada de {x} é: {resultado}")

def FAT(x):
    resultado = math.factorial(x)
    print(f"O fatorial de {x}! é: {resultado}")

def SEN(x):
    resultado = math.sin(x)
    print(f"O seno de {x} é: {resultado}")

def COS(x):
    resultado = math.cos(x)
    print(f"O resultado do cosseno de {x} é: {resultado}")

def TAN(x):
    resultado = math.tan(x)
    print(f"O resultado da tangende de {x} é: {resultado}")



while True:
    print("=================================")
    print("====== Calculadora-Python ======")
    print("Qual operação deseja realizar?")
    print("Para SOMA digite [ 1 ]")
    print("Para SUBTRAÇÃO digite [ 2 ]")
    print("Para MULTIPLICAÇÃO digite [ 3 ]")
    print("Para DIVISÃO digite [ 4 ]")
    print("Para POTENCIAÇÃO digite [ 5 ]")
    print("Para RAIZ QUADRADA digite [ 6 ]")
    print("Para FATORIAL digite [ 7 ]")
    print("Para SENO digite [ 8 ]")
    print("Para COSSENO digite [ 9 ]")
    print("Para TANGENTE digite [ 10 ]")
    print("Para SAIR digite [ 0 ]")
    print("=================================")



    escolha = input("Qual operação deseja realizar? ")

    print("=================================")



    if escolha == "0":
        print("Saindo...")
        break

    elif escolha == "1":
        x = (input("Digite o Primeiro Número: "))
        y = (input("Digite o Segundo Número: "))
        SOMA(x, y)

    elif escolha == "2":
        x = (input("Digite o Primeiro Número: "))
        y = (input("Digite o Segundo Número: "))
        SUB(x, y)

    elif escolha == "3":
        x = (input("Digite o Primeiro Número: "))
        y = (input("Digite o Segundo Número: "))
        MULT(x, y)

    elif escolha == "4":
        x = (input("Digite o Primeiro Número: "))
        y = (input("Digite o Segundo Número: "))
        DIV(x, y)
    
    elif escolha == "5":
        x = int((input("Digite o Primeiro Número: ")))
        y = int((input("Digite o Segundo Número (potência): ")))
        POT(x, y)

    elif escolha == "6":
        x = int((input("Digite o número: ")))
        RAIZ(x)
    
    elif escolha == "7":
        x = int((input("Digite o número: ")))
        FAT(x)
        
    elif escolha == "8":
        x = int((input("Digite o número: ")))
        SEN(x)
    
    elif escolha == "9":
        x = int((input("Digite o número: ")))
        COS(x)
    
    elif escolha == "10":
        x = int((input("Digite o número: ")))
        TAN(x)
   
    else:
        print("Escolha um número da lista por favor...")
    
    print("=================================")