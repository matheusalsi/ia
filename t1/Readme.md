INF01048 - Inteligência Artificial - 2023/2
Trabalho 1

Integrantes:
Matheus Almeida Silva   - 00316326    - Turma A
Maiara Schein Trevisol  - 00275946    - Turma A


1. Regressão linear
    Para a análise da regressão linear utilizou-se os dados de alegrete.csv não normalizados e normalizados, a fim de comparar qual deles resultaria em um erro quadrático médio (EQM) menor. Foram escolhidos três tipos diferentes de algoritmos de normalização: min-max scaling, L1 e L2. É importante destacar que os valores de bias e peso não impactaram significativamente no erro quadrático médio dos experimentos.
    A visualização dos resultados pode ser realizada utilizando as diferentes variações de dataset consideradas. Para isso, é preciso executar a célula que contém a visualização dos dados, e, após, executar a célula da regressão linear e cálculo do EQM por época/iteração.

1.1 Dados Não normalizados

    Considerando os dados não normalizados, obteve-se um erro quadrático médio mínimo de  8.52770819098256 usando um alpha de 0.01 e um número de iterações de 1500. Pode-se notar que para dados não normalizados é preciso usar um valor baixo de alpha devido a alta variação entre os dados de entrada.

1.2 Dados normalizados por min-max scaling
    Utilizando a normalização por min-max foi possível aumentar o valor de alpha, pois os dados normalizados variam menos. Assim, o menor EQM encontrado para min-max foi de 8.52770819098256, com um alpha de 0.3 e  1500 iterações. Também observou-se um bom resultado utilizando um alpha de 0.1 e o mesmo número de iterações, resultando num EQM de 8.52770819098458.

1.3 Dados normalizados por L1

    A normalização L1 apresentou um resultado menos satisfatório do que utilizando os dados não normalizados. O menor EQM obtido foi de 13.068339598330578 utilizando um alpha de 0.6 e 1500 iterações.

    alpha = 0.1
    iterações = 1500
    EQM = 13.069185704663097

    alpha = 0.6
    iterações = 1500
    EQM =  13.068339598330578

1.4 Dados normalizados por L2

    Os dados obervados para normalização L2 são mais satisfatórios que os dados obtidos por L1, mas ainda não são superiores ao uso do min-max ou até mesmo ao uso dos dados não normalizados. O melhor resultado obtido para L2 apresentou um EQM de 11.832758696808808 utilizando um alpha de 0.5 e 1500 iterações.


    alpha = 0.1
    iterações = 1500
    EQM = 11.868146388130713

    alpha = 0.5
    iterações = 1500
    EQM = 11.832758696808808


