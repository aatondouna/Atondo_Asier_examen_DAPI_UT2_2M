lista_num = ([(R1, G1, B1), (R2, G2, B2), (RN, GN, BN)])
luminancia = ([Y1, Y2, YN])
R = int(0, 255)
G = int(0, 255)
B = int(0, 255)
def convert_rgb2gray():
 """Funcion que convierte una lista de pixeles (RGB) en ptra lista de pixeles en escala de grises
       Parametros:
          - lista_num: una lista con un numero indeterminado de tuplas con 3 elementos que
            seran los valores de las componenetes Rojo, Verde  Azul de cada uno de los pixeles.
       Salidas:
          - luminancia: una lista con los valores de luminancia.
"""
for
def rgb2gray():
 """Funcion que calcula el componente de luminancia.
      Parametros:
         - R, G y B: Son las tres variables de esta funcion.
      Salidas:
         - Y: Representa el factor de luminancia.
"""
    factor_luminancia = (R + G + B)
    Y = factor_luminancia/3
    return Y

help(convert_rgb2gray)
help(rgb2gray)
