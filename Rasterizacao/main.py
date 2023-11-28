import numpy
from matplotlib import pyplot
from matplotlib.colors import ListedColormap
from rasterizacao import Rasterizacao as raste


# 1° reta : (0.2 , 0.2), (0.9 , 0.5)
# Resoluçôes usadas: 40x40, 320x280, 580x420
# Reta |Δx| > |Δy|

resolucao_x_1, resolucao_y_1 = 40, 40
resolucao_x_2, resolucao_y_2 = 320, 280
resolucao_x_3, resolucao_y_3 = 580, 420

p1x, p1y = 0.2, 0.2
p2x, p2y = 0.9, 0.5

matriz = numpy.zeros((resolucao_y_1, resolucao_x_1))
raste.rasteriazacao(p1x, p1y, p2x, p2y, resolucao_x_1, resolucao_y_1, matriz)
raste.plot_rasterizacao_reta(matriz, p1x, p1y, p2x, p2y, resolucao_x_1, resolucao_y_1)

matriz  = numpy.zeros((resolucao_y_2, resolucao_x_2))
raste.rasteriazacao(p1x, p1y, p2x, p2y, resolucao_x_2, resolucao_y_2, matriz)
raste.plot_rasterizacao_reta(matriz, p1x, p1y, p2x, p2y, resolucao_x_2, resolucao_y_2)

matriz = numpy.zeros((resolucao_y_3, resolucao_x_3))
raste.rasteriazacao(p1x, p1y, p2x, p2y, resolucao_x_3, resolucao_y_3, matriz)
raste.plot_rasterizacao_reta(matriz, p1x, p1y, p2x, p2y, resolucao_x_3, resolucao_y_3)


# 2° Reta: (0.2 , 0.2), (0.6, 0.9)
# Resoluçôes usadas: 40x40, 320x280, 580x420
# Reta |Δy| > |Δx|

resolucao_x_1, resolucao_y_1 = 40, 40
resolucao_x_2, resolucao_y_2 = 320, 280
resolucao_x_3, resolucao_y_3 = 580, 420

p1x, p1y = 0.2, 0.2
p2x, p2y = 0.6, 0.9

matriz = numpy.zeros((resolucao_y_1, resolucao_x_1))
raste.rasteriazacao(p1x, p1y, p2x, p2y, resolucao_x_1, resolucao_y_1, matriz)
raste.plot_rasterizacao_reta(matriz, p1x, p1y, p2x, p2y, resolucao_x_1, resolucao_y_1)

matriz = numpy.zeros((resolucao_y_2, resolucao_x_2))
raste.rasteriazacao(p1x, p1y, p2x, p2y, resolucao_x_2, resolucao_y_2, matriz)
raste.plot_rasterizacao_reta(matriz, p1x, p1y, p2x, p2y, resolucao_x_2, resolucao_y_2)

matriz = numpy.zeros((resolucao_y_3, resolucao_x_3))
raste.rasteriazacao(p1x, p1y, p2x, p2y, resolucao_x_3, resolucao_y_3, matriz)
raste.plot_rasterizacao_reta(matriz, p1x, p1y, p2x, p2y, resolucao_x_3, resolucao_y_3)

# 3° Reta: (0.4 , 0.2), (0.4, 0.8)
# Resoluçôes usadas: 40x40, 320x280, 580x420
# Reta Vertical

resolucao_x_1, resolucao_y_1 = 40, 40
resolucao_x_2, resolucao_y_2 = 320, 280
resolucao_x_3, resolucao_y_3 = 580, 420

p1x, p1y = 0.4, 0.2
p2x, p2y = 0.4, 0.8

matriz = numpy.zeros((resolucao_y_1, resolucao_x_1))
raste.rasteriazacao(p1x, p1y, p2x, p2y, resolucao_x_1, resolucao_y_1, matriz)
raste.plot_rasterizacao_reta(matriz, p1x, p1y, p2x, p2y, resolucao_x_1, resolucao_y_1)

