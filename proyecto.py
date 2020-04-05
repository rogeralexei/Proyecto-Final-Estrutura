'''
Proyecto final para la clase de Estructura de Datos I
'''

from binarytree import Node

#Menu principal
def menu():
    print("Menu:"+"\n1. Pilas\n2. Colas\n3. Arboles\n4. Listas Enlazadas\n5. Salir")
    while True:
        try:
            value=int(input("\nIntroduzca la opcion que desea utilizar: "))
        except:
            print("Whoops! El valor que introdujiste no es un numero")
        else:
            break
    return value

#Menu de Pilas
def menuPilas():
    print("Menu:"+"\n1. Insertar\n2. Extraer\n3. Visualizar\n4. Salir")
    while True: 
        try:
            value=int(input("\nIntroduzca la opcion que desea utilizar: "))
        except:
            print("Whoops! El valor que introdujiste no es un numero")
        else:
            break
    return value

#Check de pilas en la lista
def pilaEnLista(pilas):
    pass


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

    pilas=[]
    colas=[]
    arboles=[]
    listas=[]
    trabajo='' 

    opc=menu()
    
    while opc!=5: 
        if opc==1:
            print("Bienvenido a la seccion de pilas")  
            if len(pilas)>=1:
                print("Las pilas creadas son las siguientes: ")
                for pila in pilas:
                    print(pila.name)
                trabajo=input("\nSelecciona el nombre de la pila con la que deseas trabajar, escribe q para salir o n para crear una nueva: ")
                if trabajo.lower()=="n":
                    nombre=input("\nIntroduzca un nombre para crear una pila: ")
                    pila=Pila(nombre)
                    pilas.append(pila)
                    print("Pila Creada Satisfactoriamente!")
                    trabajo=pila
                    print(f"Ahora trabajaras con la pila: {trabajo.name} ")
                elif trabajo.lower()=="q":
                    break
                else: 
                    print("Under Construction")
                    # for pila in pilas:
                    #     cont=0
                    #     while cont==0:
                    #         if trabajo==pila.name:
                    #             trabajo=pila
                    #             cont=1
                    #         else:
                    #             print("La pila mencionada no existe")
                    #             for pila in pilas:
                    #                 print(pila.name)
                    #             trabajo=input("\nSelecciona el nombre de la pila con la que deseas trabajar que este en la lista: ")
                    #     print(f"Trabajaras con la pila {trabajo.name}")
            
            else:
                print("\nActualmente en nuestro sistema no hay ninguna pila")
                nombre=input("\nIntroduzca un nombre para crear una pila: ")
                pila=Pila(nombre)
                pilas.append(pila)
                print("Pila Creada Satisfactoriamente!")
                trabajo=pila
                print(f"Ahora trabajaras con la pila: {trabajo.name} ")

            while True:     
                accion=menuPilas()
                            
                if accion==1:
                    continuar=""
                    while True:
                        valor=input(f"Introduzca el valor alfanumerico que desea añadir a la pila {trabajo.name}: ")
                        trabajo.insertar(valor)
                        continuar=input("Desea Insertar otro valor? (si/no): ")
                        if continuar.lower()=="si":
                            continue
                        else:
                            break

                elif accion==2:
                    while True:
                        trabajo.extraer()
                        continuar=input("Desea Extraer otro valor? (si/no): ")
                        if continuar.lower()=="si":
                            continue
                        else:
                            break

                elif accion==3:
                    print("Tu Pila esta compuesta de los siguientes elementos: ")
                    trabajo.visualizar()
                            
                elif accion==4:
                    print(f"Ha concluido el uso de la pila {trabajo.name}")
                    break

        elif opc==2:
            print("Hello")
    #         print("Bienvenido a la seccion de colas!")

    #         nombre=input("Introduzca un nombre para su cola: ")
    #         b=Cola(nombre)
    #         colas.append(a)
    #         b.insertar(12)
    #         b.insertar(24)
    #         b.visualizar()
    #         b.extraer()
    #         b.visualizar()
        
    #     elif opc==3:
    #         print("Bienvenido a la seccion de arboles binarios!") 

    #         root=Node(23)
    #         root.left=Node(16)
    #         root.right=Node(40)
    #         root.left.left=Node(15)
    #         root.left.right=Node(63)
    #         print(root)
    #         print(root.inorder)
        
    #     elif opc==4:
    #         print("Listas Enlazadas")
        
    #     else:
    #         print("¡Ese Numero no se encuentra dentro de las opciones permitidas!")
    #         opc=menu()
    
    # print("¡Gracias por utilizar nuestro programa!")







    
