
def main():
    edad = int(input("Ingresa tu edad: "))
    #Aquí empieza tu programa...
    if (edad >= 18):
        identificacionOficial = input("¿Tienes identificación oficial? (s/n): ")
        if (identificacionOficial == 'S' or identificacionOficial == 's'):
            print("Trámite de licencia concedido")
        elif (identificacionOficial == 'N' or identificacionOficial == 'n'):
            print("No cumples requisitos")
        else:
            print("Respuesta incorrecta")
    elif (edad < 18 and edad > 0):
        print("No cumples requisitos")
    else:
        print("Respuesta incorrecta")

if __name__ == '__main__':
    main()
