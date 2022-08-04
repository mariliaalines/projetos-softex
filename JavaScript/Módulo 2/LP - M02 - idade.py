
while True:

    try:

        print("=======Informe seus dados=======\n")
        nome = str(input("Nome: "))

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
            print(f"\nNome: {nome}\nIdade: {idade} anos")
            print("\nPrograma Finalizado")

            break
        else:
            raise Exception("\nData inválida, digite uma data válida!")
    except:
        print("\nErro! Preencha os campos corretamente!")




   