from pyscript import document
from numpy import *

def separarMensagem(msg):
    grupos = []
    i = 0
    while i < len(msg):
        restante = len(msg) - i
        
        if restante >= 3:
            grupos.append(msg[i:i+3]) ## aqui vai do atual, até ele mais 2 (por que nao inclui o 3) 
            i += 3
        elif restante >= 2:
            grupos.append(msg[i:i+2]) 
            i += 2
        elif restante == 1:
            grupos[-1] += msg[i]  ## adiciona o último caractere ao último grupo
            break
    return grupos

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

        matriz = empty((linhas, colunas), dtype=str)

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

def acaoBotao(event):
    input_mensagem = document.querySelector("#mensagem")
    input_senha = document.querySelector("#senha")

    mensagem = input_mensagem.value
    senha = input_senha.value

    output_div = document.querySelector("#saida")
    
    # a = array([[1,2],[3,4]])
    # b = linalg.inv(a)

    # output_div.innerText = f"matriz inversa:\n{b}"





    if (len(mensagem) == 1):
        grupoMsg = [mensagem]
    else:
        grupoMsg = separarMensagem(mensagem)

    grupoChaves = criarChaves(senha)

    grupoMsgConvertida = converterMensagem(grupoMsg)
    finalcodi = codificarMensagem(grupoMsgConvertida, grupoChaves)

    msg = ""

    for c in finalcodi:
        for a in c:
            msg += str(a)+" "


    output_div.innerText = msg

    