quantVotos_X = 0
quantVotos_Y = 0
quantVotos_Z = 0
quantVotos_B = 0
quantVotos_N = 0

while True:

    try:
        print('=======Votações 2022=======')
        print('889 - Candidato_X \n847 - Candidato_Y \n515 - Candidato_Z \n0 - Branco\n')
        voto = int(input('Qual candidato deseja votar? '))

        if(voto == 889):
            quantVotos_X = quantVotos_X + 1
        elif(voto == 847):
            quantVotos_Y = quantVotos_Y + 1
        elif(voto == 515):
            quantVotos_Z = quantVotos_Z + 1
        elif(voto == 0):
            quantVotos_B = quantVotos_B + 1
        else:
            quantVotos_N = quantVotos_N + 1
        
        nulo = quantVotos_B + quantVotos_N

        opcao = int(input('\nDeseja finalizar as eleições? \n1 - SIM\n2 - NÃO \n'))
        if(opcao == 1):
            break
        elif(opcao == 2):
            continue
        else:
            print('Opção inválida, escolha uma opção válida!')
            while opcao != 1 and opcao != 2:
                opcao = int(input('\nDeseja finalizar as eleições? \n1 - SIM\n2 - NÃO \n'))

    except Exception as erro:
        print('\n\033[0;31mOpção inválida. Tente novamente!\n\033[m')

maior = 0
if(quantVotos_X >= maior):
    maior = quantVotos_X
    vencedor = 'Candidato_X'
elif(quantVotos_Y >= maior):
    maior = quantVotos_Y
    vencedor = 'Candidato_Y'
elif(quantVotos_Z >= maior):
    maior = quantVotos_Z
    vencedor = 'Candidato_Z'

print('\nVotação finalizada\n')
if(maior == quantVotos_X == quantVotos_X == quantVotos_Y == quantVotos_Z):
    print(f'Empate entre os Candidato_X, Candidato_Y, Candidato_Z')
elif(maior == quantVotos_Y == quantVotos_Z):
    print(f'A votação deu empate entre Candidato_Y e Candidato_Z')
elif(maior == quantVotos_X == quantVotos_Z):
    print(f'A votação deu empate entre Candidato_X e Candidato_Z')
elif(maior == quantVotos_X == quantVotos_Y):
    print(f'A votação deu empate entre Candidato_X e Candidato_Y')
else:
    print(f'O candidato vencedor foi o {vencedor} com {maior} votos. ')

print(f'O candidato_X recebeu {quantVotos_X} votos. ')
print(f'O candidato_Y recebeu {quantVotos_Y} votos. ')
print(f'O candidato_Z recebeu {quantVotos_Z} votos. ')
print(f'Votos Brancos ou Nulos foram {nulo} votos. ')

