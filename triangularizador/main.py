from pyscript import when, document
from matplotlib.patches import Polygon
from pyscript import display
import numpy as np
import matplotlib.pyplot as plt

def piramidar_comangulos(a1, a2, a3):
    container = document.getElementById("meu-grafico2")
    container.innerHTML = ""
    verificacao=a1+a2+a3

    clean()
    if( verificacao== 180 ):
        if(a1!=a2 and  a2!=a3 and a1!=a3 ):
            document.getElementById("val-tipo").innerText = f"Escaleno"
            container.innerText = "É possível formar um triângulo ESCALENO a partir desses três ângulos."    
            
        elif (a1==a2 and a1!=a3 or a1==a3 and a1!=a2 or a2==a3 ):
            print("É um triângulo isósceles ")
            document.getElementById("val-tipo").innerText = f"Isóceles"
            container.innerText = "É possível formar um triângulo ISÓCELES a partir desses três ângulos."    
            

        elif(a1==a2==a3):
            document.getElementById("val-tipo").innerText = f"Equilátero"
            container.innerText = "É possível formar um triângulo EQUILÁTERO a partir desses três ângulos."    
            print("Triângulo equilátero")   
        
        document.getElementById("val-a").innerText = f"{a1}°"
        document.getElementById("val-b").innerText = f"{a2}°"
        document.getElementById("val-c").innerText = f"{a3}°"

    else:
        container.innerText = "Não é possível formar quaisquer triângulos partir desses três ângulos."    
        print("Não é um triângulo")


def piramidar_comlados(a, b, c):
    container = document.getElementById("meu-grafico")
    container.innerHTML = ""

    A = (0, 0)
    B = (c, 0)
    x = (a**2 + c**2 - b**2) / (2 * c)
    y = np.sqrt(a**2 - x**2)
    C = (x, y)

    fig, ax = plt.subplots()
    vertices = np.array([A, B, C])

    triangulo = Polygon(vertices, closed=True, facecolor="#96f8ff", edgecolor='#008cff')
    ax.add_patch(triangulo)

    bari = (((A[0]+B[0]+C[0])/3),((A[1]+B[1]+C[1])/3))

    meioAB = ((c/2), 0)
    meioBC = (((c+C[0])/2), ((C[1])/2))
    meioCA = (((C[0])/2), ((C[1])/2))

    maiorx = max(A[0], B[0], C[0])
    maiory = max(A[1], B[1], C[1])

    menorx = min(A[0], B[0], C[0])
    menory = min(A[1], B[1], C[1])

    margemx = (maiorx - menorx) * 0.1
    margemy = (maiory - menory) * 0.1

    ax.set_xlim(menorx - margemx, maiorx + margemx)
    ax.set_ylim(menory - margemy, maiory + margemy)
    ax.set_aspect('equal')


    plt.plot([C[0], meioAB[0]], [C[1], meioAB[1]], color="gray", linestyle=':', linewidth=1)
    plt.plot([A[0], meioBC[0]], [A[1], meioBC[1]], color="gray", linestyle=':', linewidth=1)
    plt.plot([B[0], meioCA[0]], [B[1], meioCA[1]], color="gray", linestyle=':', linewidth=1)

    plt.scatter(bari[0], bari[1], color="#ff0055", marker="x")
    ax.tick_params(axis='x', colors="#2e25b3")
    ax.tick_params(axis='y', colors="#2e25b3")

    # ############### #

    ax.spines['bottom'].set_color("#2e25b3")
    ax.spines['top'].set_color("#2e25b3")
    ax.spines['right'].set_color("#2e25b3")
    ax.spines['left'].set_color("#2e25b3")
    fig.patch.set_facecolor('none')


    perimetro = a + b + c
    semi_p = perimetro / 2

    area = np.sqrt(semi_p * (semi_p - a) * (semi_p - b) * (semi_p - c))
    
    g_x = (A[0] + B[0] + C[0]) / 3
    g_y = (A[1] + B[1] + C[1]) / 3

    document.getElementById("val-a").innerText = f"{a:.2f}m"
    document.getElementById("val-b").innerText = f"{b:.2f}m"
    document.getElementById("val-c").innerText = f"{c:.2f}m"
    
    document.getElementById("val-area").innerText = f"{area:.2f}m²"
    document.getElementById("val-perim").innerText = f"{perimetro:.2f}m"
    document.getElementById("val-semi").innerText = f"{semi_p:.2f}m"

    # ############### #

    display(fig, target="meu-grafico")
    plt.close(fig)


