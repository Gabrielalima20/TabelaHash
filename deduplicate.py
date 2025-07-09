import pandas as pd
import os
from tab_hash import TabelaHash
from divisao import hash_simples, hash_dobra

#Dicionario pra definir parâmetros
FUNCOES_HASH = {
    "simples":hash_simples,
    "dobra":hash_dobra
}

def deduplicar_csv(arquivo_entrada, arquivo_saida=None, coluna_chave=None, funcao_hash="simples", tamanho_tabela=1000):
    """
    Remove duplicatas de um CSV usando Tabela Hash.
    :param arquivo_entrada: Caminho do arquivo CSV original
    :param arquivo_saida: Caminho para salvar o CSV deduplicado
    :param coluna_chave: Nome da coluna usada como chave
    :param funcao_hash: Nome da função de hash ('simples' ou 'dobra')
    :param tamanho_tabela: Tamanho da Tabela Hash
    """
    #Gerar nome automatico se arquivo_saida não for definido
    if arquivo_saida is None:
        nome_base, ext = os.path.splitext(arquivo_entrada)
        arquivo_saida = f"{nome_base}-dedup{ext}"
    #Definir funcao hash utilizada
    if funcao_hash not in FUNCOES_HASH:
        raise ValueError(f"Função de hash '{funcao_hash}' inválida. Escola entre:{list(FUNCOES_HASH.keys())}")
    
    hash_escolhido = FUNCOES_HASH[funcao_hash]


    # Verificação da função de hash
    try:
        _ = hash_escolhido("teste") % tamanho_tabela
    except Exception as e:
        raise ValueError(f"A função de hash '{funcao_hash}' falhou ao processar uma chave: {e}")

    # Verificação da classe TabelaHash
    if not hasattr(TabelaHash, 'insert'):
        raise TypeError("Classe TabelaHash não possui método 'insert'.")

    # Leitura do CSV
    try:
        df = pd.read_csv(arquivo_entrada)
    except Exception as e:
        raise IOError(f"Erro ao ler o arquivo CSV: {e}")

    if coluna_chave not in df.columns:
        raise TypeError(f"Coluna '{coluna_chave}' não encontrada no arquivo")
    tabela = TabelaHash(tamanho_tabela, hash_escolhido)
    linhas_unicas = []

    # Eliminar Duplicatas
    for i, linha in df.iterrows():
        #transforma chave em string
        chave = str(linha[coluna_chave])
        #Inserir a chave na tabela hash
        if tabela.insert(chave, linha.to_dict()):
            #Se for unica insere na lista
            linhas_unicas.append(linha)
    
    pd.DataFrame(linhas_unicas).to_csv(arquivo_saida,index=False)
    print(f"Arquivo deduplicado salvo em: {arquivo_saida}")

