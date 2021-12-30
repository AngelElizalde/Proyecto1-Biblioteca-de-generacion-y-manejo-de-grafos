"""
Instituto Politécnico Nacional
Centro de investigación en computación
Maestría en ciencias en ingenieria de computo 

Análisis y diseño de Algoritmos 
Dr. Rolando Quintero Téllez

Corona Elizalde Luis Ángel
"""

"""
Clase Arista, sus propiedades son id y vértices
"""


class Arista:

    def __init__(self, id, source, target):

        self.id = id
        self.src = source
        self.trg = target

    def __str__(self):

        return str(self.id)
