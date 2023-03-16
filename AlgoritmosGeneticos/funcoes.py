import random

def gene_cb():
    """Gera um gene válido para o problema das caixas binárias.

    Retorna:
        Um valor zero ou um.
    """
    lista = [0, 1]
    gene = random.choice(lista)
    return gene

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

def funcao_objetiva_cb(individuo):
    """Computa a função objetiva no problema das caixas binárias.

    Argumentos:
        individuos: lista contendo os genes das caixas binárias.

    Retorna:
        Um valor representando a soma dos genes do indivíduo.
    """
    return sum(individuo)

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

