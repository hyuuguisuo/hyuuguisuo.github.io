from numpy import *

def separarMensagem(msg, is_decod):

    # msg = "2503 1715 1415 1467 1055 1255 2065 1401 1781"

    grupos = []
    i = 0

    if (is_decod == True):
        mensagem = msg.split(" ")
     
        for i in range (0, len(mensagem)):
            mensagem[i] =  int(mensagem[i])

        print(mensagem)
        
        i = 0
        
        while i < len(mensagem):
            restante = len(mensagem) - i

            if restante >= 3:
                grupos.append(mensagem[i:i+3])
                i += 3
            elif restante == 2:
                grupos.append(mensagem[i:i+2])
                i += 2
            elif restante == 1:
                if grupos:
                     grupos[-1].append(mensagem[i])
                else:
                     grupos.append([mensagem[i]])
                break

    else:
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

def converterMensagem(grupomsg, desconverter):
    santoDicionario = {
        " ": 2,  "A": 3,  "B": 5,  "C": 7,  "D": 9,
        "E": 11, "F": 13, "G": 15, "H": 17, "I": 19,
        "J": 21, "K": 23, "L": 25, "M": 27, "N": 29,
        "O": 31, "P": 33, "Q": 35, "R": 37, "S": 39,
        "T": 41, "U": 43, "V": 45, "W": 47, "X": 39,
        "Y": 51, "Z": 53
    }
    malignoDicionario = {
        2: " ",  3: "A",  5: "B",  7: "C",  9: "D",
        11: "E", 13: "F", 15: "G", 17: "H", 19: "I",
        21: "J", 23: "K", 25: "L", 27: "M", 29: "N",
        31: "O", 33: "P", 35: "Q", 37: "R", 39: "S",
        41: "T", 43: "U", 45: "V", 47: "W", 49: "X",
        51: "Y", 53: "Z"
    }
    msgConvertida = []
    
    if (desconverter == True):
        for grupo in grupomsg:
            letras = []

            for numero in grupo:
                if int(numero) in malignoDicionario:
                    letras.append(malignoDicionario[int(numero)])
            
            msgConvertida.append(letras)
    else:
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
def criarChaves():
    chave2x2 = ([[4, 5],
                 [3, 4]])


    chave3x3 = ([[2, 1, 3],
                 [0, 1, 4],
                 [5, 2, 0]])

    chave4x4 = ([[1, 2, 0, 1],  
                 [0, 1, 1, 0],
                 [2, 3, 0, 1],
                 [1, 0, 0, 1]])


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
                
                print (f"{grupos[0]} * {chave[0][i]} + {(grupos[1])} * {chave[1][i]}") 
            
                multi.append(linha)
                i += 1

        if tamanho == 2:
            chave = grupoChaves[0]

            while(i<tamanho):

                linha = ((grupos[0] * chave[0][i]) 
                         + (grupos[1]) * chave[1][i] )
                
                print (f"{grupos[0]} * {chave[0][i]} + {(grupos[1])} * {chave[1][i]}")
                
                multi.append(linha)
                i += 1

        elif tamanho == 3:
            chave = grupoChaves[1]

            while(i<tamanho):

                linha = ((grupos[0] * chave[0][i]) 
                         + (grupos[1]) * chave[1][i] 
                         + (grupos[2]) * chave[2][i] )
                
                print (f"{grupos[0]} * {chave[0][i]} + {(grupos[1])} * {chave[1][i]} + {(grupos[2])} * {chave[2][i]}")
                
                multi.append(linha)
                i += 1

        elif tamanho == 4:
            chave = grupoChaves[2]

            while(i<tamanho):

                linha = ((grupos[0] * chave[0][i]) 
                         + (grupos[1]) * chave[1][i] 
                         + (grupos[2]) * chave[2][i] 
                         + (grupos[3]) * chave[3][i])
                
                print (f"{grupos[0]} * {chave[0][i]} + {(grupos[1])} * {chave[1][i]} + {(grupos[2])} * {chave[2][i]} + {(grupos[3])} * {chave[3][i]}")
                
                multi.append(linha)
                i += 1

        print("multi",multi)
        
        resultado.append(multi)

    print("linhares:",resultado)
    
    return resultado

