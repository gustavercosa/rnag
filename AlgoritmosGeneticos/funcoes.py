def funcao_objetiva_cb(individuo):
    """Computa a função objetiva no problema das caixas binárias.

    Argumentos:
        individuos: lista contendo os genes das caixas binárias.

    Retorna:
        Um valor representando a soma dos genes do indivíduo.
    """
    return sum(individuo) 