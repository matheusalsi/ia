# INF01048 - Inteligência Artificial - 2023/2 - Trabalho 1 

## Integrantes:

    Matheus Almeida Silva   - 00316326    - Turma A
    Maiara Schein Trevisol  - 00275946    - Turma A


## 1. Regressão linear
    
        Para a análise da regressão linear utilizou-se os dados de alegrete.csv não normalizados e normalizados, a fim de comparar qual deles resultaria em um erro quadrático médio (EQM) menor. Foram escolhidos três tipos diferentes de algoritmos de normalização: min-max scaling, L1 e L2. É importante destacar que os valores de bias e peso não impactaram significativamente no erro quadrático médio dos experimentos.
        
        A visualização dos resultados pode ser realizada utilizando as diferentes variações de dataset consideradas. Para isso, é preciso executar a célula que contém a visualização dos dados, e, após, executar a célula da regressão linear e cálculo do EQM por época/iteração.
    
### 1.1 Dados Não normalizados
        
        Considerando os dados não normalizados, obteve-se um erro quadrático médio mínimo de  8.52770819098256 usando um alpha de 0.01 e um número de iterações de 1500. Pode-se notar que para dados não normalizados é preciso usar um valor baixo de alpha devido a alta variação entre os dados de entrada.

### 1.2 Dados normalizados por min-max scaling
        
        Utilizando a normalização por min-max foi possível aumentar o valor de alpha, pois os dados normalizados variam menos. Assim, o menor EQM encontrado para min-max foi de 8.52770819098256, com um alpha de 0.3 e  1500 iterações. Também observou-se um bom resultado utilizando um alpha de 0.1 e o mesmo número de iterações, resultando num EQM de 8.52770819098458.

### 1.3 Dados normalizados por L1

        A normalização L1 apresentou um resultado menos satisfatório do que utilizando os dados não normalizados. O menor EQM obtido foi de 13.068339598330578 utilizando um alpha de 0.6 e 1500 iterações.

        alpha = 0.1
        iterações = 1500
        EQM = 13.069185704663097

        alpha = 0.6
        iterações = 1500
        EQM =  13.068339598330578

### 1.4 Dados normalizados por L2

        Os dados obervados para normalização L2 são mais satisfatórios que os dados obtidos por L1, mas ainda não são superiores ao uso do min-max ou até mesmo ao uso dos dados não normalizados. O melhor resultado obtido para L2 apresentou um EQM de 11.832758696808808 utilizando um alpha de 0.5 e 1500 iterações.


        alpha = 0.1
        iterações = 1500
        EQM = 11.868146388130713

        alpha = 0.5
        iterações = 1500
        EQM = 11.832758696808808

## 2. Redes Neurais

###  Características do dataset
        cifar-10: Consiste em 50000 imagens de treino e 10000 imagens de teste, cada imagem tem 32x32 pixels em RGB(3 canais) categorizada entre 10 classes.

        cifar-100: Consiste em 50000 imagens de treino e 10000 imagens de teste, cada imagem tem 32x32 pixels em RGB(3 canais) categorizada entre 100 classes.

        mnist: Consiste em 60000 imagens de treino e 10000 imagens de teste, cada imagem tem 28x28 pixels em grayscale(1 canal) categorizada entre 10 classes.

        fashion mnist: Consiste em 60000 imagens de treino e 10000 imagens de teste, cada imagem tem 28x28 pixels em grayscale(1 canal) categorizada entre 10 classes.
    
### 2.1 Investigue e reflita sobre os fatores que tornam os problemas de classificação de cada dataset mais  ou  menos  complexos  em  cada  dataset. Pense  em  uma  relação  de  ordem  de complexidade/dificuldade dos datasets e justifique a resposta. O mais importante nesta questão é a investigação e a reflexão e não o fato de a resposta estar precisa.  
       Entre os fatores que podem impactar a classificação do dataset estão o tamanho e quantidade de canais das imagens, além das características que queremos extrair deles.Nota-se que para dataset simples como o mnist e fashion mnist, no qual o canal de cor é único, temos que arquiteturas de redes convolucionais com poucas camadas e menos filtros já apresentam um desempenho satisfatório, ao passo que as mesmas não são adequadas para as imagens do cifar.

       Ademais, a quantidade de classes impacta na complexidade da tarefa, e.g no cifar-100 o desempenho para uma rede mais simples era consideravelmente inferior ao do cifar-10, refletindo a complexidade maior da tarefa em extrair features adequadas para classificar entre 100 possibilidades.

       A complexidade também está intimamente ligada as camadas utilizadas, uma vez que para problemas mais complexos é razoável fornecer mais camadas, permitindo que se especializem em features genéricos no início e mais complexas ao fim do feature extractor da rede convolucional.

### 2.2 Qual  a  maior  acurácia  obtida  em  cada  dataset  e  quais  mudanças  fizeram  a  performance melhorar (ou pior, caso tenha ocorrido piora em relação a alguma performance já avaliada).


        Em nosso experimento variamos inicialmente a quantidade de filtros de uma única camada convolucional, observando os impactos nos diferentes datasets, gerando a versão 2(64 filtros) e versão 3(128 filtros). No cifar-10 e cifar-100 houve aumento da acurácia com o aumento de filtros, com a acurácia do cifar-10 original de 31.25% indo a 55.02% com 64 filtros na Conv2D e o cifar-100 indo de 1% a 26.73% com 128 filtros na Conv2d. Nos datasets do mnist e fashion_mnist houveram diferenças residuais na acurácia, com 64 e 128 filtros a acurácia diminui levemente em uma diferença de menos de 1% para ambos os casos.

        Posteriormente buscamos explorar a inclusão de novas camadas convolucionais e de max polling na rede, visando observar como as camadas poderiam ajudar se especializando em features diferentes. Gerando as versão 4(uma camada Conv2d adicional) e versão 5(duas camadas Conv2d adicionais).
        No cifar10 conseguimos melhorar a rede saindo de 31.25% do original a 63.84% na versão 4(com uma camada adicionald de Conv2d), enquanto no cifar100 saímos de 1% para 26.73% na versão 5, houve entretanto pouco ganho da versão 4 para a versão 5 do cifar100. No mnist houve ganho com as versão 4 e 5 mas pequenos, em torno de 1%.

        Notamos também que na versão 4 e 5 o cifar100 apresentava certo overfitting, com acurácia de treino de 40.87% em comporação aos 26.73% observados no teste. Essa limitação pode estar relacionado a limitação do classificar, i.e rede neural pós convolução, que apresenta somente uma única camada após receber o flatten do feature map final, tendo que inferir as 100 classes com apenas uma camada de abstração. Versões adicionais poderiam explorar o aumento de camdas no classificador mas não foram implementadas no tempo hábil.

        Por fim sumarizamos abaixo os melhores resultados obtidos para cada dataset e sua respectiva versão:

        * Mnist Versão 4 - Acurácia no conjunto de teste: 98.50%
        * Fashion_mnist Versão 4 - Acurácia no conjunto de teste: 89.42%
        * Cifar10 Versão 4 - Acurácia no conjunto de teste: 63.84%
        * Cifar100 Versão 5 - Acurácia no conjunto de teste: 26.73%

Para o item 2.2 é fornecemos uma documentação adicional em um arquivo de texto, chamado resultados_redes.txt, com o log dos treinamentos das diferentes versões citadas.




