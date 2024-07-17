from lib import validar as v

print("PROGRAMA DE CALCULO DE UTILIDAD")
print("-------------------------------")
print("Por favor, solo ingresar valores numéricos enteros")

M_1 = "Ingrese precio suscripcion: \n"
M_2 =  "Ingrese numero de usuarios: \n"
M_3 = "Ingrese gastos totales: \n"


p = v(M_1,'i')
u = v(M_2,'i')
gt = v(M_3,'i')



utilidad = p * u - gt

print(f'Utilidad del negocio: ${utilidad:0,.0f}')

