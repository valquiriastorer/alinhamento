# -*- coding: utf-8 -*-

# Constantes
# use essas constantes caso desejar
DNA = 'ATCG'
GAP = '_'

#------------------------------------------------------------------
def main():
    '''
        Modifique essa função, escrevendo os seus testes.
    '''

    print('Testes da função gera_gaps():')

    print(f"dna = 'T', gera_gaps = {gera_gaps('T')}")
    print(f"dna = 'CA', gera_gaps = {gera_gaps('CA')}")
    print(f"dna = 'AT_G', gera_gaps = {gera_gaps('AT_G')}")
    print()
    
    print('Testes da função pontuacao():')
    print(f"pontuacao('T_', 'CT', 1, 5, 6, 3) = {pontuacao('T_', 'CT', 1, 5, 6, 3)}")
    print(f"pontuacao('T_CGTAC', 'T_CG_TC', 1, 5, 6, 3) = {pontuacao('T_CGTAC', 'T_CG_TC', 1, 5, 6, 3)}")
    print(f"pontuacao('T_CGTAC', 'A_CG_T_', 2, 3, 5, 4) = {pontuacao('T_CGTAC', 'A_CG_T_', 2, 3, 5, 4)}")
    print(f"pontuacao('T_CGTA',  'A_CGT_', -1, 5, 3, 2) = {pontuacao('T_CGTA',  'A_CGT_', -1, 5, 3, 2)}")
    print()

    print('Testes de gera_n_gaps')
    print(f"gera_n_gaps( 'T', 2 ) = {gera_n_gaps( 'T', 2 )}")
    print(f"gera_n_gaps( 'CA', 2 ) = {gera_n_gaps( 'CA', 2 )}")
    print(f"gera_n_gaps( 'C_A', 2) = {gera_n_gaps( 'C_A', 2)}")
    print()
    ## Escreva aqui os testes para a função pontuacao_max()
    print(f"pontuacao_max('T_CG', 'ATCG', 5, 4, 3, 2) = {pontuacao_max('T_CG', 'ATCG', 5, 4, 3, 2)}")
    print(f"pontuacao_max('T_CGTAC', 'ATCG_T_', 0, 1, 4, 3, 2) = {pontuacao_max('T_CGTAC', 'ATCG_T_', 0, 1, 4, 3, 2)}")
    print(f"pontuacao_max('AT_', 'A_T', 2, 5, 1, 0, 2) = {pontuacao_max('AT_', 'A_T', 2, 5, 1, 0, 2)}")
 
    print("Fim dos meus testes.")

#------------------------------------------------------------------
def gera_gaps( dna ):
    ''' ( str ) -> list

    RECEBE uma string `dna` representando uma fita de DNA com os
    símbolos 'A', 'T', 'C', 'G' e '_' (GAP).

    RETORNA uma lista com todas as variações de dna com um símbolo GAP 
    a mais e sem repetições.

    exemplos: 
    In  [1]: gera_gaps( 'T' )
    Out [1]: ['_T', 'T_']
    
    In  [2]: gera_gaps( 'CA' )
    Out [2]: ['_CA', 'C_A', 'CA_']
    
    In  [3]: gera_gaps( 'AT_G')
    Out [3]: ['_AT_G', 'A_T_G', 'AT__G', 'AT_G_'] 
    '''
    # modifique o código abaixo para conter a sua solução.
    variações = []
    n = len(dna)
    i = 0 #contador para marcar o momento de colocar o gap
    while i <= n:
        dna_gap = ''
        for j in range(n): #construo a string caractere a caractere
            if j == i:
                dna_gap += GAP
            dna_gap += dna[j]
        if i == n: #para o GAP ir após o dna
            dna_gap += GAP
        if dna_gap not in variações:
            variações += [dna_gap]
        i += 1
    
    return variações
#------------------------------------------------------------------
def gera_n_gaps( dna, n=1 ):
    '''( str, int ) -> list

    RECEBE uma string `dna` representando uma fita de DNA com os
    símbolos 'A', 'T', 'C', 'G' e '_' (gap), e um número inteiro positivo `n`.
 
    RETORNA uma lista sem repetições com todas as variações de `dna` 
    com até `n` gaps extras.

    EXEMPLOS:
 
    In [1]: gera_n_gaps( 'T', 2 )
    Out[1]: ['T', '_T', 'T_', '__T', '_T_', 'T__']
    
    In [2]: gera_n_gaps( 'CA', 2 )
    Out[2]: ['CA', '_CA', 'C_A', 'CA_', '__CA', '_C_A', '_CA_', 'C__A', 'C_A_', 'CA__']
    
    In [3]: gera_n_gaps( 'C_A', 2)
    Out[3]: ['C_A', '_C_A', 'C__A', 'C_A_', '__C_A', '_C__A', '_C_A_', 'C___A', 'C__A_', 'C_A__']
    '''
    # modifique o código abaixo para conter a sua solução.
    variações = []
  
    for n_gaps in range(n+1):
        if n_gaps == 0:
            variações += [dna]
        elif n_gaps == 1:
            variações += gera_gaps(dna) 
        else:
            n_var = len(variações)
            for i in range(1, n_var): 
               variações += gera_gaps(variações[i])
    
    var_n = []
    n_var = len(variações)
    for j in range(n_var):
        if variações[j] not in var_n:
            var_n += [variações[j]]
    return var_n

