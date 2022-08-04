
def menu():
    print("=======CALCULADORA=======")
    print("1 - Soma \n2 - Subtração \n3 - Multiplicação \n4 - Divisão \n0 - Sair\n")

def calculadora(opcao, num1, num2): 
    if (opcao == 1): return num1 + num2
    elif(opcao == 2): return num1 - num2
    elif(opcao == 3): return num1 * num2
    elif(opcao == 4): return num1 / num2

while True:
    menu()
    opcao = int(input("Qual operação deseja realizar? "))
    if(opcao == 0):
        print("\nPrograma Finalizado")
        break
    elif(opcao < 0 or opcao > 4):
        print("\nEssa opção não existe, tente novamente!")
        
    elif(1 <= opcao <= 4):
        num1 = float(input("Insira o 1° número: "))
        num2 = float(input("Insira o 2° número: "))
        operacao = calculadora(opcao, num1, num2)
        print(f"Resultado = {operacao}")