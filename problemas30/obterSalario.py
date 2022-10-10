import csv

nomeArq = input("Entre com o nome do Arquivo (sem .csv): ")

try:
    with open("./novo.csv","w") as arqN:    
        w = csv.writer(arqN)
        w.writerow(['Matricula','Salario','Data'])
        with open("./"+nomeArq+".csv","r") as arqA:
            c = csv.reader(arqA)
            for m,s,d,e in c:
                if s != "Salario":
                    if float(s) > 5000:
                        w.writerow([m,s,d])
except Exception as e:
    print("Erro: ",e)                    