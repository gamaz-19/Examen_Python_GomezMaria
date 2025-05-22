import json

def abrieJSON():
    listaCompras=[]
    with open("./data/compras.json",'r') as openFile:
        listaCompras=json.load(openFile)
    return listaCompras

def guardaeJSON(dic):
    with open("./data/compras.json",'w') as outFile:
        json.dump(dic,outFile)

def cargaeLogs():
    listaCompras=[]
    with open("./data/compras/logs.json",'r') as openFile:
        listaCompras=json.load(openFile)
    return listaCompras

def logseJSON(dic):
    listaCompras = []
    #print("Diccionario Importado LOGS")
    
    listaCompras=cargarLogs()
    #print(diccionarioVentas)
    listaCompras.append(dic)
    with open("./data/compras/logs.json",'w') as outFile:
        json.dump(listaCompras,outFile)