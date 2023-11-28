import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from modelagem import Modelagem as mode

def plotagem_3D(faces, cor_solido):
  
  fig = plt.figure(figsize=(8,8))
  ax = fig.add_subplot(111, projection = "3d")

  # Gerando solido em 3D
  poly = Poly3DCollection(faces, alpha = 0.5, linewidths = 2, edgecolors = "yellow", facecolor = cor_solido)
  ax.add_collection3d(poly)

  # Setando os tamanhos de X, Y e Z do Grafico
  ax.set_xlim(-5,5)
  ax.set_ylim(-5,5)
  ax.set_zlim(0,8)

  # Nome dos eixos
  ax.set_xlabel("X")
  ax.set_ylabel("Y")
  ax.set_zlabel("Z")
  ax.grid(True)

  plt.show()

# Passando as coordenadas dos Vertices
piramide = np.array([ [-1.0, -1.0, 0.0],
                      [1.0, -1.0, 0.0],
                      [1.0, 1.0, 0.0],
                      [-1.0, 1.0, 0.0],
                      [0.0, 0.0, 3.0], ])

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

piramide_3D = mode.faces_piramide(piramide)
cubo_3D = mode.faces_quadrilatero(cubo)
paralelepipedo_3D = mode.faces_quadrilatero(paralelepipedo)
tronco_piramide_3D = mode.faces_quadrilatero(tronco_piramide)

plotagem_3D(cubo_3D, 'purple')
plotagem_3D(paralelepipedo_3D, 'green')
plotagem_3D(piramide_3D, 'blue')
plotagem_3D(tronco_piramide_3D, 'red')
