print("PROGRAMA DE CALCULO DE UTILIDAD")
print("-------------------------------")
print("Por favor, solo ingresar valores numéricos enteros")


razon = 0

p = int(input("Ingrese precio suscripcion: \n"))
u = int(input("Ingrese numero de usuarios: \n"))
gt = int(input("Ingrese gastos totales: \n"))
u_ant = int(input("Ingrese utilidad del año anterior: \n"))
utilidad = p * u - gt
if(u_ant == 0):
    print("No se puede calcular la razon entre utilidades.")
else:
    razon = utilidad/u_ant





print(f'Razon entre utilidades: {razon:0,.2f}')

