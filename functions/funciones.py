import json

def abrirJSON():
    listaVentas=[]
    with open("./data/ventas.json",'r') as openFile:
        listaVentas=json.load(openFile)
    return listaVentas

def guardarJSON(dic):
    with open("./data/ventas.json",'w') as outFile:
        json.dump(dic,outFile)

def cargarLogs():
    listaVentas=[]
    with open("./data/ventas.json",'r') as openFile:
        listaVentas=json.load(openFile)
    return listaVentas

def logsJSON(dic):
    listaVentas = []
    #print("Diccionario Importado LOGS")
    
    listaVentas=cargarLogs()
    #print(diccionarioVentas)
    listaVentas.append(dic)
    with open("./data/ventas.json",'w') as outFile:
        json.dump(listaVentas,outFile)