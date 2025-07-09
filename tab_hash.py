class TabelaHash:
    
    def __init__(self, lot, funcao_hash):
        """
        Construtor da tabela hash.
        lot= tamanho da tabela
        funcao_hash= usada para calcular os indices 
        """
        self.lot = lot
        self.tabela = [[] for _ in range(lot)] 
         # Encadeamento (lista de listas)
         # cada lot da tabela é uma list(lista)
         # começa com todos os list vazio
         
        self.funcao_hash = funcao_hash

    def insert(self, chave, data):
        """
        Insere um novo elemento na tabela hash se não for duplicado.
        key: chave de busca
        data: dado a ser armazenado
        return: True se inserido, False se duplicata
        """
        ini= self.funcao_hash(chave) % self.lot
        #aplica função de hash à chave 
        # usa % para garantir que o itém caia dentro do tamanho da tabela 
        lista = self.tabela[ini] 
        #acessa a lista no índice calculado

        # Verificar se já existe (duplicata)
        for indicacao_chave, _ in lista:
            if indicacao_chave == chave:
                return False  # se tiver duplicada não inserir novamente

        lista.append((chave, data))#se não for duplicada adiciona um par (chave, dado )
        return True  

    def search(self, chave):
        """
        Busca um elemento na tabela hash pela chave.
        
        """
        ini = self.funcao_hash(chave) % self.lot #calcula um índice buscando onde a chave deve estar 
        lista = self.tabela[ini]#acessa onde pode estar o índice 

        for indicacao_chave, indicacao_data in lista:
            #acessa os elementos se encontrar a chave, retorna o dado associado 
            if indicacao_chave == chave:
                return indicacao_chave
        
        return None   # Chave não encontrada
       

    def remove(self,chave):
        """
        Remove um elemento da tabela  chave.
        """
        ini= self.funcao_hash(chave) % self.lot
        #calcula o índice onde  a chave deve estar
        lista = self.tabela[ini]
        #acessa a lista onde pode estar o  item 

        for i, (indicacao_chave, _) in enumerate(lista):
            #se encontrar a chave, remove tal elemento dela usando a função del 
            # retorna verdadeiro indicando que a remoção foi feita 
            if indicacao_chave == chave:
                del lista [i]
                return True  
        
        return False # caso a chave não seja encontrada 
        
    def __getitem__(self, lista):
        """
        Permite acessar as listas  diretamente pelo índice.
        index: posição da tabela hash
        return: lista de elementos na lista 
        """
        return self.tabela[lista]#retorna a lista de elementos no índice especificado

    def __str__(self):
        """
        define como a tabela será impressa 
        """
        return str(self.tabela)
    #reotna a tabela como uma string, amostra todas as listas e seus conteúdos

    