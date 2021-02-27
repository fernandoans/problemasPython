import subprocess

process = subprocess.run('ls -lha',
                         shell=True,
                         check=True,
                         stdout=subprocess.PIPE,
                         universal_newlines=True)
output = process.stdout
print(output)

# /usr/bin/lpr

imp = subprocess.Popen("/usr/bin/lpr",
                       stdin=subprocess.PIPE,
                       stderr=subprocess.STDOUT,
                       encoding='utf8')

# Nota Fiscal
imp.stdin.write("=" * 50)
imp.stdin.write("\n\t\tEmpresa XPTO Limitada")
imp.stdin.write("\n\t\tRua dos Bobos - Nº 0")
imp.stdin.write("\n\t\tQualquer uma\n")
imp.stdin.write("-" * 50)

produtos = {
    "Impressora":220.00,
    "Computador":2300.00,
    "Mouse USB":50.00
}
imp.stdin.write("\nProduto\t\t\t Preço\n")
total = 0.0
for produto in produtos.keys():
    imp.stdin.write(produto + "\t\t" + str(produtos[produto]) + "\n")
    total += produtos[produto]

imp.stdin.write("-" * 50)
imp.stdin.write("\nTotal da Nota: \t" + str(total))