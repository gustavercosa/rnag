![REDES NEURAIS E ALGORITMOS GENÉTICOS (3)](https://github.com/gustavercosa/rnag/assets/107042962/45a07711-4c97-42d8-ae73-ce9d86daf08d)
<h1 align="center"> </h1>

<h2 align="left"> Introdução </h2> 
<blockquote> 
<p align="justify"> Essa é a parte que contém os experimentos e as discussões que tangem o aprendizado de Algoritmos Genéticos.</p>
<img src="https://img.shields.io/badge/STATUS-Concluído-576CFB"> <img src="https://img.shields.io/badge/LICENCE-GNU%20General%20Public%20License%20v3.0-75CA75">
</blockquote> 

<h2 align="left"> Aprofundação </h2>
<blockquote> 
<p align="justify"> Foi apresentado sucintamente, no <a href="https://github.com/gustavercosa/rnag/blob/main/README.md">README.md introdutório</a>, o que são algoritmos genéticos.</p>
<p align="justify"> Como visto, algoritmos genéticos são uma classe de algoritmos de otimização inspirados na evolução biológica. Seu principal usado é voltado para encontrar soluções aproximadas para problemas complexos de otimização.</p>
<p align="justify"> <strong>Entretanto, como eles funcionam?</strong> Esses algoritmos geram um conjunto de soluções candidatas representadas por indivíduos. Cada indivíduo é codificado por um conjunto de genes que representam suas características ou parâmetros. Esses genes podem ser combinados e modificados por agentes genéticos como seleção, cruzamento e mutação para produzir novas gerações de indivíduos. Cada geração é avaliada de acordo com um critério de ajuste que mede o quão bem cada pessoa se ajusta ao problema dado. A partir dessa avaliação, são selecionados os indivíduos mais adequados para sobrevivência e reprodução, que darão origem a novas gerações.</p>
<p align="justify"> Ao longo do tempo, a população evolui e converge para melhores soluções até que uma solução ótima seja encontrada ou um limite de tempo, ou geração, seja atingido.</p>
<p align="justify"> Algoritmos genéticos têm sido usados em muitos campos, como engenharia, finanças, bioinformática, e são particularmente úteis quando soluções devem ser encontradas em espaços de busca complexos e multidimensionais.</p>
</blockquote> 

<h2 align="left"> Diferenças </h2>
<blockquote> 
<p align="justify"> Em comparação com os algoritmos tradicionais, os algoritmos genéticos diferem em vários aspectos, como:</p>
<ol>
  <li><p align="justify">Os algoritmos genéticos podem avaliar várias soluções candidatas simultaneamente, enquanto os algoritmos tradicionais geralmente avaliam uma solução por vez.</p></li>
  <li><p align="justify">Os algoritmos genéticos podem explorar com eficiência espaços de busca muito grandes e complexos, enquanto os algoritmos convencionais podem se esforçar para encontrar soluções em um espaço de busca com muitas variáveis e restrições.</p></li>
  <li><p align="justify">Os algoritmos genéticos tendem a encontrar soluções ótimas globais, enquanto algoritmos tradicionais podem ficar presos em mínimos locais.</p></li>
  <li><p align="justify">Os algoritmos genéticos são algoritmos heurísticos que utilizam técnicas probabilísticas e estocásticas para explorar o espaço de busca, enquanto os algoritmos convencionais são algoritmos determinísticos que seguem uma estratégia predeterminada para encontrar uma solução.</p></li>
  <li><p align="justify">Os algoritmos genéticos são adaptativos e podem se adaptar às mudanças no espaço de busca ao longo do tempo, enquanto os algoritmos tradicionais são estáticos e não podem se adaptar às mudanças no espaço de busca.</p></li>
</ol>
<p align="justify"> Em suma, enquanto os algoritmos tradicionais são algoritmos de otimização determinísticos que seguem uma estratégia predeterminada para encontrar uma solução, os algoritmos genéticos são uma classe de algoritmos de otimização que exploram o espaço de busca de forma heurística e adaptativa. O que faz sentido, quando vemos a sua inspiração na evolução biológica.</p>
</blockquote>

<h2 align="left"> O que temos aqui? </h2>
<blockquote> 
<p align="justify"> Nessa pasta, temos quatro tipos de arquivos:</p>
<ol>
    <li><p align="justify">Os arquivos com experimentos abordados em sala, que são mais conteudistas. Eles são nomeados como "Experimento A.0X", onde X representa a cronologia da sucessão do estudo.</p></li>
    <li><p align="justify">Os arquivos com experimentos exploratórios, que são conteúdos complementares, feitos sem o direcionamento em sala. Eles são nomeados como "Experimento GA.0X", onde X representa o tipo de exercício.</p></li>
    <li><p align="justify">O arquivo "funcoes.py", que contém todas as funções gerais utilizadas.</p></li>
    <li><p align="justify">O arquivo "README.md", o qual você está lendo no momento.</p></li>
</blockquote>
    
<h2 align="left"> Quais são as funções? </h2>
<blockquote>
<p align="justify"> Na pasta "funcoes.py", temos oito tipos de funções:</p>
<ol>
    <li><p align="justify"> As funções de <strong>suporte</strong>, utilizadas para especificar uma resolução de alguma problemática.</p></li>
    <li><p align="justify"> As funções de <strong>genes</strong>, utilizadas para criar um objeto inicial de interação e manipulação dos algoritmos.</p></li>
    <li><p align="justify"> As funções de <strong>indivíduos</strong>, utilizadas para criar um conjunto de genes, isto é, uma composição complexas de objetos para serem analisados.</p></li>
    <li><p align="justify"> As funções de <strong>população</strong></p>, utilizadas, de modo análogo às funções anteriores, para compor uma associação de indivíduos, ou seja, uma grade de objetos para serem analisados.</li>
    <li><p align="justify"> As funções de <strong>seleção</strong>, utilizadas para escolher, com base em determinados critérios, indivíduos de uma população.</p></li>
    <li><p align="justify"> As funções de <strong>cruzamento</strong>, utilizadas para entrelaçar indivíduos selecionados.</p></li>
    <li><p align="justify"> As funções de <strong>mutação</strong>, utilizadas para alterar, de forma aleatória, um gene (ou mais) de um indivíduo, que também pode ser aleatório.</p></li>
    <li><p align="justify"> As funções <strong>objetivas <i>para indivíduos</i></strong>, utilizadas para ver o desempenho de um indivíduo, maximizando ou minimizandor o valor de <i>fitness</i>.</p></li>
    <li><p align="justify"> As funções <strong>objetivas <i>para população</i></strong>, utilizadas para ver o desempenho de uma população, maximizando ou minimizando o valor de <i>fitness</i>.</p></li>
</ol>
<p align="justify"> Dentro da pasta, há uma coletânea de funções para cada tipo e as diversas explicações que compõem o conjunto. É recomendado ler a descrição do objetivo e ver como o código foi construído, para entender a atribuição de cada função.</p>
</blockquote>
    
<h2 align="left"> Entendimento final </h2>
<blockquote> 
<p align="justify"> Para entender como isso ocorre, é preciso ter em mente como há a validação dos processamentos até chegar em um resultado.</p>   
<p align="justify"> Nisso, temos o uso do <i>fitness</i>. O papel do fitness é medir a aptidão de cada indivíduo em relação ao objetivo do problema que está sendo resolvido.</p>  
<p align="justify"> Em outras palavras, é uma função que pontua cada pessoa com base em quão bem ela se encaixa em uma determinada tarefa. E, a partir disso, podemos ver como o código está bem aquedado.</p>  
</blockquote>