def piramidar_comlado3s(a, b, c):
    
    A = (0, 0)
    B = (c, 0)


    x = (a**2 + c**2 - b**2) / (2 * c)
    y = np.sqrt(a**2 - x**2)
    C = (x, y)
    

    fig, ax = plt.subplots(figsize=(5, 4))
    vertices = np.array([A, B, C])

    triangulo = Polygon(vertices, closed=True, facecolor="#96f8ff", edgecolor='#008cff')
    ax.add_patch(triangulo)


    maiorx = max(A[0], B[0], C[0])
    maiory = max(A[1], B[1], C[1])
    distanciax = (30 * maiorx) / 100
    distanciay = (30 * maiory) / 100

    ax.set_xlim(0, maiorx + distanciax)
    ax.set_ylim(0, maiory + distanciay)
    ax.set_aspect('equal')

    
    
    display(fig, target="meu-grafico")
    plt.close(fig)


def piramidar():
    fig, ax = plt.subplots()

    x1 = 5
    y1 = 5 // 3

    x2 = 7
    y2 = 5 // 4

    x3 = 7 // 4
    y3 = 1

    maiorx = max(x1, x2, x3)
    maiory = max(y1, y2, y3)

    distanciax = (30*maiorx) /100
    distanciay = (30*maiory) /100

    vertices = np.array([[x1, y1], [x2, y2], [x3, y3]])

    le_triangulo = Polygon(vertices, closed=True, facecolor="#96f8ff", edgecolor='#008cff')
    ax.add_patch(le_triangulo)
    
    ax.set_xlim(0, maiorx + distanciax)
    ax.set_ylim(0, maiory + distanciay)
    ax.set_aspect('equal')

    display(plt, target="meu-grafico")

def clean():
    document.getElementById("val-a").innerText = f"--"
    document.getElementById("val-b").innerText = f"--"
    document.getElementById("val-c").innerText = f"--"
    
    document.getElementById("val-tipo").innerText = f"--"

    document.getElementById("val-area").innerText = f"--"
    document.getElementById("val-perim").innerText = f"--"
    document.getElementById("val-semi").innerText = f"--"
    
def verificarFormacao(n1: float, n2: float, n3:float):
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
            document.getElementById("val-tipo").innerText = f"Equilátero"
            piramidar_comlados(n1, n2, n3)
            # return f"Forma um triângulo equilátero (todos os lados iguais)  !"

        elif n1 != n2 and n2 != n3:
            piramidar_comlados(n1, n2, n3)
            document.getElementById("val-tipo").innerText = f"Escaleno"
            # return f"Forma um triângulo escaleno (todos os lados diferentes), parabéns !"
        
        else:
            piramidar_comlados(n1, n2, n3)
            document.getElementById("val-tipo").innerText = f"Isóceles"
            # return f"Forma um triângulo isóceles (dois lados iguais) ! ! !"
    
    else:
        clean()

        container = document.getElementById("meu-grafico")
        container.innerHTML = ""
        container.innerText = "É impossível formar um triângulo a partir dessas três medidas. 🍅 🍅 🍅"

@when("click", "#acaoBotao2")
def acaoBotao2(event):
    container = document.getElementById("meu-grafico2")
    try:
        a1 = float(document.getElementById("angulo_a1").value)
        a2 = float(document.getElementById("angulo_a2").value)
        a3 = float(document.getElementById("angulo_a3").value)
    except ValueError:
        container.innerHTML = "Por favor, insira ângulos válidos."
        return
    
    piramidar_comangulos(a1, a2, a3)

@when("click", "#acaoBotao")
def acaoBotao(event):

    container = document.getElementById("meu-grafico")

    try:
        a = float(document.getElementById("lado_a").value)
        b = float(document.getElementById("lado_b").value)
        c = float(document.getElementById("lado_c").value)
    except ValueError:
        container.innerHTML = "Por favor, insira números válidos."
        return
    
    
    verificarFormacao(a, b, c)
    

