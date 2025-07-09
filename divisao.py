

def divisão_hash(key):
    """
    Função de hash por divisão simples.
    """
    return int(key)

def hash_dobra(key):
    """
    Função de hash por dobra.
  soma as duas metades da chave numérica 
    """
    key_str = str(key)
    # converte a chave para string 
    if not key_str.isdigit():
        print(f"chave inválida para metade_hash: '{key}'")
        return 0
    mid = len(key_str) // 2
    #calcula o ponto medio da chave
    if len(key_str) % 2 == 0:
        # se par somar todos os digitos 
        part1 = int(key_str[:mid])
        part2 = int(key_str[mid:])
        #exemplo "487900" part1= 487 part2=900 separa  de forma homogenea em pares iguais 
    else:
        # Se impar...
        part1 = int(key_str[:mid])
        part2 = int(key_str[mid:])
    #exemplo "48790" part1=48 part2=790 maior parte na segunda parte
    return part1 + part2

def hash_simples(chave):
        return int(chave) 

