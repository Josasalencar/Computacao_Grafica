import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from modelagem import Modelagem as mode

def plotagem_2D(lista_arestas, lista_cores):
  fig = plt.figure(figsize=(8,8))
  ax = fig.add_subplot(111)

  # para substituir a multiplicação pela matriz de projeção paralela utilizamos somente o X e Y
  for i in range(len(lista_arestas)):
      for j in lista_arestas[i]:
        ax.plot(j[:,0], j[:,1], color=lista_cores[i])

  plt.show()

piramide = np.array([ [-1.0, -1.0, 0.0],
                      [1.0,  -1.0, 0.0],
                      [1.0,   1.0, 0.0],
                      [-1.0,  1.0, 0.0],
                      [0.0,   0.0, 3.0], ])

cubo = np.array([ [-0.75, -0.75, 0.0],
                  [0.75, -0.75, 0.0],
                  [0.75, 0.75, 0.0],
                  [-0.75, 0.75, 0.0],
                  [-0.75, -0.75, 1.5],
                  [0.75, -0.75, 1.5],
                  [0.75, 0.75, 1.5],
                  [-0.75, 0.75, 1.5], ])

paralelepipedo = np.array([ [0.0, 0.0, 0.0],
                            [1.5, 0.0, 0.0],
                            [1.5, 5.0, 0.0],
                            [0.0, 5.0, 0.0],
                            [0.0, 0.0, 2.5],
                            [1.5, 0.0, 2.5],
                            [1.5, 5.0, 2.5],
                            [0.0, 5.0, 2.5], ])

tronco_piramide = np.array([ [0.0, 0.0, 0.0],
                             [3.0, 0.0, 0.0],
                             [3.0, 3.0, 0.0],
                             [0.0, 3.0, 0.0],
                             [0.85, 0.85, 2.5],
                             [1.95, 0.85, 2.5],
                             [1.95, 1.95, 2.5],
                             [0.85, 1.95, 2.5], ])

paralepipido_3D = mode.translacao(paralelepipedo, x=-5.25, y=-5.5, z=0, qtd_pontos = len(paralelepipedo))
tronco_piramide_3D = mode.translacao(tronco_piramide,  x=-3.25, y=-4, z=0, qtd_pontos = len(tronco_piramide))

eye = np.array([1,2,-6])
centro_de_massa = np.array([0,0,0])


mode.mudanca_base([tronco_piramide_3D,paralepipido_3D],eye,centro_de_massa)

lista_arestas = [ mode.arestas_quadrilatero(paralepipido_3D),
                  mode.arestas_quadrilatero(tronco_piramide_3D)]

lista_cores = ['green','red']

plotagem_2D(lista_arestas,lista_cores)