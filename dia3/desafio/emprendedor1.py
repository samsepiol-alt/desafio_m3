print("PROGRAMA DE CALCULO DE UTILIDAD")
print("-------------------------------")
print("Por favor, solo ingresar valores numéricos enteros")

p = int(input("Ingrese precio suscripcion: \n"))
u = int(input("Ingrese numero de usuarios: \n"))
gt = int(input("Ingrese gastos totales: \n"))



utilidad = p * u - gt

print(f'Utilidad del negocio: ${utilidad:0,.0f}')

