print("***************************************")
print("'* Sistema de Control Vacasional Rappy *'")
print("*************************************** \n")

nombre_empleado = input("Por favor introduce el nombre del empleado: ")
clave_departamento = int(input("Por favor introduce la clave del departamento: "))
antiguedad_empleado = float(input("Por favor introduce los años laborados del empleado: "))

if clave_departamento == 1:

    if antiguedad_empleado == 1 and antiguedad_empleado < 2:
        print("El empleado ", nombre_empleado, "tiene derecho a 6 dias de vacasiones: ")
    elif antiguedad_empleado >= 2 and antiguedad_empleado <= 6:
        print("El empleado ", nombre_empleado, "tiene derecho a 14 dias de vacasiones: ")
    elif antiguedad_empleado >= 7:
        print("El empleado ", nombre_empleado, "tiene derecho a 20 dias de vacasiones: ")
    else:
        print("El empleado ", nombre_empleado, " aún no tiene derecho a  vacasiones: ")
        
        

elif clave_departamento == 2:
    
    if antiguedad_empleado == 1 and antiguedad_empleado < 2:
        print("El empleado ", nombre_empleado, "tiene derecho a 7 dias de vacasiones: ")
    elif antiguedad_empleado >= 2 and antiguedad_empleado <= 6:
        print("El empleado ", nombre_empleado, "tiene derecho a 15 dias de vacasiones: ")
    elif antiguedad_empleado >= 7:
        print("El empleado ", nombre_empleado, "tiene derecho a 22 dias de vacasiones: ")
    else:
        print("El empleado ", nombre_empleado, " aún no tiene derecho a  vacasiones: ")
        


elif clave_departamento == 3:

    if antiguedad_empleado == 1 and antiguedad_empleado < 2:
        print("El empleado ", nombre_empleado, "tiene derecho a 10 dias de vacasiones: ")
    elif antiguedad_empleado >= 2 and antiguedad_empleado <= 6:
        print("El empleado ", nombre_empleado, "tiene derecho a 20 dias de vacasiones: ")
    elif antiguedad_empleado >= 7:
        print("El empleado ", nombre_empleado, "tiene derecho a 30 dias de vacasiones: ")
    else:
        print("El empleado ", nombre_empleado, " aún no tiene derecho a  vacasiones: ")
        
else:
        print("La clave del departamento no existe, vuelve a intentarlo: ")
      
print("""\n|  ___|  | |                   / _ \     | |                        
| |__  __| | __ _  __ _ _ __  / /_\ \_ __| |_ ___  __ _  __ _  __ _ 
|  __|/ _` |/ _` |/ _` | '__| |  _  | '__| __/ _ \/ _` |/ _` |/ _` |
| |__| (_| | (_| | (_| | |    | | | | |  | ||  __/ (_| | (_| | (_| |
\____/\__,_|\__, |\__,_|_|    \_| |_/_|   \__\___|\__,_|\__, |\__,_|
             __/ |                                       __/ |      
            |___/                                       |___/   """)