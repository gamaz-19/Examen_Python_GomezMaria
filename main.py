##############################
########### PanCamp ##########
##############################

import json
from functions.funciones import*








booleano = True

while booleano
    print ('''
    Bienvenido a la panaderia PanCamp

    1.Gestion de ventas y compras
    2.Interacción con proveedores, empleados y clientes
    3.Generaacion de informes

    ''')

    menuprincipal == (int (input ( " Ingrese la opcion que quiere seleccionar")))

    if (menuprincipal == 1):
        print ('''
        Gestion de ventas y compras
        1.Registrar ventas
        2.Registrar compras
        
        ''')
        menu1 == (int (input ( " Ingrese la opcion que quiere seleccionar")))
        if ( menu1 == 1)
            print("Registrar ventas")
            print("Fecha venta")
            dia = (input("Dia: "))
            mes = (input("Mes: "))
            year = (input("Year: "))
            fechadt = (dia,"/",mes,"/",year) #
            print ("Informacion cliente")
            nombreCliente1 = (input("Nombre: "))
            direccion = (input("Direccion: "))
            infoclient1 = ("Nombre: ",nombre,"\nDireccion: ",direccion) #
            print ("Informacion empleado")
            nombreEmpleado1 = (input("Nombre: "))
            cargo1 = (input("Cargo: "))
            infoEmpleado1 = ("Nombre: ",nombre,"\nCargo: ",cargo1) #
            print ("Informacion producto vendido")
            producto1 = (input("Producto: ")) 
            cantidad1 = (input("Cantidad: ")) 
            precio1 = (input("Precio: ")) 
            productoVendido = ("Producto: ",producto, "Cantidad: ",cantidad1, "Precio: ",precio1) #

            diccionarioVentas = {
                "fechaVenta" : fechadt
                "inforCliente" : infoclient1
                "inforEmpleado" : infoEmpleado1
                "productVendido" : productoVendido

            }




    elif ( menuprincipal == 2):
        print ('''
        Interacción con proveedores, empleados y clientes
        Registro y gestion 
        1.Proveedores
        2.Empleados
        3.Clientes
        
        ''')
        menu2 == (int (input ( " Ingrese la opcion que quiere seleccionar")))
        if ( menu2 == 1)
            print ('''
        Proveedores
        Registro y gestion 
        1.Registrar
        2.Ver
        3.Editar
        4.Eliminar
        
        
        ''')
        elif ( menu1 == 1)
            print (" ")

    elif ( menuprincipal == 3):
        print("")


# Desarrollado por: Maria Alejandra Gomez Archila - cc. 1005234916