# Qual o prato mais pedido por 'maria'?

# Quantas vezes 'arnaldo' pediu 'hamburguer'?

# Quais pratos 'joao' nunca pediu?

# Quais dias 'joao' nunca foi na lanchonete?

# hamburguer
# 1
# {'pizza', 'coxinha', 'misto-quente'}
# {'sabado', 'segunda-feira'}

import csv


def analyze_log(path_to_file):
    with open(path_to_file, "r") as file:
        fieldnames = ['nome', 'comida', 'dia']
        reader = csv.DictReader(file, fieldnames=fieldnames)
        array = []
        for row in reader:
            array.append(row)
        print(array)


analyze_log("data/orders_1.csv")
