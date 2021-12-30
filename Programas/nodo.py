"""
Instituto Politécnico Nacional
Centro de investigación en computación
Maestría en ciencias en ingenieria de computo 

Análisis y diseño de Algoritmos 
Dr. Rolando Quintero Téllez

Corona Elizalde Luis Ángel
"""

"""
Clase Nodo, sus propiedades son id, coordenadas y grado, principalmente
"""


class Nodo:

    def __init__(self, nombre, x=0.0, y=0.0, gr=0.0):

        self.id = nombre
        self.x = x
        self.y = y
        self.grado = gr
        self.atrib: {
            ATTR_ESTILO: {
                ESTILO_COLOR: (100, 200, 300),
            },
        }

    def __str__(self):

        return self.id
