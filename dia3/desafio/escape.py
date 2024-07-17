# LIBRERIAS
import math as m

#######################
print("CALCULADORA VELOCIDAD DE ESCAPE")
print("--------------------------------")
print("Por favor, ingresar solo números reales")
print("Utilizar separador decimal de punto < . >")



g= float(input("Ingrese constante g [m/s²]: \n"))
r = float(input("Ingrese radio en metros: \n"))
v_escape = m.sqrt(2*g*r)

print('La velocidad de escape es : {:.2f} [m/s]'.format(v_escape))