def inverteChaves(chaveiro):
    chaveiro[0] = (linalg.inv(chaveiro[0])).tolist()
    chaveiro[1] = (linalg.inv(chaveiro[1])).tolist()
    chaveiro[2] = (linalg.inv(chaveiro[2])).tolist()

    chaveiro_inverso = chaveiro

    for c in chaveiro_inverso:
        print("chaveiro invertido",c)

    return chaveiro_inverso


# def acaoDescodificar(event):
#     input_mensagem_descod = document.querySelector("#mensagem")
#     input_senha_descod = document.querySelector("#senha")

#     mensagem_descod = input_mensagem_descod.value
#     senha = input_senha_descod.value

#     output_div = document.querySelector("#saida_descod")
    
#     # a = array([[1,2],[3,4]])
#     # b = linalg.inv(a)

#     # output_div.innerText = f"matriz inversa:\n{b}"





#     if (len(mensagem_descod) == 1):
#         grupoMsg = [mensagem_descod]
#     else:
#         grupoMsg = separarMensagem(mensagem_descod, True)
#         print("grupo msg:", grupoMsg)

#     grupoChaves = criarChaves(senha)

#     chaveiroInvertido = inverteChaves(grupoChaves)

#     multiMsg = codificarMensagem(grupoMsg, chaveiroInvertido)

#     # grupoMsgConvertida = converterMensagem(grupoMsg, True)

#     # finalcodi = codificarMensagem(grupoMsgConvertida, grupoChaves)

#     # msg = ""

#     # for c in finalcodi:
#     #     for a in c:
#     #         msg += str(a)+" "


#     output_div.innerText = multiMsg
def arredondar_lista(matriz):
    nova_matriz = []

    for linha in matriz:
        print("linha", linha)
        nova_linha = []
        for valor in linha:
            print("valor", valor)
            valor_arredondado = round(valor)
            print("valorarre", valor_arredondado)
            nova_linha.append(valor_arredondado)
        nova_matriz.append(nova_linha)

    return nova_matriz


def codificar():
    mensagem = input("Digite a mensagem que deverá ser codificada: \n")

    if (len(mensagem) == 1):
        grupoMsg = [mensagem]
    else:
        grupoMsg = separarMensagem(mensagem, False)

    grupoChaves = criarChaves()

    grupoMsgConvertida = converterMensagem(grupoMsg, False)

    finalcodi = codificarMensagem(grupoMsgConvertida, grupoChaves)

    msg = ""

    for c in finalcodi:
        for a in c:
            msg += str(a)+" "

    print("Mensagem convertida!")
    print(f"> {msg}")


def descodificar():
    mensagem = input("Digite a mensagem que deverá ser descodificada/traduzida: \n")

    if (len(mensagem) == 1):
        grupoMsg = [mensagem]
    else:
        grupoMsg = separarMensagem(mensagem, True)

    grupoChaves = criarChaves()
    chaveiroInvertido = inverteChaves(grupoChaves)
    
    semifinalcodi = codificarMensagem(grupoMsg, chaveiroInvertido)

    print("semifinal:", semifinalcodi)
    
    finale = arredondar_lista(semifinalcodi)

    grupoMsgConvertida = converterMensagem(finale, True)

    print(grupoMsgConvertida)

    print("-----------------------------")
    
    msg = ""

    for c in grupoMsgConvertida:
        for a in c:
            msg += str(a)

    print("Mensagem (des)convertida!")
    print(f"> {msg}")

op = -1

while (op != 0):
    op = int(input("Deseja codificar [1] ou descodificar a mensagem? [2] \n> "))
    
    if op == 0:
        break
    elif op == 1:
        codificar()
    elif op ==2:
        descodificar()
    else:
        print("opção inválida")


# output_div = document.querySelector("#saida")

# # a = array([[1,2],[3,4]])
# # b = linalg.inv(a)

# # output_div.innerText = f"matriz inversa:\n{b}"





# if (len(mensagem) == 1):
#     grupoMsg = [mensagem]
# else:
#     grupoMsg = separarMensagem(mensagem, False)


    # grupoChaves = criarChaves()

    # grupoMsgConvertida = converterMensagem(grupoMsg)
    # finalcodi = codificarMensagem(grupoMsgConvertida, grupoChaves)

    # msg = ""

    # for c in finalcodi:
    #     for a in c:
    #         msg += str(a)+" "

    
    # output_div.innerText = msg

    