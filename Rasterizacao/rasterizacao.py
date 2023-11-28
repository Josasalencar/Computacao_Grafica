import numpy
from matplotlib import pyplot
from matplotlib.colors import ListedColormap

class Rasterizacao :
 
  def rasteriazacao(ponto_1_x, ponto_1_y, ponto_2_x, ponto_2_y, resolucao_x, resolucao_y, matriz):

    # Pega as coordenadas e ajusta de acordo com a resolução
    ponto_1_x *= resolucao_x
    ponto_1_y *= resolucao_y
    ponto_2_x *= resolucao_x
    ponto_2_y *= resolucao_y

    
    # Inicializa 
    x_inicial, x_final = int(min(ponto_1_x, ponto_2_x)), int(max(ponto_1_x, ponto_2_x))
    y_inicial, y_final = int(min(ponto_1_y, ponto_2_y)), int(max(ponto_1_y, ponto_2_y))
    dx = ponto_2_x - ponto_1_x
    dy = ponto_2_y - ponto_1_y

    # Reta Vertical 
    if dx == 0: 
      while y_inicial <= y_final:
        matriz[y_inicial][x_inicial] = 1
        y_inicial += 1 

    # Reta Horizontal
    elif dy == 0: 
      while x_inicial <= x_final:
        matriz[y_inicial][x_inicial] = 1
        x_inicial += 1

    else:
      # Inicializa
      m = dy / dx # Coeficiente Angular
      b =  ponto_1_y - m * ponto_1_x # Coeficiante Linear
      
      # 𝑦 = 𝑚𝑥 + b

      # Reta |Δx| > |Δy|
      if abs(dx) > abs(dy): 
        while x_inicial <= x_final:
          y = int(m * x_inicial + b) # 𝑦 = 𝑚𝑥 + b
          matriz[y][x_inicial] = 1
          x_inicial += 1

      # Reta |Δy| > |Δx|
      else: 
        while y_inicial <= y_final:
          x = int( (y_inicial - b ) / m ) # x = (y - b) / m
          matriz[y_inicial][x] = 1
          y_inicial += 1

  # Plota os dados no Grafico
  def plot_rasterizacao_reta(matriz, ponto_1_x, ponto_1_y, ponto_2_x, ponto_2_y, resolucao_x, resolucao_y):
      fig = pyplot.figure()
      ax = fig.add_subplot(1, 1, 1)
      ax.set_xlim([0, resolucao_x])
      ax.set_ylim([0, resolucao_y])
      ax.imshow(matriz, cmap = ListedColormap(['w', 'purple'],))
      ax.set_title('(' + str(ponto_1_x) + ' , ' + str(ponto_1_y) + '), (' + str(ponto_2_x) + ' , ' + str(ponto_2_y) + ')')
      pyplot.show()

  # Rasterização do triangulo 
  def rasterização_triangulo(self ,p1x, p1y, p2x, p2y ,p3x, p3y, resolucao_x, resolucao_y, matriz):
    self.rasteriazacao(p1x, p1y, p2x, p2y, resolucao_x, resolucao_y, matriz)
    self.rasteriazacao(p2x, p2y, p3x, p3y, resolucao_x, resolucao_y, matriz)
    self.rasteriazacao(p3x, p3y, p1x, p1y, resolucao_x, resolucao_y, matriz)
  
   # Rasterização do quadrado
  def rasterizcao_quadrado(self,p1x, p1y, p2x, p2y, p3x, p3y, p4x, p4y, resolucao_x, resolucao_y, matriz):
    self.rasteriazacao(p1x, p1y, p2x, p2y, resolucao_x, resolucao_y, matriz)
    self.rasteriazacao(p2x, p2y, p3x, p3y, resolucao_x, resolucao_y, matriz)
    self.rasteriazacao(p3x, p3y, p4x, p4y, resolucao_x, resolucao_y, matriz)
    self.rasteriazacao(p4x, p4y, p1x, p1y, resolucao_x, resolucao_y, matriz)

   # Rasterização do hexagono
  def rasterizacao_hexgono(self,p1x, p1y, p2x, p2y, p3x, p3y, p4x, p4y, p5x, p5y, p6x, p6y, resolucao_x, resolucao_y, matriz):
    self.rasteriazacao(p1x, p1y, p2x, p2y, resolucao_x, resolucao_y, matriz)
    self.rasteriazacao(p2x, p2y, p3x, p3y, resolucao_x, resolucao_y, matriz)
    self.rasteriazacao(p3x, p3y, p4x, p4y, resolucao_x, resolucao_y, matriz)
    self.rasteriazacao(p4x, p4y, p5x, p5y, resolucao_x, resolucao_y, matriz)
    self.rasteriazacao(p5x, p5y, p6x, p6y, resolucao_x, resolucao_y, matriz)
    self.rasteriazacao(p6x, p6y, p1x, p1y, resolucao_x, resolucao_y, matriz)

  # Coloca os pixels do poligono em uma matriz
  def pixels_poligono(matriz, matriz_poligono):
    for i in range(len(matriz)):
      aux = 0
      for j in range(len(matriz[i])):
        if matriz[i][j] != 0:
          aux = aux + 1 
        if aux == 1 :
          matriz_poligono[i][j] = 1

  # Plota os dados no Grafico
  def plot_rasterizacao_poligono(matriz, resolucao_x, resolucao_y,nome_poligono):
      fig = pyplot.figure()
      ax = fig.add_subplot(1, 1, 1)
      ax.set_xlim([0, resolucao_x])
      ax.set_ylim([0, resolucao_y])
      ax.imshow(matriz, cmap = ListedColormap(['w', 'purple']))
      ax.set_title(str(nome_poligono))
      pyplot.show()