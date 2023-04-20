import random


def distancia_entre_dois_pontos(a, b):
    """Computa a distância Euclidiana entre dois pontos em R².

    Argumentos:
      a: lista contendo as coordenadas x e y de um ponto.
      b: lista contendo as coordenadas x e y de um ponto.

    Retorna:
      Distância entre as coordenadas dos pontos `a` e `b`.
    """

    x1 = a[0]
    x2 = b[0]
    y1 = a[1]
    y2 = b[1]

    dist = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (1 / 2)

    return dist


def cria_cidades(n):
    """Cria um dicionário aleatório de cidades com suas posições (x,y).

    Argumentos:
      n: inteiro positivo; o número de cidades que serão visitadas pelo caixeiro.

    Retorna:
      Um dicionário contendo o nome das cidades como chaves e a coordenada no plano cartesiano das cidades como valores.
    """
    cidades = {}
    for i in range(n):
        cidades[f"Cidade {i}"] = (random.random(), random.random())
    return cidades


def computa_mochila(individuo, objetos, ordem_dos_nomes):
    """Computa o valor total e peso total de uma mochila.

    Argumentos:
      individiuo: uma lista binária contendo a informação de quais objetos serão selecionados.
      objetos: um dicionário onde as chaves são os nomes dos objetos e os valores são dicionários com a informação do peso e valor.
      ordem_dos_nomes: uma lista contendo a ordem dos nomes dos objetos.

    Retorna:
      valor_total: valor total dos itens da mochila em unidades de dinheiros.
      peso_total: peso total dos itens da mochila em unidades de massa.
    """

    valor_total = 0
    peso_total = 0

    for pegou_o_item_ou_nao, nome_do_item in zip(individuo, ordem_dos_nomes):
        if pegou_o_item_ou_nao == 1:
            valor_do_item = objetos[nome_do_item]["valor"]
            peso_do_item = objetos[nome_do_item]["peso"]

            valor_total = valor_total + valor_do_item
            peso_total = peso_total + peso_do_item
    return valor_total, peso_total


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


def individuo_cv(cidades):
    """Sorteia um caminho possível no problema do caixeiro viajante.

    Argumentos:
        cidades: dicionário onde as chaves são os nomes das cidades e os valores são as coordenadas das cidades.

    Retorna:
        Uma lista de nomes de cidades formando um caminho onde visitamos cada cidade apenas uma vez.
    """
    nomes = list(cidades.keys())
    random.shuffle(nomes)
    return nomes


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


def populacao_inicial_cv(tamanho, cidades):
    """Cria população inicial no problema do caixeiro viajante.
    Args
      tamanho:
        Tamanho da população.
      cidades:
        Dicionário onde as chaves são os nomes das cidades e os valores são as
        coordenadas das cidades.
    Returns:
      Lista com todos os indivíduos da população no problema do caixeiro
      viajante.
    """
    populacao = []
    for _ in range(tamanho):
        populacao.append(individuo_cv(cidades))
    return populacao


