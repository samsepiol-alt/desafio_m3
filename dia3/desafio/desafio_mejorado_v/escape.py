# LIBRERIAS
import math as m
from lib import validar as v
#######################


print("CALCULADORA VELOCIDAD DE ESCAPE")
print("--------------------------------")
print("Por favor, ingresar solo números reales")
print("Utilizar separador decimal de punto < . >")

M_1 = "Ingrese constante g [m/s²]: \n"
M_2 =  "Ingrese radio en metros: \n"

g = v(M_1,'f')
r = v(M_2,'f')

v_escape = m.sqrt(2 * g * r)

print('La velocidad de escape es : {:.2f} [m/s]'.format(v_escape))