"""
Instituto Politécnico Nacional
Centro de investigación en computación
Maestría en ciencias en ingenieria de computo 

Análisis y diseño de Algoritmos 
Dr. Rolando Quintero Téllez

Corona Elizalde Luis Ángel
"""

import algoritmos

"""
Generador los grafos.
"""

if __name__ == '__main__':

    #Malla
    gM = algoritmos.grafoMalla(6, 5)
    gM.muestragv()
    gM = algoritmos.grafoMalla(10, 10)
    gM.muestragv()
    gM = algoritmos.grafoMalla(25, 20)
    gM.muestragv()
   

    #Erdos y Renyi 
    gE = algoritmos.grafoErdosRenyi(30, 40)
    gE.muestragv()
    gE = algoritmos.grafoErdosRenyi(100, 150)
    gE.muestragv()
    gE = algoritmos.grafoErdosRenyi(500, 700)
    gE.muestragv()
    
    
    #Gilbert 
    gG = algoritmos.grafoGilbert(30, 0.5)
    gG.muestragv()
    gG = algoritmos.grafoGilbert(100, 0.2)
    gG.muestragv()
    gG = algoritmos.grafoGilbert(500, 0.01)
    gG.muestragv()
    

    #Geográfico simple
    gS = algoritmos.grafoGeografico(30, 0.5)
    gS.muestragvpos()
    gS = algoritmos.grafoGeografico(100, 0.2)
    gS.muestragvpos()
    gS = algoritmos.grafoGeografico(500, 0.1)
    gS.muestragvpos()
    

    #Barabasi-Albert
    gB = algoritmos.grafoBarabasiAlbert(30, 2)
    gB.muestragv()
    gB = algoritmos.grafoBarabasiAlbert(100, 2)
    gB.muestragv()
    gB = algoritmos.grafoBarabasiAlbert(500, 2)
    gB.muestragv()
    

    #Dorogovtsev-Mendes
    gD = algoritmos.grafoDorogovtsevMendes(30)
    gD.muestragv()
    gD = algoritmos.grafoDorogovtsevMendes(100)
    gD.muestragv()
    gD = algoritmos.grafoDorogovtsevMendes(500)
    gD.muestragv()



