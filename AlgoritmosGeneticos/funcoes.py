import random

def gene_cb():
    """Gera um gene válido para o problema das caixas binárias.

    Retorna:
        Um valor zero ou um.
    """
    lista = [0, 1]
    gene = random.choice(lista)
    return gene

def gene_cnb(valor_max_caixa):
    """Gera um gene válido para o problema das caixas não-binárias.
    
    Argumentos:
        valor_max_caixa: valor máximo que a caixa pode assumir.

    Retorna:
        Um valor entre 0 e o "valor_max_caixa" (incluso).
    """
    gene = random.randint(0, valor_max_caixa)
    return gene

def gene_letra(letras):
    """Sorteia uma letra.
    
    Argumentos:
      letras: letras possíveis de serem sorteadas.
      
    Retorna:
      Uma letra dentro das possíveis de serem sorteadas.
    """
    letra = random.choice(letras)
    return letra

def individuo_cb(n):
    """Gera um indivíduo para o problema das caixas binárias.

    Argumentos:
        n: número de genes do indivíduo.

    Retorna:
        Uma lista com n genes. Cada gene é um valor zero ou um.
    """
    individuo = []
    for i in range(n):
        gene = gene_cb()
        individuo.append(gene)
    return individuo

def individuo_cnb(numero_genes, valor_max_caixa):
    """Gera um indivíduo válido para o problema das caixas não-binárias.
    
    Argumentos:
        numero_genes: número de genes na lista que representa o indivíduo.
        valor_max_caixa: valor máximo que a caixa pode assumir.
        
    Returna:
        Uma lista que representa um indivíduo válido para o problema das caixas não-binárias.
    """
    individuo = []
    for _ in range(numero_genes):
        gene = gene_cnb(valor_max_caixa)
        individuo.append(gene)
    return individuo

# NOVIDADE
def individuo_senha(tamanho_senha, letras):
    """Cria um candidato para o problema da senha.
    
    Argumentos:
      tamanho_senha: inteiro representando o tamanho da senha.
      letras: letras possíveis de serem sorteadas.
      
    Retorna:
      Uma lista com n letras
    """

    candidato = []

    for n in range(tamanho_senha):
        candidato.append(gene_letra(letras))

    return candidato

def populacao_cb(tamanho, n):
    """Cria uma população no problema das caixas binárias.
    
    Argumentos:
        tamanho: tamanho da população.
        n: número de genes do indivíduo.
    
    Retorna:
        Uma lista onde cada item é um indivíduo. Um indivíduo é uma lista com n genes.
    """
    populacao = []
    for _ in range(tamanho):
        populacao.append(individuo_cb(n))
    return populacao

def populacao_cnb(tamanho, n_genes, valor_max_caixa):
    """Cria uma população no problema das caixas não-binárias.
    
    Argumentos:
      tamanho: tamanho da população.
      n_genes: número de genes do indivíduo.
      valor_max_caixa: maior número inteiro possível em uma caixa.
      
    Retorna:
      Uma lista onde cada item é um indivíduo. Um indivíduo é uma lista com `n_genes` genes.
    """
    populacao = []
    for _ in range(tamanho):
        populacao.append(individuo_cnb(n_genes, valor_max_caixa))
    return populacao

def populacao_inicial_senha(tamanho, tamanho_senha, letras):
    """Cria população inicial no problema da senha
    
    Argumentos
      tamanho: tamanho da população.
      tamanho_senha: inteiro representando o tamanho da senha.
      letras: letras possíveis de serem sorteadas.
          
    Retorna:
      Uma lista com todos os indivíduos da população no problema da senha.
    """
    populacao = []
    for n in range(tamanho):
        populacao.append(individuo_senha(tamanho_senha, letras))
    return populacao
    
def selecao_roleta_max(populacao, fitness):
    """ Seleciona indivíduos de uma população usando o método da roleta.
    
    Nota: apenas funciona para problemas de maximização.
    
    Argumentos:
        populacao: lista com todos os indivíduos da população.
        fitness: lista com o valor da função objetiva dos indivíduos da população.
    
    Retorna:
        População dos indivíduos selecionados.
    """
    populacao_selecionada = random.choices(populacao, weights=fitness, k=len(populacao))
    return populacao_selecionada

def selecao_torneio_min(populacao, fitness, tamanho_torneio=3):
    """Faz a seleção de uma população usando torneio.
    
    Nota: da forma que está implementada, só funciona em problemas de minimização.
    Argumentos:
      populacao: população do problema.
      fitness: lista com os valores de fitness dos indivíduos da população.
      tamanho_torneio: quantidade de indivíduos que batalham entre si
      
    Reto\rna:
      Indivíduos selecionados. Lista com os indivíduos selecionados com mesmo tamanho do argumento `populacao`.
    """
    selecionados = []

    # criamos essa variável para associar cada individuo com seu valor de fitness
    par_populacao_fitness = list(zip(populacao, fitness))

    # vamos fazer len(populacao) torneios! Que comecem os jogos!
    for _ in range(len(populacao)):
        combatentes = random.sample(par_populacao_fitness, tamanho_torneio)

        # é assim que se escreve infinito em python
        minimo_fitness = float("inf")

        for par_individuo_fitness in combatentes:
            individuo = par_individuo_fitness[0]
            fit = par_individuo_fitness[1]

            # queremos o individuo de menor fitness
            if fit < minimo_fitness:
                selecionado = individuo
                minimo_fitness = fit

        selecionados.append(selecionado)

    return selecionados

