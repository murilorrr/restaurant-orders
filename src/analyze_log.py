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
    if not path_to_file.endswith('.csv'):
        raise FileNotFoundError(f'Extensão invalida: {path_to_file}')
    try:
        with open(path_to_file, "r") as file:
            fieldnames = ['nome', 'comida', 'dia']
            reader = csv.DictReader(file, fieldnames=fieldnames)
            array = []
            for row in reader:
                array.append(row)

            prato_mais_pedido = prato_mais_pedido_por_maria(array)
            arnaldo_count = arnaldo_count_hamburguer(array)
            nao_pratos_joao = pratos_joao_nao_pediu(array)
            dias_joao_nao_foi = dias_joao_nao_foi_lanchonete(array)

        with open('data/mkt_campaign.txt', 'w') as write_file:
            write_file.write(
                f'{prato_mais_pedido}\n'
                f'{arnaldo_count}\n'
                f'{nao_pratos_joao}\n'
                f'{dias_joao_nao_foi}\n'
            )
    except FileNotFoundError:
        raise FileNotFoundError(f'Arquivo inexistente: {path_to_file}')


def prato_mais_pedido_por_maria(array):
    count = {}
    maria_orders = [row for row in array if row['nome'] == 'maria']
    max_value = maria_orders[0]['comida']
    for row in maria_orders:
        if row['comida'] not in count:
            count[row['comida']] = 1
        if row['comida'] in count:
            count[row['comida']] += 1
        if count[row['comida']] > count[max_value]:
            max_value = row['comida']
    return max_value


def arnaldo_count_hamburguer(array):
    count = 0
    for row in array:
        if row['comida'] == 'hamburguer' and row['nome'] == 'arnaldo':
            count = count + 1
    return count


def pratos_joao_nao_pediu(array):
    todos_os_pratos = set(['misto-quente', 'hamburguer', 'pizza', 'coxinha'])
    pratos_do_joao = set()
    for row in array:
        if row['nome'] == 'joao':
            pratos_do_joao.add(row['comida'])
    return todos_os_pratos.difference(pratos_do_joao)


def dias_joao_nao_foi_lanchonete(array):
    todos_os_dias = set()
    dias_do_joao = set()
    for row in array:
        todos_os_dias.add(row['dia'])
        if row['nome'] == 'joao':
            dias_do_joao.add(row['dia'])
    return todos_os_dias.difference(dias_do_joao)


analyze_log("data/orders_1.csv")
