# Alinhamento de sequências de DNA

## Descrição do projeto

### Introdução

Em bioinformática, um alinhamento de sequência é uma maneira de organizar as sequências de DNA, RNA ou proteína para identificar seu grau de similaridade que pode ser importante na identificação de relações funcionais, estruturais ou evolutivas entre eles. O genoma humano e o do rato, por exemplo, compartilham uma região conservada com até 8 megabases de comprimento.

O ácido desoxirribonucleico (DNA) é uma molécula que carrega o código genético de todos os organismos vivos.

Sequenciamento é o processo para determinar a ordem precisa de nucleotídeos de uma determinada molécula de DNA. É usado para determinar a ordem das quatro bases adenina ('A'), guanina ('G'), citosina ('C') e timina ('T'), em uma fita de DNA. Assim, (fitas de) DNAs são representados por strings dos caracteres 'A', 'C', 'G' e 'T'.

Um alinhamento de duas sequências de DNA s e t é obtido adicionando-se os chamados gaps, representados pelo caractere ‘_’ (underscore), a essas strings de modo que fiquem com um mesmo comprimento.

Por exemplo, se s = TCGTAC e t = ATCG, então um alinhamento em que as strings resultantes s e t tenham o mesmo tamanho poderia ser: s' = T_CGTAC e t' = ATCG___ .

Uma tarefa importante em bioinformática é encontrar um alinhamento entre duas sequências de DNA que tenha pontuação máxima. 

### Descrição do projeto

As funções presentes no arquivo alinhamento.py permitem a comparação entre duas fitas de DNA calculando uma pontuação. Quanto maior é a pontuação, mais similares são as fitas entre si.

As funções gera_gaps() e gera_n_gaps() recebem uma string representando uma fita de DNA com os símbolos 'A', 'T', 'C', 'G' e '_'; e retornam uma lista de todas as variações de dna com um '_' extra (no caso da primeira função) ou mais '_' extras (no caso da segunda função).

A função pontuacao() retorna a pontuação do alinhamento entre duas fitas de DNA distintas.

A função pontuacao_max() retorna uma lista com os pares de variações de duas fitas de DNA distintas com a maior pontuação, e a maior pontuação entre pares de variações com o mesmo comprimento e número de '_' extras.

> Este programa foi realizado como exercício de programação para a disciplina de Introdução à Computação (MAC0110) oferecida pela Universidade de São Paulo em 2021, ministrada pelos professores Jose Coelho de Pina Junior e Carlos Hitoshi Morimoto



