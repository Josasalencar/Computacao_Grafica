
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from mpl_toolkits.mplot3d.art3d import Poly3DCollection


def multiplica_3x4(matriz_3, matriz_4):
    matriz_3 = np.hstack((matriz_3, np.ones((len(matriz_3), 1))))
    matriz_3 = np.dot(matriz_3, matriz_4)
    matriz_3 = np.delete(matriz_3, 3, axis=1)
    return matriz_3

class Modelagem:

  # Criando as Faces para Piramide
  def faces_piramide(pontos):
    P = pontos
    faces = [ [P[0], P[1], P[2], P[3]],
              [P[0], P[1], P[4]],
              [P[0], P[3], P[4]],
              [P[2], P[1], P[4]],
              [P[2], P[3], P[4]], ]
    return faces

  # Criando as faces para Quadrilatero
  def faces_quadrilatero(pontos):
    P = pontos
    faces = [ [P[0], P[1], P[2],P[3] ],
              [P[5], P[4], P[7],P[6] ],
              [P[0], P[1], P[5],P[4] ],
              [P[2], P[6], P[7],P[3] ],
              [P[1], P[2], P[6],P[5] ],
              [P[0], P[3], P[7],P[4] ], ]
    return faces

  def arestas_quadrilatero(pontos):
    P = pontos
    arestas = np.array([ [P[0], P[1]],
                         [P[1], P[2]],
                         [P[2], P[3]],
                         [P[3], P[0]],
                         [P[0], P[4]],
                         [P[1], P[5]],
                         [P[2], P[6]],
                         [P[3], P[7]],
                         [P[4], P[5]],
                         [P[5], P[6]],
                         [P[6], P[7]],
                         [P[7], P[4]], ])
    return arestas

  def translacao(solido, x, y, z, qtd_pontos):

    matriz_homogenea = np.ones((qtd_pontos, 4))

    # tranformando em coordenadas homogeneas
    for i in range(qtd_pontos):
      for j in range(3):
        matriz_homogenea[i][j] = solido[i][j]

    # matriz de tranlação 
    matriz_de_translacao = np.array([ [1, 0, 0, x],
                                      [0, 1, 0, y],
                                      [0, 0, 1, z],
                                      [0, 0, 0, 1], ])

    aux = np.dot(matriz_de_translacao, matriz_homogenea.T)
    aux = aux.T

    matriz_transladada = np.ndarray((qtd_pontos, 3))
    
    #prenchenado a matriz transladada
    for i in range(qtd_pontos):
      for j in range(3):
        matriz_transladada[i][j] = aux[i][j]

    return matriz_transladada

  def mudanca_base(solido, eye, centro_de_massa):

    # Centro de massa
    at = (np.mean(solido[0], axis=0) + np.mean(solido[1],axis=0)) / 2

    centro_de_massa[0] = at[0]
    centro_de_massa[1] = at[1]
    centro_de_massa[2] = at[2]

    # Gerando os vetores do sistema de coordenada da camera
    N = np.subtract(at, eye)
    N = N/np.linalg.norm(N)

    aux = [1, 2, -3]

    V = np.cross(N, aux)
    V = V/np.linalg.norm(V)

    U = np.cross(N, V)
    U = U/np.linalg.norm(U)
    
    RT = np.array([[U[0], U[1], U[2], -(eye[0]*U[0])-(eye[1]*U[1])-(eye[2]*U[2])],
                   [V[0], V[1], V[2], -(eye[0]*V[0])-(eye[1]*V[1])-(eye[2]*V[2])],
                   [N[0], N[1], N[2], -(eye[0]*N[0])-(eye[1]*N[1])-(eye[2]*N[2])],
                   [0, 0, 0, 1]])  
  

    solido_mudado_0 = multiplica_3x4(solido[0],RT)
  
    solido_mudado_1 = multiplica_3x4(solido[1],RT)
    
    for i in range(len(solido[0])):
      for j in range(3):
        solido[0][i,j] = solido_mudado_0[i,j]

    for i in range(len(solido[1])):
      for j in range(3):
        solido[1][i,j] = solido_mudado_1[i,j]

    return solido