matriz = matriz = numpy.zeros((resolucao_y_2, resolucao_x_2))
raste.rasteriazacao(p1x, p1y, p2x, p2y, resolucao_x_2, resolucao_y_2, matriz)
raste.plot_rasterizacao_reta(matriz, p1x, p1y, p2x, p2y, resolucao_x_2, resolucao_y_2)

matriz = numpy.zeros((resolucao_y_3, resolucao_x_3))
raste.rasteriazacao(p1x, p1y, p2x, p2y, resolucao_x_3, resolucao_y_3, matriz)
raste.plot_rasterizacao_reta(matriz, p1x, p1y, p2x, p2y, resolucao_x_3, resolucao_y_3)

# 4° Reta: (0.2 , 0.4), (0.8, 0.4)
# Resoluçôes usadas: 40x40, 320x280, 580x420
# Reta Horizontal

resolucao_x_1, resolucao_y_1 = 40, 40
resolucao_x_2, resolucao_y_2 = 320, 280
resolucao_x_3, resolucao_y_3 = 580, 420

p1x, p1y = 0.2, 0.4
p2x, p2y = 0.8, 0.4

matriz = numpy.zeros((resolucao_y_1, resolucao_x_1))
raste.rasteriazacao(p1x, p1y, p2x, p2y, resolucao_x_1, resolucao_y_1, matriz)
raste.plot_rasterizacao_reta(matriz, p1x, p1y, p2x, p2y, resolucao_x_1, resolucao_y_1)

matriz = numpy.zeros((resolucao_y_2, resolucao_x_2))
raste.rasteriazacao(p1x, p1y, p2x, p2y, resolucao_x_2, resolucao_y_2, matriz)
raste.plot_rasterizacao_reta(matriz, p1x, p1y, p2x, p2y, resolucao_x_2, resolucao_y_2)

matriz = numpy.zeros((resolucao_y_3, resolucao_x_3))
raste.rasteriazacao(p1x, p1y, p2x, p2y, resolucao_x_3, resolucao_y_3, matriz)
raste.plot_rasterizacao_reta(matriz, p1x, p1y, p2x, p2y, resolucao_x_3, resolucao_y_3)

# 1° Triangulo Equilatero:  (0.1, 0.1), ( 0.7, 0.1), (0.4, 0.6)
# Resolução: 100x100, 300x300, 600x600


resolucao_x_1, resolucao_y_1 = 50, 50
resolucao_x_2, resolucao_y_2 = 300, 300
resolucao_x_3, resolucao_y_3 = 600, 600

p1x, p1y = 0.1, 0.1
p2x, p2y = 0.7, 0.1
p3x, p3y = 0.4, 0.6


matriz = numpy.zeros((resolucao_y_1, resolucao_x_1))
matriz_poligono =  numpy.zeros((resolucao_y_1, resolucao_x_1))
raste.rasterização_triangulo(raste,p1x, p1y, p2x, p2y ,p3x, p3y, resolucao_x_1, resolucao_y_1, matriz)
raste.pixels_poligono(matriz,matriz_poligono)
raste.plot_rasterizacao_poligono(matriz_poligono,resolucao_x_1,resolucao_y_1,'Triangulo Equilatero')

matriz = numpy.zeros((resolucao_y_2, resolucao_x_2))
matriz_poligono = numpy.zeros((resolucao_y_2, resolucao_x_2))
raste.rasterização_triangulo(raste,p1x, p1y, p2x, p2y ,p3x, p3y, resolucao_x_2, resolucao_y_2, matriz)
raste.pixels_poligono(matriz,matriz_poligono)
raste.plot_rasterizacao_poligono(matriz_poligono,resolucao_x_2,resolucao_y_2,'Triangulo Equilatero')

