import numpy as np



### MEU MÉTODO (GUILHERME H) MAS O MATEUS TAMBEM FEZ, PORÉM O DELE ERA MAIS GRANDE SÓ ISSO
def separarMensagem(msg):
    grupos = []
    i = 0
    while i < len(msg):
        restante = len(msg) - i

        if restante >= 3:
            grupos.append(msg[i:i+3]) ## aqui vai do atual, até ele mais 2 (por que nao inclui o 3) 
            i += 3
        elif restante == 2:
            grupos.append(msg[i:i+2]) 
            i += 2
        elif restante == 1:
            grupos[-1] += msg[i]  ## adiciona o último caractere ao último grupo
            break
    return grupos

### GUILHERME ORESTE MÉTODOS
def converterMensagem(grupomsg):
    santoDicionario = {
        " ": 2,  "A": 3,  "B": 5,  "C": 7,  "D": 9,
        "E": 11, "F": 13, "G": 15, "H": 17, "I": 19,
        "J": 21, "K": 23, "L": 25, "M": 27, "N": 29,
        "O": 31, "P": 33, "Q": 35, "R": 37, "S": 39,
        "T": 41, "U": 43, "V": 45, "W": 47, "X": 39,
        "Y": 51, "Z": 53
    }

    msgConvertida = []

    for grupo in grupomsg:
        numeros = []

        for letra in grupo:
            #Transforma as letras minúsculas em maiúsculas,assim fazendo a conversão
            letra = letra.upper()

            if letra  in santoDicionario:
              numeros.append(santoDicionario[letra])
        
        msgConvertida.append(numeros)
    
    return msgConvertida


