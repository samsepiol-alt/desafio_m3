def validar(message, type):

    match type:
        case 'i':
           while True:
                try:
                    data = int(input(message))
                    break
                except ValueError:
                    print("Por favor ingrese un numero válido.")
           
        case 'f':
           while True:
                try:
                    data = float(input(message))
                    break
                except ValueError:
                    print("Por favor ingrese un numero válido.")

        case _:
           print("Dato no valido.")
    return data
        