from divisao import hash_dobra  
from tab_hash import TabelaHash
from divisao import hash_simples
from deduplicate import deduplicar_csv
while True:
    key = input("Digite a chave numérica para calcular o hash (ou 'sair' para encerrar): ")

    if key.lower() == 'sair':
        print("Programa encerrado.")
        break
    try:
     resultado = hash_dobra(key)
     print(f"O valor do hash para a chave '{key}' é: {resultado}")
   
       
    except ValueError as e:
        print(e)

    print("-" * 40)

if __name__ == "__main__":
    # Cria a tabela hash com tamanho 5 e a função hash_simples
    tabela = TabelaHash(5, hash_simples)

    
    print("Inserindo elementos...")
    print(tabela.insert('5','a'))  # retornar True
    print(tabela.insert('21','b'))  # retornar True
    print(tabela.insert('5','c'))  #  deve retornar False
    print(tabela.insert('8','d'))
    print(tabela.insert('31','e'))

    print("\nTabela atual:")
    print(tabela)

    
    print("\nBuscando elementos...")
    print("Busca chave 5:", tabela.search('5'))  
    print("Busca chave 8:", tabela.search('8')) 
    print("Busca chave 31:", tabela.search('31'))  
    print("Busca chave 21:", tabela.search('21')) 
    print("Busca chave 33:", tabela.search('33'))  #  deve retornar None

    
    print("\nRemovendo elementos...")
    print("Remover chave 5:", tabela.remove('5'))  # Deve retornar True
    print("Remover chave 33:", tabela.remove('33'))  #none (chave inexistente)

    print("\nTabela final:")
    print(tabela)

deduplicar_csv(
   "dados/customers-10000.csv",
   "dados/customers-10000-deduplicado.csv",
   coluna_chave="Email",
   funcao_hash="dobra",
   tamanho_tabela=10000
)

