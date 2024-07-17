from lib import validar as v


print("PROGRAMA DE CALCULO DE UTILIDAD")
print("-------------------------------")
print("Por favor, solo ingresar valores numéricos")

M_1 = "Ingrese precio suscripciones "
M_2 = "Ingrese número de usuarios "
M_3 = "Ingrese gastos totales: \n"
p_n = v(M_1 + ' normales: \n','i')
p_p = v(M_1 + ' premuim: \n','i')
u_n = v(M_2 + ' normales: \n','i')
u_p= v(M_2 + ' premuim: \n','i')
gt = v(M_3,'i')



utilidad = (p_n * u_n) + (p_p * u_p) - gt

print(f'Utilidad del negocio: ${utilidad:0,.0f}')