#------------------------------------------------------------------
def pontuacao(s, t, ga, la, ldif, lgap):
    ''' (str, str, int, int, int, int) -> int

    RECEBE duas strings `s` e `t` de mesmo tamanho com zero ou mais gaps 
    representando fitas de DNA; e quatro inteiros `ga`, `la`, `ldif`, `lgap`.
 
    RETORNA a pontuação do alinhamento entre `s` e `t` calculada da seguinte 
    forma:

       * dois gaps alinhados contam `ga` pontos,
       * duas letras iguais alinhadas contam `la` pontos, 
       * duas letras diferentes alinhadas contam `-ldif` pontos (subtrai ldif pontos) e 
       * uma letra alinhada com um gap contam `-lgap` pontos (subtrai lgap pontos).

    Exemplos:

    In  [1]: pontuacao('T_', 'CT', 1, 5, 6, 3)
    Out [1]: -9

    In  [2]: pontuacao('T_CGTAC', 'T_CG_TC', 1, 5, 6, 3)
    Out [2]: 12
    
    In  [3]: pontuacao('T_CGTAC', 'A_CG_T_', 2, 3, 5, 4)
    Out [3]: -10
    
    In  [4]: pontuacao('T_CGTA',  'A_CGT_', -1, 5, 3, 2)
    Out [4]: 9
    '''
    # modifique o código abaixo para conter a sua solução.

    n = len(s)
    pontos = 0
    i = 0
    while i < n:
        if s[i] in DNA and t[i] in DNA:
            if s[i] == t[i]:
                pontos += la
            else:
                pontos -= ldif
        elif s[i] in GAP and t[i] in GAP:
            pontos += ga
        else:
            pontos -= lgap
        i += 1
    return pontos
#-------------------------------------------------------------------------
def pontuacao_max(s, t, ga, la, ldif, lgap, n = 1):
    '''(str, str, int, int, int, int, int) -> int, list de list

    RECEBE:

        - duas strings `s` e `t` de mesmo comprimento representando fitas de DNA 
          com os símbolos 'A', 'T', 'C', 'G' e '_' (gap); e
        - quatro números inteiros `ga`, `la`, `ldif` e `lgap`;
        - mais um número inteiro positivo `n`.

    RETORNA 

        - a maior pontuação entre pares de variações de s e t que têm:

              * o mesmo comprimento; 
              * até `n` gaps extras.

        - uma lista com todos os pares de variações de s e t que têm 
          esta maior pontuação; cada par é uma lista com duas variações.

    Exemplos:

    In [1]: pontuacao_max('T_CG', 'ATCG', 5, 4, 3, 2)
    Out[1]: (15, [['_T_CG', 'AT_CG']])

    In [2]: pontuacao_max('T_CGTAC', 'ATCG_T_', 0, 1, 4, 3, 2)
    Out[2]: (-5, [['_T_CG_TAC', 'AT_CG_T__']])

    In [3]: pontuacao_max('AT_', 'A_T', 2, 5, 1, 0, 2)
    Out[3]: (16, [['_A_T_', '_A_T_'], 
                  ['A__T_', 'A__T_'], 
                  ['A_T__', 'A_T__']])
    '''
    # modifique o código abaixo para conter a sua solução.
    pares = []
    var_s = gera_n_gaps(s, n)
    var_t = gera_n_gaps(t, n)
    pmax = pontuacao(s, t, ga, la, ldif, lgap) # não é = 0 por conta do negativo

    for i in range(len(var_s)):
        for j in range(len(var_t)):
            if len(var_s[i]) == len(var_t[j]):
                pontos = pontuacao(var_s[i], var_t[j], ga, la, ldif, lgap)
                if pontos > pmax:
                    pmax = pontos
                    pares = [[var_s[i], var_t[j]]]
                elif pontos == pmax:
                    pares += [[var_s[i], var_t[j]]]
    
    return pmax, pares
    

#######################################################
###                 FIM                             ###
#######################################################
# 

if __name__ == '__main__':
    main()