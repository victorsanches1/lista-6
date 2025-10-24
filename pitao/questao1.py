l= int(input("insira o numero de linhas: "))
c= int(input("insira o numero de Colunas: "))

matriz = []
for l in range(l):
    temperaturas = []
    for j in range (c):
        temp= int(input(f'insira as temperaturas: [{l + 1}] { j + 1}]: '))
        temperaturas.append(temp)
    matriz.append(temperaturas)

def calcularmedia(matriz):
    medias = []
    for t in matriz:
        media = sum(t)/ len(t)
        medias.append(media)
        return medias
    
md=calcularmedia(matriz)

print('\n=== Media das temperaturas ===')
for i, m in enumerate(md):
    print(f'{i+1} - {m:.1f}')