matriz = numpy.zeros((resolucao_y_3, resolucao_x_3))
matriz_poligono = numpy.zeros((resolucao_y_3, resolucao_x_3))
raste.rasterização_triangulo(raste,p1x, p1y, p2x, p2y ,p3x, p3y, resolucao_x_3, resolucao_y_3, matriz)
raste.pixels_poligono(matriz,matriz_poligono)
raste.plot_rasterizacao_poligono(matriz_poligono,resolucao_x_3,resolucao_y_3,'Triangulo Equilatero')


# 2° Triangulo Equilatero:  (0.2, 0.2), ( 0.8, 0.2), (0.5, 0.7)
# Resolução: 50x50, 300x300, 600x600

resolucao_x_1, resolucao_y_1 = 50, 50
resolucao_x_2, resolucao_y_2 = 300, 300
resolucao_x_3, resolucao_y_3 = 600, 600

p1x, p1y = 0.2, 0.2
p2x, p2y = 0.8, 0.2
p3x, p3y = 0.5, 0.7

matriz = numpy.zeros((resolucao_y_1, resolucao_x_1))
matriz_poligono =  numpy.zeros((resolucao_y_1, resolucao_x_1))
raste.rasterização_triangulo(raste,p1x, p1y, p2x, p2y ,p3x, p3y, resolucao_x_1, resolucao_y_1, matriz)
raste.pixels_poligono(matriz,matriz_poligono)
raste.plot_rasterizacao_poligono(matriz_poligono,resolucao_x_1,resolucao_y_1,'Triangulo Equilatero')

matriz = numpy.zeros((resolucao_y_2, resolucao_x_2))
matriz_poligono = numpy.zeros((resolucao_y_2, resolucao_x_2))
raste.rasterização_triangulo(raste,p1x, p1y, p2x, p2y ,p3x, p3y, resolucao_x_2, resolucao_y_2, matriz)
raste.pixels_poligono(matriz,matriz_poligono)
raste.plot_rasterizacao_poligono(matriz_poligono,resolucao_x_2,resolucao_y_2,'Triangulo Equilatero')

matriz = numpy.zeros((resolucao_y_3, resolucao_x_3))
matriz_poligono = numpy.zeros((resolucao_y_3, resolucao_x_3))
raste.rasterização_triangulo(raste,p1x, p1y, p2x, p2y ,p3x, p3y, resolucao_x_3, resolucao_y_3, matriz)
raste.pixels_poligono(matriz,matriz_poligono)
raste.plot_rasterizacao_poligono(matriz_poligono,resolucao_x_3,resolucao_y_3,'Triangulo Equilatero')

# 1° Quadrado:  (0.1, 0.1), (0.1, 0.3), (0.3, 0.3), (0.3, 0.1)
# Resolução: 50x50, 300x300, 600x600


resolucao_x_1, resolucao_y_1 = 50, 50
resolucao_x_2, resolucao_y_2 = 300, 300
resolucao_x_3, resolucao_y_3 = 600, 600

p1x, p1y = 0.1, 0.1 
p2x, p2y = 0.1, 0.3
p3x, p3y = 0.3, 0.3
p4x, p4y = 0.3, 0.1

matriz = numpy.zeros((resolucao_y_1, resolucao_x_1))
matriz_poligono =  numpy.zeros((resolucao_y_1, resolucao_x_1))
raste.rasterizcao_quadrado(raste, p1x, p1y, p2x, p2y ,p3x, p3y, p4x, p4y, resolucao_x_1, resolucao_y_1, matriz)
raste.pixels_poligono(matriz,matriz_poligono)
raste.plot_rasterizacao_poligono(matriz_poligono,resolucao_x_1,resolucao_y_1,' Quadrado ')

matriz = numpy.zeros((resolucao_y_2, resolucao_x_2))
matriz_poligono =  numpy.zeros((resolucao_y_2, resolucao_x_2))
raste.rasterizcao_quadrado(raste,p1x, p1y, p2x, p2y ,p3x, p3y, p4x, p4y, resolucao_x_2, resolucao_y_2, matriz)
raste.pixels_poligono(matriz,matriz_poligono)
raste.plot_rasterizacao_poligono(matriz_poligono,resolucao_x_2,resolucao_y_2,' Quadrado ')

