from pyscript import when, document

def verificarFormacao(n1: int, n2: int, n3:int):
    if n1 > n2:
        maiorL = n1
        soma = (n2 + n3)
    else:
        maiorL = n2
        soma = (n1 + n3)
    
    if maiorL < n3:
        maiorL = n3
        soma = (n1 + n2)

    print(n1, n2, n3, maiorL, soma)
    
    if soma > maiorL:
        if n1 == n2 and n2 == n3:
            return f"Forma um triângulo equilátero (todos os lados iguais)  !"

        elif n1 != n2 and n2 != n3:
            return f"Forma um triângulo escaleno (todos os lados diferentes), parabéns !"
        
        else:
            return f"Forma um triângulo isóceles (dois lados iguais) ! ! !"
    
    else:
        return f"É 🍅 impossível 🍅🍅 formar 🍅 um 🍅🍅 triângulo 🍅🍅🍅 assim. (-_-) 🍅🍅🍅🍅🍅🍅🍅"

    
verificarFormacao(5, 2, 5)


@when("click", "#acaoBotao")
def acaoBotao(event):
    input_n1 = document.querySelector("#medida_um")
    input_n2 = document.querySelector("#medida_dois")
    input_n3 = document.querySelector("#medida_tres")

    n1 = int(input_n1.value)
    n2 = int(input_n2.value)
    n3 = int(input_n3.value)
    

    output_div = document.querySelector("#saida")
    output_div.innerText = verificarFormacao(n1, n2, n3)
