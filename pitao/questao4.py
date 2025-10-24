estoque = []

for produto in range(4):
    print(f"\nProduto {produto + 1}:")
    lojas = []
    for loja in range(3):
        quantidade = int(input(f"  Digite a quantidade na Loja {loja + 1}: "))
        lojas.append(quantidade)
    estoque.append(lojas)

print("\n Estoque (Produtos x Lojas):")
for produto in range(4):
    print(f"Produto {produto + 1}: {estoque[produto]}")

print("\n Total de cada produto:")
for produto in range(4):
    total = sum(estoque[produto])
    print(f"Produto {produto + 1}: {total} unidades no total")