matriz = numpy.zeros((resolucao_y_3, resolucao_x_3))
matriz_poligono =  numpy.zeros((resolucao_y_3, resolucao_x_3))
raste.rasterizcao_quadrado(raste,p1x, p1y, p2x, p2y ,p3x, p3y, p4x, p4y, resolucao_x_3, resolucao_y_3, matriz)
raste.pixels_poligono(matriz,matriz_poligono)
raste.plot_rasterizacao_poligono(matriz_poligono,resolucao_x_3,resolucao_y_3,' Quadrado ')


# 2° Quadrado:  (0.2, 0.2), (0.2, 0.8), (0.8, 0.8), (0.8, 0.2)
# Resolução: 50x50, 300x300, 600x600


resolucao_x_1, resolucao_y_1 = 50, 50
resolucao_x_2, resolucao_y_2 = 300, 300
resolucao_x_3, resolucao_y_3 = 600, 600

p1x, p1y = 0.2, 0.2 
p2x, p2y = 0.2, 0.8
p3x, p3y = 0.8, 0.8
p4x, p4y = 0.8, 0.2

matriz = numpy.zeros((resolucao_y_1, resolucao_x_1))
matriz_poligono =  numpy.zeros((resolucao_y_1, resolucao_x_1))
raste.rasterizcao_quadrado(raste, p1x, p1y, p2x, p2y ,p3x, p3y, p4x, p4y, resolucao_x_1, resolucao_y_1, matriz)
raste.pixels_poligono(matriz,matriz_poligono)
raste.plot_rasterizacao_poligono(matriz_poligono,resolucao_x_1,resolucao_y_1,' Quadrado ')

matriz = numpy.zeros((resolucao_y_2, resolucao_x_2))
matriz_poligono =  numpy.zeros((resolucao_y_2, resolucao_x_2))
raste.rasterizcao_quadrado(raste,p1x, p1y, p2x, p2y ,p3x, p3y, p4x, p4y, resolucao_x_2, resolucao_y_2, matriz)
raste.pixels_poligono(matriz,matriz_poligono)
raste.plot_rasterizacao_poligono(matriz_poligono,resolucao_x_2,resolucao_y_2,' Quadrado ')

matriz = numpy.zeros((resolucao_y_3, resolucao_x_3))
matriz_poligono =  numpy.zeros((resolucao_y_3, resolucao_x_3))
raste.rasterizcao_quadrado(raste,p1x, p1y, p2x, p2y ,p3x, p3y, p4x, p4y, resolucao_x_3, resolucao_y_3, matriz)
raste.pixels_poligono(matriz,matriz_poligono)
raste.plot_rasterizacao_poligono(matriz_poligono,resolucao_x_3,resolucao_y_3,' Quadrado ')

# 1° Hexagono:  (0.2, 0.6), (0.4, 0.6), (0.5, 0.4), (0.4, 0.2), (0.2, 0.2), (0.1, 0.4)
# Resolução: 50x50, 300x300, 600x600


resolucao_x_1, resolucao_y_1 = 50, 50
resolucao_x_2, resolucao_y_2 = 300, 300
resolucao_x_3, resolucao_y_3 = 600, 600

p1x, p1y = 0.2, 0.6 
p2x, p2y = 0.4, 0.6
p3x, p3y = 0.5, 0.4
p4x, p4y = 0.4, 0.2
p5x, p5y = 0.2, 0.2
p6x, p6y = 0.1, 0.4

