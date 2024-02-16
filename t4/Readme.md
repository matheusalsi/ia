# INF01048 - Inteligência Artificial - 2023/2 - Trabalho 4 

## Integrantes:

    Matheus Almeida Silva   - 00316326    - Turma A
    Maiara Schein Trevisol  - 00275946    - Turma A


## Tic-Tac-Toe 
Observamos que o minimax no Tic-Tac-Toe apresentou um desempenho bastante satisfatório, atigindo resultados ótimos nos jogos que realizamos. Abaixo respondemos as perguntas direcionadas pela atividade.
    
### (i) O minimax sempre ganha do randomplayer?
Sim, nosso algoritmo de minimax ganhou do random players em todos os nossos jogos testados.

### (ii) O minimax sempre empata consigo mesmo?
Sim, nosso algoritmo de minimax empatou diversas vezes consigo mesmo.

### (iii) O minimax sempre empata contra as jogadas perfeitas recomendadas pelo https://nyc.cs.berkeley.edu/uni/games/ttt/variants/misere ? Para verificar isso, use o humanplayer. No link, faça as jogadas do minimax, e no servidor do kit, faça as jogadas recomendadas (amarelo ou verde) do link.
Sim, conforme alguns jogos o minimax sempre segue alguma das jogadas recomendadas ganhando ou empatando o jogo com o human player.



## Othello
Conforme a especificação implementamos 3 diferentes heurísticas para avaliação. Para a versão customizado optamos por uma heurística baseada em cantos, a escolha foi motivada pelo trabalho "An Analysis of Heuristics in Othello" Sannidhanam et. al, disponível em: https://courses.cs.washington.edu/courses/cse573/04au/Project/mini1/RUSSIA/Final_Paper.pdf

### (i) Represente em uma matriz de 3 X 3 onde as linhas representam o jogador que inicia(player 1) e as colunas representam o player 2 e em cada célula, indique se a partida resultou em vitória (1), derrota (-1) ou empate (0) entre os agentes com cada uma das heurísticas.

|                | minimax_count | minimax_mask | minimax_custom |
|----------------|---------------|--------------|----------------|
| minimax_count  |        1      |      -1      |       1        |
| minimax_mask   |        1      |      -1      |       1        |
| minimax_custom |        1      |      -1      |      -1        |


### (ii) Observe e relate qual implementação foi a mais bem-sucedida.
Nos nossos jogos a minimax_mask, i.e Heurística do valor posicional , foi a mais bem sucedida, ganhando de todas as outras, incluindo a customizada, i.e Heurística de bordas.

### (iii) Reflita sobre o que pode ter tornado cada heurística melhor ou pior, em termos de performance.
Observando nossos resultados observamos algumas implicações interessantes.

A heurística 1, i.e Heurística da contagem de peças, mesmo sendo a mais simples entretanto teve resultado superior a versão customizada, sua avaliação baseada em peças do jogador e oponente tornava ela mais rápida e eficaz. Observamos que quando ela jogava como player 1, ela vencia a heurística de bordas, com a versão customizada encerrando abruptamente. Sua simplicidade por torná-la útil para um desempenho rápido mas parece limitada quando comparado a Heurística de Posições.

A heurística 2,i.e Heurística do valor posiciona, apresentou desempenho satisfatório contra todas as demais, com sua configuração de tabuleiro oferecendo o melhor desempenho. A definição da matriz implica diretamente no desempenho da heurística, contribuindo para sua melhora ou piora dependendo da configuração estabelecida. Portanto, seu desempenho vai ser dependente da qualidade da matriz configurada.

A heurística 3, i.e Heurística de Bordas, não teve desempenho esperado, apresentando encerramento abrupto quando iniciada como player 2 e não conseguindo tirar proveito das bordas no jogo. Nossa implementação se demonstrou simples demais, pois só estabelecia o mesmo peso estático para todos os cantos sem considerar cantos capturados, cantos potencialmente capturáveis pelo adversário e demais técnicas observadas no trabalho supracitado. Entretando é notável como o refinamento do cálculo desses pesos pode contribuir para o desempenho da heurística, como visto no paper.