def selecao_roleta_max(populacao, fitness):
    """Seleciona indivíduos de uma população usando o método da roleta.

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
    ponto_de_corte = random.randint(1, len(pai) - 1)

    filho1 = pai[:ponto_de_corte] + mae[ponto_de_corte:]
    filho2 = mae[:ponto_de_corte] + pai[ponto_de_corte:]
    return filho1, filho2


def cruzamento_ordenado(pai, mae):
    """Operador de cruzamento ordenado. Neste cruzamento, os filhos mantêm os mesmos genes que seus pais tinham, porém, em outra ordem. Trata-se de um tipo de cruzamento útil para problemas onde a ordem dos genes é importante e não podemos alterar os genes em si. É um cruzamento que pode ser usado no problema do caixeiro viajante.

    Argumentos:
      pai: uma lista representando um indivíduo.
      mae: uma lista representando um indivíduo.

    Retorna:
      Duas listas, sendo que cada uma representa um filho dos pais que foram os argumentos. Estas listas mantém os genes originais dos pais, porém altera a ordem deles.
    """
    corte1 = random.randint(0, len(pai) - 2)
    corte2 = random.randint(corte1 + 1, len(pai) - 1)

    filho1 = pai[corte1:corte2]
    for gene in mae:
        if gene not in filho1:
            filho1.append(gene)
    filho2 = mae[corte1:corte2]
    for gene in pai:
        if gene not in filho2:
            filho2.append(gene)
    return filho1, filho2


def mutacao_cb(individuo):
    """Realiza a mutação de um gene no problema das caixas binárias.

    Argumentos:
        individuo: uma lista representado um indivíduo no problema das caixas binárias.

    Retorna:
        Um indivíduo com um gene mutado.
    """
    gene_a_ser_mutado = random.randint(0, len(individuo) - 1)
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
    gene_a_ser_mutado = random.randint(0, len(individuo) - 1)
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


def mutacao_tamanho_senha(individuo, letras, maximo):
    """Realiza a mutação de um gene da condição da senha.

    Argumentos:
      individuo: indivíduo que deve sofrer a mutação.
      letras: letras possíveis de serem sorteadas.
      maximo: máximo de mutações que podem ocorrer.

    Returna:
      Uma senha com um gene mutado.
    """
    n_mudar_tamanho = random.randint(1, maximo)
    soma_ou_subtração = random.randint(0, 1)

    if soma_ou_subtração:
        somar = [gene_letra(letras) for _ in range(n_mudar_tamanho)]
        individuo = individuo + somar
    else:
        if n_mudar_tamanho > len(individuo) - 1:
            n_mudar_tamanho = len(individuo) - 1
        subtrair = random.sample(individuo, n_mudar_tamanho)
        for gene in subtrair:
            individuo.remove(gene)
    return individuo


def mutacao_de_troca(individuo):
    """Troca o valor de dois genes.

    Argumentos:
      individuo: uma lista representado um indivíduo.

    Retorna:
      O indivíduo recebido como argumento, porém com dois dos seus genes trocados de posição.
    """

    indices = list(range(len(individuo)))
    lista_sorteada = random.sample(indices, k=2)

    indice1 = lista_sorteada[0]
    indice2 = lista_sorteada[1]

    individuo[indice1], individuo[indice2] = individuo[indice2], individuo[indice1]

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


def funcao_objetiva_cv(individuo, cidades):
    """Computa a função objetiva de um indivíduo no problema do caixeiro viajante.

    Argumentos:
      individiuo: uma lista contendo a ordem das cidades que serão visitadas
      cidades: um dicionário onde as chaves são os nomes das cidades e os valores são as coordenadas das cidades.

    Retorna:
      A distância percorrida pelo caixeiro seguindo o caminho contido no `individuo`. Lembrando que após percorrer todas as cidades em ordem, o caixeiro retorna para a cidade original de onde começou sua viagem.
    """
    distancia = 0

    for posicao in range(len(individuo) - 1):
        partida = cidades[individuo[posicao]]
        chegada = cidades[individuo[posicao + 1]]

        percurso = distancia_entre_dois_pontos(partida, chegada)
        distancia = distancia + percurso
    # Calculando o caminho de volta para a cidade inicial
    partida = cidades[individuo[-1]]
    chegada = cidades[individuo[0]]

    percurso = distancia_entre_dois_pontos(partida, chegada)
    distancia = distancia + percurso
    return distancia


def funcao_objetiva_senha_indeterminada(individuo, senha_verdadeira):
    """Computa a função objetiva no problema da senha.

    Argumentos:
      individiuo: lista contendo as letras da senha.
      senha_verdadeira: a senha que você está tentando descobrir.

    Retorna:
      A "distância" entre a senha proposta e a senha verdadeira.
    """
    diferenca = 0

    for letra_candidato, letra_oficial in zip(individuo, senha_verdadeira):
        diferenca += abs(ord(letra_candidato) - ord(letra_oficial))
    delta_tamanho = abs(len(senha_verdadeira) - len(individuo)) * 10
    diferenca += delta_tamanho

    return diferenca


def funcao_objetiva_mochila(individuo, objetos, limite, ordem_dos_nomes):
    """Computa a função objetiva de um candidato no problema da mochila.

    Argumentos:
      individiuo: uma lista binária contendo a informação de quais objetos serão selecionados.
      objetos: um dicionário onde as chaves são os nomes dos objetos e os valores são dicionários com a informação do peso e valor.
      limite: um número indicando o limite de peso que a mochila aguenta.
      ordem_dos_nomes: uma lista contendo a ordem dos nomes dos objetos.

    Retorna:
      Um valor total dos itens inseridos na mochila considerando a penalidade para quando o peso excede o limite.
    """

    valor_mochila, peso_mochila = computa_mochila(individuo, objetos, ordem_dos_nomes)

    if peso_mochila > limite:
        return 0.01
    else:
        return valor_mochila


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
    """Computa a funcao objetiva de uma populaçao no problema da senha.

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


def funcao_objetiva_pop_senha_tamanho_indeterminado(populacao, senha_verdadeira):
    """Computa a função objetiva de uma populaçao no problema da senha.

    Argumentos:
      populacao: lista com todos os individuos da população.
      senha_verdadeira: a senha que você está tentando descobrir

    Retura:
      Uma lista contendo os valores da métrica de distância entre senhas.
    """
    resultado = [
        funcao_objetiva_senha_indeterminada(individuo, senha_verdadeira)
        for individuo in populacao
    ]
    return resultado


def funcao_objetiva_pop_cv(populacao, cidades):
    """Computa a função objetiva de uma população no problema do caixeiro viajante.

    Argumentos:
      populacao: lista com todos os indivíduos da população.
      cidades: dicionário onde as chaves são os nomes das cidades e os valores são as coordenadas das cidades.

    Retorna:
        Uma lista contendo a distância percorrida pelo caixeiro para todos os indivíduos da população.
    """
    resultado = []
    for individuo in populacao:
        resultado.append(funcao_objetiva_cv(individuo, cidades))
    return resultado


def funcao_objetiva_pop_mochila(populacao, objetos, limite, ordem_dos_nomes):
    """Computa a função objetiva de uma população no problema da mochila.

    Argumentos:
      populacao: uma lista com todos os indivíduos da população
      objetos: um dicionário onde as chaves são os nomes dos objetos e os valores são dicionários com a informação do peso e valor.
      limite: um número indicando o limite de peso que a mochila aguenta.
      ordem_dos_nomes: uma lista contendo a ordem dos nomes dos objetos.

    Retorna:
      Uma lista contendo o valor dos itens da mochila de cada indivíduo.
    """

    resultado = []
    for individuo in populacao:
        resultado.append(
            funcao_objetiva_mochila(individuo, objetos, limite, ordem_dos_nomes)
        )
    return resultado