import math

def SOMA(x, y):
        resultado = float(x) + float(y)
        print(f"O resultado da soma de {x} + {y} é : {resultado}")


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

    escolha = input("Qual operação deseja realizar?")

    print("=================================")

    if escolha == "0":
        print("Saindo...")
        break
    elif escolha == "1":
        x = (input("Digite o Primeiro Número: "))
        y = (input("Digite o Segundo Número: "))
        SOMA(x, y)

    print("=================================")