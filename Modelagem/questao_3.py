import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from modelagem import Modelagem as mode

def plotagem_3D(lista_solidos, lista_cores, eye, centro_massa):
  x = np.array([-6, 6, 0, 0, 0, 0, 0, 0])
  y = np.array([0, 0, 0, -6, 6, 0, 0, 0])
  z = np.array([0, 0, 0, 0, 0, 0, -6, 6])
  
  fig = plt.figure(figsize=(8,8))
  ax = fig.add_subplot(111, projection = "3d")
  ax.plot(x,y,z, color='black')
  

  for i in range(len(lista_solidos)):
    poly = Poly3DCollection(lista_solidos[i], alpha = 0.5, linewidths = 2, edgecolors = "yellow", facecolor = lista_cores[i])
    ax.add_collection3d(poly)

  ax.scatter3D(eye[0], eye[1], eye[2], color = 'blue')
  ax.scatter3D(centro_massa[0], centro_massa[1], centro_massa[2], color = 'purple')

  ax.set_xlim(-6,6)
  ax.set_ylim(-6,6)
  ax.set_zlim(-6,6)
  ax.set_xlabel("X")
  ax.set_ylabel("Y")
  ax.set_zlabel("Z")
  ax.grid(True)

  plt.show()


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

paralepipido_3D_mudanca_base = mode.translacao(paralelepipedo, x=-5.25, y=-5.5, z=0, qtd_pontos = len(paralelepipedo))
tronco_piramide_3D_mudanca_base = mode.translacao(tronco_piramide,  x=-3.25, y=-4, z=0, qtd_pontos = len(tronco_piramide))

paralepipido_3D = mode.translacao(paralelepipedo, x=-5.25, y=-5.5, z=0, qtd_pontos = len(paralelepipedo))
tronco_piramide_3D = mode.translacao(tronco_piramide,  x=-3.25, y=-4, z=0, qtd_pontos = len(tronco_piramide))

eye = np.array([1,2,-6])
centro_de_massa = np.array([0,0,0])

mode.mudanca_base( [tronco_piramide_3D,paralepipido_3D] , eye , centro_de_massa)

lista_solidos = [ mode.faces_quadrilatero(paralepipido_3D_mudanca_base),
                  mode.faces_quadrilatero(tronco_piramide_3D_mudanca_base),
                  mode.faces_quadrilatero(paralepipido_3D),
                  mode.faces_quadrilatero(tronco_piramide_3D)]

lista_cores = ['green','green','red','red']

plotagem_3D(lista_solidos,lista_cores, eye, centro_de_massa)