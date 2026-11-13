

cam_disponibles = 90
salir =False
historial_reservas = 0


print( "Bienvenida ¡Bienvenido al sistema de gestión de camarotes del Crucero Atlántico!")


print("=== MENÚ PRINCIPAL ===")
print("1.- Camarotes disponibles.")
print("2.- Reservar camarote.")
print("3.- Cancelar camarote.")
print("4.- Historial de reservas.")
print("5.- Salir.")



while salir == False:
    opcion  =   input("ingrese su opcion = ")

    match opcion:
        case "1":
            print(f'camarotes disponibles = {cam_disponibles}')

        case "2":
            try:
                
                reservar_cam = int(input("cuantos camarotes desea reservar? = "))
                if reservar_cam > cam_disponibles or reservar_cam <0:
                    valido = False
                    historial_reservas = historial_reservas + reservar_cam
                    while valido == False:
                        reservar_cam = int(input ("error, ingrese un numero no mayor a los camarotes disponibles"))
                        if reservar_cam <= cam_disponibles and reservar_cam >0:
                            valido  =   True
                            historial_reservas = historial_reservas + reservar_cam


            except:
                valido = False
                while valido ==False:
                    reservar_cam = int(input ("error, ingrese un numero no mayor a los camarotes disponibles"))
                    if reservar_cam <= cam_disponibles and reservar_cam >0:
                        valido  =   True
                        historial_reservas = historial_reservas + reservar_cam


        case "3":


            try:
                liberar_cam = int(input("ingrese la cantidad de camarotes a liberar = "))

                if liberar_cam >90 or liberar_cam <0 or liberar_cam + cam_disponibles > 90:
                    valido = False
                    
                    while valido ==False:
                        if  liberar_cam <91 and liberar_cam >0 and liberar_cam + cam_disponibles > 91:
                            valido  =   True
                            

                cam_disponibles = cam_disponibles+ liberar_cam
                historial_reservas= historial_reservas -liberar_cam





            except:
                valido = False
                while valido ==False:
                    liberar_cam = input ("error, ingrese un numero no mayor a los camarotes disponibles")
                    if  liberar_cam <91 and liberar_cam >0 and liberar_cam + cam_disponibles > 91:
                        valido  =   True
                        cam_disponibles = cam_disponibles+ liberar_cam
                        historial_reservas= historial_reservas -liberar_cam






        case "4":
            print("historial de reservas = ")
            print(historial_reservas)




        case "5":
            print("Gracias por utilizar nuestro software, hasta la próxima.")
            salir =True


        case _:

            opcion = input("opcion no valida, intentelo nuevamente = ")










