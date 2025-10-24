l = int(input('Insira o número de linhas: '))
c = int(input('Insira o número de colunas: '))


matriz = []
for i in range(l):
    linhas = []
    for j in range(c):
        notas = float(input(f'Insira a nota da prova [{j+1}] do aluno [{i+1}]: '))
        linhas.append(notas)
    matriz.append(linhas)


def calcularMediaAluno(matriz):
    mediaAluno = []
    for n in matriz:
        media = sum(n) / len(n)
        mediaAluno.append(media)
    return mediaAluno

def calcularMediaProva(matriz, num_linhas, num_colunas):
    mediasProva = []
    for j in range(num_colunas):
        soma_da_prova = 0
        for i in range(num_linhas):
            soma_da_prova += matriz[i][j]
        media = soma_da_prova / num_linhas
        mediasProva.append(media)
    return mediasProva

medias_alunos = calcularMediaAluno(matriz)
medias_provas = calcularMediaProva(matriz, l, c)


print("\n--- MATRIZ DE NOTAS ---")
for linha in matriz:
    print(linha)

print("\n--- MÉDIA POR ALUNO ---")
for i, m in enumerate(medias_alunos):
    print(f'Aluno {i+1}: {m:.1f}')

print("\n--- MÉDIA POR PROVA ---")
for i, m in enumerate(medias_provas):
    print(f'Prova {i+1}: {m:.1f}')
