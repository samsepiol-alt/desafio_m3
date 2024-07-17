
print("PROGRAMA DE CALCULO DE UTILIDAD")
print("-------------------------------")
print("Por favor, solo ingresar valores numéricos")



p_n = int(input("Ingrese precio suscripcion normal: \n"))
p_p = int(input("Ingrese precio suscripcion premium: \n"))
u_n = int(input("Ingrese numero de usuarios normales: \n"))
u_p= int(input("Ingrese numero de usuarios premium: \n"))
gt = int(input("Ingrese gastos totales: \n"))



utilidad = (p_n * u_n) + (p_p * u_p) - gt

print(f'Utilidad del negocio: ${utilidad:0,.0f}')

