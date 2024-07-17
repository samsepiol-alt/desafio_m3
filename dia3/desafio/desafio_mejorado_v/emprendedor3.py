from lib import validar as v
print("PROGRAMA DE CALCULO DE UTILIDAD")
print("-------------------------------")
print("Por favor, solo ingresar valores numéricos enteros")


razon = 0
M_1 = "Ingrese precio suscripcion: \n"
M_2 = "Ingrese número de usuarios: \n "
M_3 = "Ingrese gastos totales: \n"
M_4 =  "Ingrese utilidad del año anterior: \n"

p = v(M_1,'i')
u = v(M_2,'i')
gt = v(M_3,'i')
u_ant = v(M_4,'i')
utilidad = p * u - gt
if(u_ant == 0):
    print("No se puede calcular la razon entre utilidades.")
else:
    razon = utilidad/u_ant




print(f"Utilidad del negocio: ${utilidad:0,}")
print(f'Razon entre utilidades: {razon:0,.2f}')