### GUILHERME HENRIQUE MÉTODOS
def criarChaves(chave):
    def preencher_matriz(ordem, chave):
        
        linhas, colunas = ordem

        matriz = np.empty((linhas, colunas), dtype=str)

        tamanho_total = linhas * colunas
        
        chave_repetida = (chave * ((tamanho_total // len(chave)) + 1))[:tamanho_total]
        
        index = 0
        for i in range(linhas):
            for j in range(colunas):
                matriz[i][j] = chave_repetida[index]
                index += 1
                
        return matriz

    
    chave2x2 = converterMensagem(preencher_matriz((2, 2), chave))
    print(chave2x2)
    chave3x3 = converterMensagem(preencher_matriz((3, 3), chave))
    chave4x4 = converterMensagem(preencher_matriz((4, 4), chave))

    grupoChaves = [chave2x2, chave3x3, chave4x4]

    return grupoChaves


### TA AQUI POR UNS MOTIVOS AINDA PENSANDO
def codificarMensagem(grupoMsgConvertida, grupoChaves):
    return multiplicarMatrizes(grupoChaves, grupoMsgConvertida)


### MATEUS MULTIPLICAR MATRIZ
def multiplicarMatrizes(grupoChaves, grupoMsg):
    resultado = []    
    
    for grupos in grupoMsg:
        
        tamanho = len(grupos)

        i = 0           
        multi = []

        if tamanho == 1:
            chave = grupoChaves[0]
            
            while(i<tamanho):

                linha = ((grupos[0] * chave[0][i]))
                
                #print (f"{grupos[0]} * {chave[0][i]} + {(grupos[1])} * {chave[1][i]}") 
            
                multi.append(linha)
                i += 1

        if tamanho == 2:
            chave = grupoChaves[0]

            while(i<tamanho):

                linha = ((grupos[0] * chave[0][i]) 
                         + (grupos[1]) * chave[1][i] )
                
                #print (f"{grupos[0]} * {chave[0][i]} + {(grupos[1])} * {chave[1][i]}")
                
                multi.append(linha)
                i += 1

        elif tamanho == 3:
            chave = grupoChaves[1]

            while(i<tamanho):

                linha = ((grupos[0] * chave[0][i]) 
                         + (grupos[1]) * chave[1][i] 
                         + (grupos[2]) * chave[2][i] )
                
                #print (f"{grupos[0]} * {chave[0][i]} + {(grupos[1])} * {chave[1][i]} + {(grupos[2])} * {chave[2][i]}")
                
                multi.append(linha)
                i += 1

        elif tamanho == 4:
            chave = grupoChaves[2]

            while(i<tamanho):

                linha = ((grupos[0] * chave[0][i]) 
                         + (grupos[1]) * chave[1][i] 
                         + (grupos[2]) * chave[2][i] 
                         + (grupos[3]) * chave[3][i])
                
                #print (f"{grupos[0]} * {chave[0][i]} + {(grupos[1])} * {chave[1][i]} + {(grupos[2])} * {chave[2][i]} + {(grupos[3])} * {chave[3][i]}")
                
                multi.append(linha)
                i += 1

        # print("multi",multi)
        
        resultado.append(multi)

    # print("linhares:",resultado)

    return resultado

### MÉTODO QUE EU FIZ (GUILHERME HENRIQUE) ENQUANTO O MATEUS FAZIA O DELE, OS DOIS FUNCIONAM ENTAO O DO MATEUS VAI SER USADO
def multiplicarMatrizes_NAO_UTILIZADO(grupoChaves, grupoMsg):
    resultado_codificado = []

    for grupo in grupoMsg:
        tamanho = len(grupo)

        # Seleciona a chave correspondente
        if tamanho == 1:
            chave = grupoChaves[0]
        elif tamanho ==2:
            chave = grupoChaves[0]
        elif tamanho == 3:
            chave = grupoChaves[1]
        elif tamanho == 4:
            chave = grupoChaves[2]
        else:
            raise ValueError(f"Grupo de tamanho {tamanho} não suportado (esperado: 2, 3 ou 4)")

        # Multiplicação na mão: grupo (1xN) * chave (NxN)
        linha_resultado = []
        for coluna in range(tamanho):
            soma = 0

            ## i é cada elemento do grupo

            for i in range(tamanho):
                ## aqui ele ta basicamente entrando na chave [i]~(que é a primeira linha da chave) [19, 2, 47]
                ## entao ele seleciona o elemento "coluna" lá dentro, ou seja 19 (por que é a primeira coluna)

                ## logo ele multiplica o primeiro(i) elemento da mensagem * o primeiro(coluna) da primeira linha(chave[i])
                ## quando i atualiza e vira 2, ele ira mult o segundo(i) elemento da msg * o elemento na primeira coluna e segunda linha
                ## i == 3, terceiro da msg * (terceira linha x primeira coluna)

                ## agora que acabou ele irá atualizar a coluna e repetir o processo

                soma += int(grupo[i]) * int(chave[i][coluna])
            
            linha_resultado.append(soma)
            print("linha resultado:",linha_resultado)
            ## é a matriz resultante, nesse caso ele tá juntando os resultados da multiplicação em uma linha, representando
            ## o grupo original de mensagens. ['g', 'u', 'i'], ['l','h','e']...
            ## aqui a linha resultado seria o resultado apenas de [g, u, i]

        resultado_codificado.append(linha_resultado)
        ## aqui é todos os resultados enfileirados [['g', 'u', 'i'](resultado), ['l','h','e'](resultado), [...]]

    return resultado_codificado



# msg = input("Digite a mensagem a ser encriptografada:\n> ")
# chave = input("Digite a chave:\n> ")

# if (len(msg) == 1):
#     grupoMsg = [msg]
# else:
#     grupoMsg = separarMensagem(msg)

# grupoChaves = criarChaves(chave)

# grupoMsgConvertida = converterMensagem(grupoMsg)
# finalcodi = codificarMensagem(grupoMsgConvertida, grupoChaves)

# print("----------------------")
# print("Separada: ", grupoMsg)
# print("chaves:", grupoChaves[0],"\n", grupoChaves[1],"\n", grupoChaves[2])
# print("convertida:", grupoMsgConvertida)
# print("mensagem codificada: ", finalcodi)