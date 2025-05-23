##############################
########### PanCamp ##########
##############################

import json
from functions.funciones import*
from functions.funciones2 import*

listaVentas = abrirJSON()

listaCompras = abrirJSON2()

from datetime import datetime



booleano = True

while booleano:
    print ('''
    Bienvenido a la panaderia PanCamp

    1.Gestion de ventas y compras
    2.Interacción con proveedores, empleados y clientes
    3.Generaacion de informes

    ''')

    menuprincipal = (int (input (" Ingrese la opcion que quiere seleccionar")))

    if (menuprincipal == 1):
        print ('''
        Gestion de ventas y compras
        1.Registrar ventas
        2.Registrar compras
        
        ''')
        menu1 = (int (input (" Ingrese la opcion que quiere seleccionar")))
        if ( menu1 == 1):
            print("Registrar ventas")
            print("Fecha venta")
            dia = (int(input("Dia: ")))
            mes = (int(input("Mes: ")))
            year = (int(input("Year: ")))
            fechadt = (f"{dia:02d}/{mes:02d}/{year}")
            print ("Informacion cliente")
            nombreCliente1 = (input("Nombre: "))
            direccion = (input("Direccion: "))
            infoclient1 = ("Nombre: ",nombreCliente1,"\nDireccion: ",direccion) #
            print ("Informacion empleado")
            nombreEmpleado1 = (input("Nombre: "))
            cargo1 = (input("Cargo: "))
            infoEmpleado1 = ("Nombre: ",nombreEmpleado1,"\nCargo: ",cargo1) #
            print ("Informacion producto vendido")
            producto1 = (input("Producto: ")) 
            cantidad1 = (input("Cantidad: ")) 
            precio1 = (input("Precio: ")) 
            productoVendido = ("Producto: ",producto1, "Cantidad: ",cantidad1, "Precio: ",precio1) #

            diccionarioVentas = {
                "fechaVenta" : fechadt,
                "inforCliente" : infoclient1,
                "infempleado" : infoEmpleado1,
                "productVendido" : productoVendido

            }

            listaVentas.append(diccionarioVentas)
            guardarJSON(listaVentas)

        elif (menu1 == 2):
            print("Registrar compras")
            print("Fecha compra")
            dia = (int(input("Dia: ")))
            mes = (int(input("Mes: ")))
            year = (int(input("Year: ")))
            fechadt = (f"{dia:02d}/{mes:02d}/{year}")
            print ("Informacion proveedor")
            nombreProveedor1 = (input("Nombre: "))
            contacto = (input("Contacto: "))
            inforProveedor = ("Nombre: ",nombreProveedor1,"\nDireccion: ",contacto) #
            print ("Informacion producto comprado")
            producto1 = (input("Producto: ")) 
            cantidad1 = (input("Cantidad: ")) 
            precio1 = (input("Precio: ")) 
            productoVendido = ("Producto: ",producto1, "Cantidad: ",cantidad1, "Precio: ",precio1) #

            diccionarioCompras = {
                "fechaVenta" : fechadt,
                "inforProveedor" : inforProveedor,

                "productVendido" : productoVendido

            }

            listaCompras.append(diccionarioCompras)
            guardarJSON2(listaCompras)




    elif ( menuprincipal == 2):
        print ('''
        Interacción con proveedores, empleados y clientes
        Registro y gestion 
        1.Proveedores
        2.Empleados
        3.Clientes
        
        ''')
        menu2 = (int (input ( " Ingrese la opcion que quiere seleccionar")))
        if ( menu2 == 1):
            print ('''
        Proveedores
        Registro y gestion 
        1.Registrar
        2.Ver
        3.Editar
        4.Eliminar
        
        Ingrese opcion para proveedores:
        
        ''')
            proveedores= (int(input("opcion")))
            if (proveedores == 1):
                print("nuevo proveedor")
                nombreP = (input("Nombre proveedor: "))
                contactoP = (input("Contacto proveedor: "))
                direccionP = (input("Direccion proveedor: "))

        elif ( menu2 == 2):
            print (" ")

    elif ( menuprincipal == 3):
        print("")


# Desarrollado por: Maria Alejandra Gomez Archila - cc. 1005234916