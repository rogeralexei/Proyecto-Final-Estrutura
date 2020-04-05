'''
Proyecto final para la clase de Estructura de Datos I
'''

from binarytree import Node,tree,build

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

#Check de pilas/colas en la lista
def EnLista(lista,valor):
    temp=0
    for e in lista:
        if e.name==valor:
            temp=e
        else:
            continue
    if temp==0:
        return "El elemento no esta en lista"
    else:
        return temp       

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
    
    def __str__(self):
        return self.name

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

def arboles():
    print("Menu:"+"\n1. Crear Arbol\n2. Recorrido Preorden\n3. Recorrido PostOrden\n4. Recorrido Enorden\n5. Salir")
    while True: 
        try:
            value=int(input("\nIntroduzca la opcion que desea utilizar: "))
        except:
            print("Whoops! El valor que introdujiste no es un numero")
        else:
            break
    return value

def crear_arbol():
    print ("En este programa te brindamos 3 opciones para crear arboles, elige la que mas se adapte a tu objetivo")
    
    try:
        crear=int(input("1. Crear un arbol de manera aleatoria\n2. Introducir los datos en forma de arreglo\n3. Introducir los datos en orden"))
    except:
        print("Valor Invalido")
    
    if crear==1:
        print("Excelente! Tu arbol sera generado de forma aleatoria. Solo necesitamos aclarar que tipo de arbol quieres")
        while True:
            try:
                altura=int(input("Añade la altura de tu arbol: "))
            except:
                print("El valor introducido no es valido!")
            else:
                break
        
        perfecto=input("¿Deseas crear un arbol perfecto? (si/no): ")
        if perfecto.lower()!="no":
            perfecto=True
        else:
            perfecto=False
        
        arbol=tree(height=altura, is_perfect=perfecto)
        return arbol
    
    elif crear==2:
        print("Excelente! Tu arbol sera generado en base a un arreglo. Solo necesitamos recibir los valores")
        valores=[]
        valor=0
        print("Introduce los valores en orden. El valor inicial sera considerado la raiz. Los valores se ordenaran de izquiera a derecha." +
        "Deja el valor en blanco para saltar ese espacio. Escribe -1 para dejar de añadir valores")
        # while valor!=-1:

        #     if valor=" ":
        #         valor=None
        #     else:




#Listas Enlazadas



if __name__=="__main__":

    pilas=[]
    colas=[]
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
                    trabajo=EnLista(pilas,trabajo)
 
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

                else:
                    print("\nOpcion no valida")

        elif opc==2:
            print("Bienvenido a la seccion de colas")  
            if len(colas)>=1:
                print("Las colas creadas son las siguientes: ")
                for cola in colas:
                    print(cola.name)
                trabajo=input("\nSelecciona el nombre de la cola con la que deseas trabajar, tambien puedes escribir q para salir o n para crear una nueva: ")
                if trabajo.lower()=="n":
                    nombre=input("\nIntroduzca un nombre para crear una cola: ")
                    cola=Cola(nombre)
                    colas.append(cola)
                    print("Cola Creada Satisfactoriamente!")
                    trabajo=cola
                    print(f"Ahora trabajaras con la cola: {trabajo.name} ")
                elif trabajo.lower()=="q":
                    break
                else: 
                    trabajo=EnLista(colas,trabajo)
 
            else:
                print("\nActualmente en nuestro sistema no hay ninguna cola")
                nombre=input("\nIntroduzca un nombre para crear una cola: ")
                cola=Cola(nombre)
                colas.append(cola)
                print("Cola Creada Satisfactoriamente!")
                trabajo=cola
                print(f"Ahora trabajaras con la cola: {trabajo.name} ")

            while True:     
                accion=menuPilas()
                            
                if accion==1:
                    continuar=""
                    while True:
                        valor=input(f"Introduzca el valor alfanumerico que desea añadir a la cola {trabajo.name}: ")
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
                    print("Tu Cola esta compuesta de los siguientes elementos: ")
                    trabajo.visualizar()
                            
                elif accion==4:
                    print(f"Ha concluido el uso de la cola {trabajo.name}")
                    break

                else:
                    print("\nOpcion no valida")
        
        elif opc==3:
            print("Bienvenido al sistema de Arboles!")
            accion=arboles()
            if accion==1:
                arbol=crear_arbol()
                print(arbol)
            
                
            

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







    
