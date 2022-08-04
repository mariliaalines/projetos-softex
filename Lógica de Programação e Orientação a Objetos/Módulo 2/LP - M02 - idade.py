
while True:

    try:

        print("=======Informe seus dados=======\n")
        nome = input("Nome: ")

        if(nome == ''):
            print("\033[0;31mErro! O campo Nome deve ser preenchido.\033[m")
            continue

        print("Data de Nascimento")
        dia_nasc = int(input("Dia: "))
        mes_nasc = int(input("Mês: "))
        ano_nasc = int(input("Ano: "))

        if( 2021 >= ano_nasc >= 1922):

            print("\nData Atual")
            dia_atual = int(input("Dia: "))
            mes_atual = int(input("Mês: "))
            ano_atual = int(input("Ano: "))
            idade = ano_atual - ano_nasc

            if(mes_nasc > mes_atual or (mes_nasc == mes_atual and dia_nasc > dia_atual)):
                idade = idade - 1

            print("\n=======Dados Informados=======")
            print(f"\nNome: {nome}\nIdade: {idade} anos")
            print("\nPrograma Finalizado")

            break
    except:
        print("\033[0;31m\nErro! Informe uma data válida!\033[m")




   