"""
Instituto Politécnico Nacional
Centro de investigación en computación
Maestría en ciencias en ingenieria de computo 

Análisis y diseño de Algoritmos 
Dr. Rolando Quintero Téllez

Corona Elizalde Luis Ángel
"""

from grafo import Grafo
import random
import math

#Modelo Gm,n de malla. 

def grafoMalla(m, n, dirigido=False):
    
    # Crear el grafo g
    g = Grafo()

    # Validar parámetros
    if m <= 1 or n <= 1 or m > 99 or n > 99:
        print("Solo valores mayores que 1 y menores que 100 para m y n")
        return g

    print("Malla(" + str(m) + ", " + str(n) + ")")

    # Agregar m x n nodos al grafo g
    for i in range(m):
        for j in range(n):
            nombrenodo = j * m + i
            g.agreganodo(nombrenodo)

    # Agregar aristas al grafo g hacia la derecha para i < m-1 y hacia abajo para j < n-1
    for i in range(m):
        for j in range(n):
            nombrenodo = j * m + i
            if(i < m-1):
                nombrenodosigi = j*m + i + 1
                g.agregaarista(nombrenodo, nombrenodosigi)
            if(j < n-1):
                nombrenodosigj = (j+1)*m + i
                g.agregaarista(nombrenodo, nombrenodosigj)
    # Regresar el grafo g
    return g

#Modelo Gn,m de Erdös y Rényi. 

def grafoErdosRenyi(n, m, dirigido=False, auto=False):
    
    # Crear el grafo g
    g = Grafo()

    # Validar parámetros
    if n <= 0 or m < n-1:
        print("Solo valores n>0 y m>=n-1")
        return g

    print("ErdosRenyi(" + str(n) + "," + str(m) + ")")

    # Agregar n nodos al grafo g
    for i in range(n):
        g.agreganodo(i)

    # Agregar m aristas al grafo g
    i = 0
    while i < m:
        # Seleccionar un par de nodos al azar
        nodo1 = random.randrange(0, n)
        nodo2 = random.randrange(0, n)
        agregada = 0
        # Si los nodos son diferentes, agregar la arista al grafo g
        if nodo1 != nodo2:
            agregada = g.agregaarista(nodo1, nodo2)
            # Si la arista no agregó porque ya existe, regresar el índice e intentar con otro par
            if agregada == 0:
                i -= 1
        else:
            # Si los nodos son iguales, no agregar arista, regresar el índice e intentar con otro par
            i -= 1
        # Incrementar el índice
        i += 1
    # Regresar el grafo g
    return g

#Modelo Gn,p de Gilbert.

def grafoGilbert(n, p, dirigido=False, auto=False):
    
    # Crear el grafo g
    g = Grafo()

    # Validar parámetros
    if n <= 0 or p<0 or p>1:
        print("Solo valores n>0 y 0<=p<=1")
        return g

    print("Gilbert(" + str(n) + ", " + str(p) + ")")
    # Agregar n nodos
    for nodo in range(n):
        g.agreganodo(nodo)

    # Para todos los pares de nodos diferentes, agregar las posibles aristas con probabilidad p
    for u in range(n):
        for v in range(n):
            if random.random() <= p and u != v:
                agregada = g.agregaarista(u, v)
            else:
                agregada = 0

    # Regresar el grafo g
    return g


"""
Calcular la distancia entre dos nodos por Pitágoras: h = sqrt (a**2 + b**2)
"""


def distancia(n1, n2):
    return math.sqrt((n2.x - n1.x)**2 + (n2.y - n1.y)**2)


#Modelo Gn,r geográfico simple. 

def grafoGeografico(n, r, dirigido=False, auto=False):
    
    # Crear grafo g
    g = Grafo()

    # Validar parámetros
    if n <= 0 or r < 0 or r > 1:
        print("Solo valores n>0 y 0<=r<=1")
        return g

    print("GeograficoSimple(" + str(n) + "," + str(r) + ")")
    # Agregar n nodos al grafo g, cada nodo con coordenadas aleatorias
    for i in range(n):
        if g.agreganodo(i) == 1:
            nodo = g.obtenernodo(i)
            nodo.x = random.random()
            nodo.y = random.random()
    # Para cada par de nodos distintos, agregar la arista al grafo g si la distancia es menor que r
    for i in range(n):
        for j in range(n):
            if i != j:
                d = distancia(g.obtenernodo(i), g.obtenernodo(j))
                if d <= r:
                    g.agregaarista(i, j)
    # Regresar el grafo g
    return g

#Variante del modelo Gn,d Barabási-Albert. 

def grafoBarabasiAlbert(n, d, dirigido=False, auto=False):
    

    # Crear el grafo g
    g = Grafo()

    # Validar parámetros
    if n<=0 or d<=1:
        print("Solo valores n>0 y d>1")
        return g

    print("BarabasiAlbert(" + str(n) + ", " + str(d) + ")")
    # Agregar n nodos al grafo g
    for i in range(n):
        j = 0
        g.agreganodo(i)
        if i >= d:
            # Inicializar el número de aristas agregadas al nuevo nodo
            di = 0
            # Mientras el número de aristas agregadas sea menor que d
            while di < d:
                # Para todos los nodos existentes
                for j in range(i):
                    # La probabilidad es igual al grado del nodo entre la suma de grados de todos los nodos,
                    # que es igual al doble de aristas que tiene el grafo
                    k = g.obtenernodo(j)
                    p = k.grado / (len(g.aristas) * 2)
                    # Si un número aleatorio es menor o igual que la probabilidad del nodo, agregar la arista
                    r = random.random()
                    if r <= p:
                        if g.agregaarista(i, j) == 1:
                            di += 1
                    # Si el número de aristas agregadas es igual a d, salir del ciclo
                    if di == d:
                        break
        else:
            # Si hay de 0 a d nodos, agregar una arista desde el nuevo nodo a todos los existentes
            if i > 0:
                for j in range(i):
                    g.agregaarista(i, j)
    # Regresar el grafo g
    return g


#Modelo Gn Dorogovtsev-Mendes. 

def grafoDorogovtsevMendes(n, dirigido=False):
    
    # Crear el grafo g
    g = Grafo()
    # Validar parámetros
    if n < 3:
        print("Solo valores n>=3")
        return g

    print("DorogovtsevMendes(" + str(n) + ")")
    # Aregar 3 nodos y 3 aristas al grafo g, formando un triángulo
    for i in range(3):
        g.agreganodo(i)
    g.agregaarista(0, 1)
    g.agregaarista(0, 2)
    g.agregaarista(1, 2)
    # Agregar los siguientes nodos desde 3 hasta n al grafo g
    for i in range(3, n):
        g.agreganodo(i)
        # Elegir una arista existente al azar
        idx = random.randrange(0, i)
        a = g.obtenerarista(idx)
        # Agregar aristas entre el nuevo y los extremos de la arista elegida
        g.agregaarista(i, int(a.src))
        g.agregaarista(i, int(a.trg))
    # Regresar el nodo g
    return g





