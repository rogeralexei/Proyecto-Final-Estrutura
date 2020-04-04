'''
Proyecto final para la clase de Estructura de Datos I
'''
from binarytree import Node

#Menu principal
def menu():
    print("Menu:"+"\n1. Pilas\n2.Colas\n3.Arboles\n4.Listas Enlazadas\n5.Salir")
    try:
        value=int(input("\nIntroduzca la opcion que desea utilizar: "))
    except:
        print("Whoops! El valor que introdujiste no es un numero")
    else:
        return value

#Pilas
class Pila():
    
    def __init__(self, name):
        self.name=name
        self.stack=[]
    
    def insertar(self,valor):
        self.stack.append(valor)
        print("El valor ha sido agregado correctamente")
    
    def extraer(self):
        valor=self.stack.pop()
        print (f"Se ha extraido exitosamente el ultimo valor que es: {valor}")

    def visualizar(self):
        print(self.stack)

#Colas
class Cola():

    def __init__(self, name):
        self.name=name
        self.queue=[]
    
    def insertar(self,valor):
        self.queue.append(valor)
        print("El valor ha sido agregado correctamente")
    
    def extraer(self):
        valor=self.queue.pop(0)
        print (f"Se ha extraido exitosamente el ultimo valor que es: {valor}")

    def visualizar(self):
        print(self.queue)


#Arboles

#Listas Enlazadas



if __name__=="__main__":
    opc=menu()
    pilas=[]
    colas=[]
    arboles=[]


    if opc==1:
        print("Bienvenido a la seccion de pilas!")

        nombre=input("Introduzca un nombre para su pila: ")
        a=Pila(nombre)
        pilas.append(a)
        a.insertar(12)
        a.insertar(24)
        a.visualizar()
        a.extraer()
        a.visualizar()
    elif opc==2:
        print("Bienvenido a la seccion de colas!")

        nombre=input("Introduzca un nombre para su cola: ")
        b=Cola(nombre)
        colas.append(a)
        b.insertar(12)
        b.insertar(24)
        b.visualizar()
        b.extraer()
        b.visualizar()
    elif opc==3:
       print("Bienvenido a la seccion de arboles binarios!") 

       root=Node(23)
       root.left=Node(16)
       root.right=Node(40)
       root.left.left=Node(15)
       root.left.right=Node(63)
       print(root)
       print(root.inorder)
    
    elif 







    
