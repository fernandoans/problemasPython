# Nota Fiscal
print("=" * 50)
print("\t\tEmpresa XPTO Limitada")
print("\t\tRua dos Bobos - Nº 0")
print("\t\tQualquer uma")
print("-" * 50)

produtos = {
    "Impressora":220.00,
    "Computador":2300.00,
    "Mouse USB":50.00
}
print("Produto\t\t\t Preço")
total = 0.0
for produto in produtos.keys():
    print(produto, "\t\t", produtos[produto])
    total += produtos[produto]

print("-" * 50)
print("Total da Nota: \t", total)