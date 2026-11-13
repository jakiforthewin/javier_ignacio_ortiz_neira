
chef_aprendis   =   0
chef_maestro    =   0
valido = True
todo_valido = False




try:
    cant_registrar    =  int(input( "cuantos chefs desea registrar? = "))
    if cant_registrar <=0:
        valido = False
        while valido ==False:
            cant_registrar = input("¡Ingrediente inválido! Ingresa un entero positivo para continuar el registro")
            if cant_registrar >0:
                valido = True


except:
    valido = False
    while valido == False:
        cant_registrar = input ("¡Ingrediente inválido! Ingresa un entero positivo para continuar el registro")
        if cant_registrar >0:
            break
        else: print("¡Ingrediente inválido! Ingresa un entero positivo para continuar el registro")


while   cant_registrar !=0:
    exp_culinaria_chef = 0


    try:
        
        while todo_valido == False:
            nombre_chef = input("ingrese el nombre del chef= ")
            
            if len(nombre_chef) <6:
                valido  =    False
                while valido == False:
                    print("el nombre debe de tener al menos 6 caracteres")
                    nombre_chef = input("ingrese el nombre del chef= ")
                    if len(nombre_chef) >=6:
                        valido = True

                for letra in nombre_chef:

                    if nombre_chef == " " :
                        valido = False
                        while valido ==False:
                            nombre_chef = input("tiene espacios, por favor ingrese un nombre sin ellos = ")
                            if nombre_chef != " ":
                                valido = True


                            


                    else:
                        print("no tiene espacios")

            
            try:   
                exp_culinaria_chef = int(input("ingrese la experiencia culinaria del chef = "))
                if exp_culinaria_chef <0:
                    valido = False
                    while valido ==False:
                        exp_culinaria_chef = int(input("¡Error gastronómico! Ingresa un número entero positivo para la experiencia culinaria."))
                        if exp_culinaria_chef >0:
                            valido = True
            except:
                valido = False
                while valido ==False:
                    exp_culinaria_chef = int(input("¡Error gastronómico! Ingresa un número entero positivo para la experiencia culinaria."))
                    if exp_culinaria_chef >0:
                        valido = True


            if nombre_chef != " " and len(nombre_chef) >6 and exp_culinaria_chef >0:
                todo_valido = True
                if exp_culinaria_chef >8:
                    chef_maestro = chef_maestro +1
                elif exp_culinaria_chef <=8 and exp_culinaria_chef >0:
                    chef_aprendis = chef_aprendis+1

            else: print("algo salio mal, intentelo nuevamente")

        cant_registrar = cant_registrar -1



        
            




    except: print("algo salio mal")








print(f'La escuela cuenta con {chef_maestro}] Chefs Maestros y {chef_aprendis} Chefs Aprendices! ¡A cocinar')


















