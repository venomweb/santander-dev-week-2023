# @title Extract + Transform
import random
import pandas as pd

# EXTRACT
users = [
    {'id': 137, 'nome': 'Carlos Mendes', 'saldo': 0, 'mensagem': []},
    {'id': 842, 'nome': 'Juliana Ribeiro', 'saldo': 0, 'mensagem': []},
    {'id': 59, 'nome': 'Fernando Alves', 'saldo': 0, 'mensagem': []},
    {'id': 913, 'nome': 'Mariana Costa', 'saldo': 0, 'mensagem': []},
    {'id': 276, 'nome': 'Ricardo Nogueira', 'saldo': 0, 'mensagem': []},
    {'id': 488, 'nome': 'Patrícia Lima', 'saldo': 0, 'mensagem': []},
    {'id': 721, 'nome': 'Bruno Carvalho', 'saldo': 0, 'mensagem': []},
    {'id': 305, 'nome': 'Aline Souza', 'saldo': 0, 'mensagem': []},
    {'id': 664, 'nome': 'Diego Fernandes', 'saldo': 0, 'mensagem': []},
    {'id': 198, 'nome': 'Camila Rocha', 'saldo': 0, 'mensagem': []},
]

# TRANSFORM
for user in users:
# Gera um saldo ficctício para testes
    user['saldo'] = round(random.uniform(0, 50), 2)
    # Vai checar se o usuário tem um saldo mínimo e aloca a mensagem adequada
    if user['saldo'] <= 24.45:
        user['mensagem'].append("Saldo Insuficiente")
    else:
        user['mensagem'].append("Negociação Liberada")

# Converte para DataFrame
df = pd.DataFrame(users)

# Garante 2 casas decimais
df['saldo'] = df['saldo'].map(lambda x: f"{x:.2f}")

# Exporta para CSV
df.to_csv('saldo_atualizado.csv', sep=';', index=False, encoding='utf-8')