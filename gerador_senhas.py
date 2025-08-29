"""
Gerador de Senhas Fortes
Autor: João (JoZoEzUd)
Licença: MIT
"""

import random
import string

def gerar_senha(tamanho=12, proibidos=''):
    letras = string.ascii_letters
    numeros = string.digits
    especiais = string.punctuation

    for c in proibidos:
        letras = letras.replace(c, '')
        numeros = numeros.replace(c, '')
        especiais = especiais.replace(c, '')

    todos = letras + numeros + especiais
    if not todos:
        raise ValueError("Nenhum caractere disponível após remover os proibidos.")

    senha = [
        random.choice(letras) if letras else random.choice(todos),
        random.choice(numeros) if numeros else random.choice(todos),
        random.choice(especiais) if especiais else random.choice(todos)
    ]
    senha += [random.choice(todos) for _ in range(tamanho - len(senha))]
    random.shuffle(senha)
    return ''.join(senha)

def menu():
    print("=" * 40)
    print("🔐 GERADOR DE SENHAS SEGURAS 🔐")
    print("=" * 40)
    try:
        tamanho = int(input("Digite o tamanho da senha (mínimo 6): "))
        if tamanho < 6:
            tamanho = 6
    except ValueError:
        print("Entrada inválida. Usando tamanho padrão de 12.")
        tamanho = 12

    proibidos = input("Digite os caracteres que deseja excluir (ou deixe vazio): ")
    senha = gerar_senha(tamanho, proibidos)
    print("\nSua senha gerada é:\n")
    print(senha)
    print("\nCopie e use sua senha com segurança!")

if __name__ == "__main__":
    menu()
