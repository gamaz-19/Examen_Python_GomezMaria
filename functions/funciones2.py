import json

def abrirJSON2():
    listaCompras=[]
    with open("./data/compras.json",'r') as openFile:
        listaCompras=json.load(openFile)
    return listaCompras

def guardarJSON2(dic):
    with open("./data/compras.json",'w') as outFile:
        json.dump(dic,outFile)

def cargarLogs2():
    listaCompras=[]
    with open("./data/compras.json",'r') as openFile:
        listaCompras=json.load(openFile)
    return listaCompras

def logsJSON2(dic):
    listaCompras = []
    #print("Diccionario Importado LOGS")
    
    listaCompras=cargarLogs()
    #print(diccionarioCompras)
    listaCompras.append(dic)
    with open("./data/compras.json",'w') as outFile:
        json.dump(listaCompras,outFile)