def cruzamento_ponto_simples(pai, mae):
    """Operador de cruzamento de ponto simples.
    
    Argumentos:
        pai: uma lista representando um indivíduo.
        mae: uma lista representando um indivíduo.
        
    Retorna:
        Duas listas, sendo que cada uma representa um filho dos pais que foram os argumentos.
    """
    ponto_de_corte = random.randint(1, len(pai)-1)
    
    filho1 = pai[:ponto_de_corte] + mae[ponto_de_corte:]
    filho2 = mae[:ponto_de_corte] + pai[ponto_de_corte:]
    return filho1, filho2

def mutacao_cb(individuo):
    """Realiza a mutação de um gene no problema das caixas binárias.
    
    Argumentos: 
        individuo: uma lista representado um indivíduo no problema das caixas binárias.
        
    Retorna:
        Um indivíduo com um gene mutado.
    """
    gene_a_ser_mutado = random.randint(0, len(individuo)-1)
    individuo[gene_a_ser_mutado] = gene_cb()
    return individuo

def mutacao_cnb(individuo, valor_max_caixa):
    """Realiza a mutação do indivíduo.
    
    Argumentos:
        individuo: indivíduo que deve sofrer a mutação.
        valor_max_caixa: valor máximo que a caixa pode asssumir.
        
    Retorna:
        Indivíduo que sofreu a mutação.
    """
    gene_a_ser_mutado = random.randint(0, len(individuo)-1)
    individuo[gene_a_ser_mutado] = gene_cnb(valor_max_caixa)
    return individuo

def mutacao_senha(individuo, letras):
    """Realiza a mutação de um gene no problema da senha.
    
    Argumentos:
      individuo: uma lista representado um indivíduo no problema da senha
      letras: letras possíveis de serem sorteadas.
      
    Retorna:
      Um individuo (senha) com um gene mutado.
    """
    gene = random.randint(0, len(individuo) - 1)
    individuo[gene] = gene_letra(letras)
    return individuo

def funcao_objetiva_cb(individuo):
    """Computa a função objetiva no problema das caixas binárias.

    Argumentos:
        individuos: lista contendo os genes das caixas binárias.

    Retorna:
        Um valor representando a soma dos genes do indivíduo.
    """
    return sum(individuo)

def funcao_objetiva_cnb(individuo):
    """Calcula a fitness do indivíduo para o problema das caixas não-binárias.
    
    Argumentos:
        individuo: lista que representa um indivíduo dentro do problema das caixas não-binárias.
        
    Retorna:
        Um valor que presenta o fitness do indivíduo.
    """
    fitness = sum(individuo)
    return fitness

def funcao_objetiva_senha(individuo, senha_verdadeira):
    """Computa a função objetiva de um indivíduo no problema da senha.
    
    Argumentos:
        individuo: lista contendo as letras da senha.
        senha_verdadeira: a senha que você está tentando descobrir.
        
    Retorna:
        A "distância" entre a senha proposta e a senha verdadeira. Essa distância é medida letra por letra. Quanto mais distante uma letra for da que deveria ser, maior é essa distância.
    """
    diferenca = 0
    
    for letra_candidato, letra_oficial in zip(individuo, senha_verdadeira):
        diferenca = diferenca + abs(ord(letra_candidato) - ord(letra_oficial))

    return diferenca

def funcao_objetiva_pop_cb(populacao):
    """Calcula a função objetiva para todos os membros de uma população.
    
    Argumentos:
        populacao: lista com todos os indivíduos da população.
    
    Retorna:
        Lista de valores representando a fitness de cada indivíduo da população.
    """
    fitness = []
    for individuo in populacao:
        fobj = funcao_objetiva_cb(individuo)
        fitness.append(fobj)
    return fitness

def funcao_objetiva_pop_cnb(populacao):
    """Calcula o fitness da população completa.
    
    Argumentos:
        populacao: lista com todos os indivíduos da população.
        
    Retorna:
        Uma lista com o fitness de cada indivíduo em ordem.
    """
    fitness_pop = []
    for individuo in populacao:
        fitness_ind = funcao_objetiva_cnb(individuo)
        fitness_pop.append(fitness_ind)
    return fitness_pop

def funcao_objetiva_pop_senha(populacao, senha_verdadeira):
    """Computa a funcao objetivo de uma populaçao no problema da senha.
    
    Argumentos:
      populacao: lista com todos os individuos da população.
      senha_verdadeira: a senha que você está tentando descobrir.
      
    Retorna:
      Lista contendo os valores da métrica de distância entre senhas.
    """
    resultado = []

    for individuo in populacao:
        resultado.append(funcao_objetiva_senha(individuo, senha_verdadeira))

    return resultado