matriz = numpy.zeros((resolucao_y_1, resolucao_x_1))
matriz_poligono =  numpy.zeros((resolucao_y_1, resolucao_x_1))
raste.rasterizacao_hexgono(raste,p1x, p1y, p2x, p2y, p3x, p3y, p4x, p4y, p5x, p5y, p6x, p6y, resolucao_x_1, resolucao_y_1, matriz)
raste.pixels_poligono(matriz,matriz_poligono)
raste.plot_rasterizacao_poligono(matriz_poligono,resolucao_x_1,resolucao_y_1,' Hexagono ')

matriz = numpy.zeros((resolucao_y_2, resolucao_x_2))
matriz_poligono =  numpy.zeros((resolucao_y_2, resolucao_x_2))
raste.rasterizacao_hexgono(raste,p1x, p1y, p2x, p2y, p3x, p3y, p4x, p4y, p5x, p5y, p6x, p6y, resolucao_x_2, resolucao_y_2, matriz)
raste.pixels_poligono(matriz,matriz_poligono)
raste.plot_rasterizacao_poligono(matriz_poligono,resolucao_x_2,resolucao_y_2,' Hexagono ')

matriz = numpy.zeros((resolucao_y_3, resolucao_x_3))
matriz_poligono =  numpy.zeros((resolucao_y_3, resolucao_x_3))
raste.rasterizacao_hexgono(raste,p1x, p1y, p2x, p2y, p3x, p3y, p4x, p4y, p5x, p5y, p6x, p6y, resolucao_x_3, resolucao_y_3, matriz)
raste.pixels_poligono(matriz,matriz_poligono)
raste.plot_rasterizacao_poligono(matriz_poligono,resolucao_x_3,resolucao_y_3,' Hexagono ')


# 2° Hexagono:  (0.1, 0.2), (0.2, 0.1), (0.3, 0.1), (0.4, 0.2), (0.3, 0.3), (0.2, 0.3)
# Resolução: 50x50, 300x300, 600x600


resolucao_x_1, resolucao_y_1 = 50, 50
resolucao_x_2, resolucao_y_2 = 300, 300
resolucao_x_3, resolucao_y_3 = 600, 600

p1x, p1y = 0.3, 0.7 
p2x, p2y = 0.5, 0.7
p3x, p3y = 0.6, 0.5
p4x, p4y = 0.5, 0.3
p5x, p5y = 0.3, 0.3
p6x, p6y = 0.2, 0.5

matriz = numpy.zeros((resolucao_y_1, resolucao_x_1))
matriz_poligono =  numpy.zeros((resolucao_y_1, resolucao_x_1))
raste.rasterizacao_hexgono(raste,p1x, p1y, p2x, p2y, p3x, p3y, p4x, p4y, p5x, p5y, p6x, p6y, resolucao_x_1, resolucao_y_1, matriz)
raste.pixels_poligono(matriz,matriz_poligono)
raste.plot_rasterizacao_poligono(matriz_poligono,resolucao_x_1,resolucao_y_1,' Hexagono ')

matriz = numpy.zeros((resolucao_y_2, resolucao_x_2))
matriz_poligono =  numpy.zeros((resolucao_y_2, resolucao_x_2))
raste.rasterizacao_hexgono(raste,p1x, p1y, p2x, p2y, p3x, p3y, p4x, p4y, p5x, p5y, p6x, p6y, resolucao_x_2, resolucao_y_2, matriz)
raste.pixels_poligono(matriz,matriz_poligono)
raste.plot_rasterizacao_poligono(matriz_poligono,resolucao_x_2,resolucao_y_2,' Hexagono ')

matriz = numpy.zeros((resolucao_y_3, resolucao_x_3))
matriz_poligono =  numpy.zeros((resolucao_y_3, resolucao_x_3))
raste.rasterizacao_hexgono(raste,p1x, p1y, p2x, p2y, p3x, p3y, p4x, p4y, p5x, p5y, p6x, p6y, resolucao_x_3, resolucao_y_3, matriz)
raste.pixels_poligono(matriz,matriz_poligono)
raste.plot_rasterizacao_poligono(matriz_poligono,resolucao_x_3,resolucao_y_3,' Hexagono ')
