import pandas as pd

try:
    #Leitura do conjunto de dados
    df = pd.read_csv('alunos.csv', encoding = 'utf-8', sep= ';')

    #Gerando novo valor
    media = (df["Primeira Nota"] + df["Segunda Nota"]) / 2

    #Criando nova coluna; inserindo novo valor
    df["Media"] = media

    #Definindo a situação de cada aluno(aprovado ou reprovado)
    df.loc[(df["Media"] < 7.0) | (df["Numero de Faltas"] > 5), "Situacao"] = "REPROVADO"
    df.loc[(df["Media"] >= 7.0) & (df["Numero de Faltas"] <= 5), "Situacao"] = "APROVADO"

    #Salvando novo dataframe
    situacao_df = df.to_csv('alunos_situacao.csv', encoding = 'utf-8')

    #Imprimindo dataframe
    #print(df.head())

    #O maior número de faltas
    maior_quant_faltas = df['Numero de Faltas'].max()
    #A média geral dasnotas dos alunos
    media_geral = df['Media'].median()
    #A maior média
    maior_media = df['Media'].max()

    #Mostrando na tela:
    print('-'*50)
    print(f'{"Resumo":^50}')
    print('-'*50)
    print(f'Maior número de faltas: {maior_quant_faltas}')
    print(f'Média geral: {media_geral}')
    print(f'Maior média: {maior_media}')
    print('-'*50)

except FileNotFoundError as erro:
    print('Arquivo não encontrado!')

except ValueError as erro:
    print('Argumento Inválido')

except Exception as erro:
    print('Erro inesperado!')

print('\nPrograma Finalizado')
