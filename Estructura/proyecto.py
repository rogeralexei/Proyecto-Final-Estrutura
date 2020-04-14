from binarytree import tree,build
from termcolor import colored
import os,time

#Menu principal
def menu():
    """
    Funcion que muestra el menu general
    """
    os.system('clear')
    print("\nBienvenido a el programa de Prueba de Estructura de datos\nElija una opcion del Menu:"+"\n1. Pilas\n2. Colas\n3. Arboles\n4. Listas Enlazadas\n5. Salir")
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
    """
    Funcion que nos permite interactuar con el menu de pilas y de Colas
    """
    print("\nMenu:"+"\n1. Insertar\n2. Extraer\n3. Visualizar\n4. Salir")
    while True: 
        try:
            value=int(input("\nIntroduzca la opcion que desea utilizar: "))
        except:
            print("\nWhoops! El valor que introdujiste no es un numero")
        else:
            break
    return value

#Check de pilas/colas en la lista
def EnLista(lista,valor):
    """
    Funcion que nos permite evaluar si el elemento que buscamos se encuentra dentro de la lista de colas o pilas
    """
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
    
    """
    Clase que nos permite trabajar con pilas dentro de el programa. 
    """

    def __init__(self, name):
        self.name=name
        self.stack=[]
    
    def insertar(self,valor):
        """
        Permite Insertar valores a la pila
        :type valor: string
        :param valor: Valor del elemento a adicionar
        """
        self.stack.append(valor)
        print("El valor ha sido agregado correctamente")
    
    def extraer(self):
        """
        Permite eliminar valores en la pila
        """
        valor=self.stack.pop()
        print (f"Se ha extraido exitosamente el ultimo valor que es: {valor}")

    def visualizar(self):
        """
        Permite visualizar los valores de la Pila
        """
        print(self.stack)
    
    def __str__(self):
        return self.name

#Colas
class Cola():
    """
    Clase que nos permite trabajar con colas dentro de el programa. 
    """

    def __init__(self, name):
        self.name=name
        self.queue=[]
    
    def insertar(self,valor):
        """
        :type valor: string
        :param valor: Valor del elemento a adicionar
        """
        self.queue.append(valor)
        print("El valor ha sido agregado correctamente")
    
    def extraer(self):
        """
        Permite extraer los valores de la cola
        """
        valor=self.queue.pop(0)
        print (f"Se ha extraido exitosamente el primer valor que es: {valor}")

    def visualizar(self):
        """
        Permite visualizar los valores de la pila.
        """
        print(self.queue)

#Arboles

def arboles():
    """
    Menu de Arboles
    """
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
    """
    Creacion de un arbol
    """
    print ("En este programa te brindamos 2 opciones para crear arboles, elige la que mas se adapte a tu objetivo")
    
    try:
        crear=int(input("1. Crear un arbol de manera aleatoria\n2. Introducir los datos en forma de arreglo\n"))
    except:
        print("Valor Invalido")
    
    if crear==1:
        print("\nExcelente! Tu arbol sera generado de forma aleatoria. Solo necesitamos aclarar que tipo de arbol quieres")
        while True:
            try:
                altura=int(input("\nAñade la altura de tu arbol: "))
            except:
                print("El valor introducido no es valido!")
            else:
                break
        
        perfecto=input("\n¿Deseas crear un arbol perfecto? (si/no): ")
        if perfecto.lower()!="no":
            perfecto=True
        else:
            perfecto=False
        
        arbol=tree(height=altura, is_perfect=perfecto)
        return arbol
    
    elif crear==2:
        print("\nExcelente! Tu arbol sera generado en base a un arreglo. Solo necesitamos recibir los valores")
        valores=[]
        counter=0
        print("\nIntroduce los valores en orden. El valor inicial sera considerado la raiz. Los valores se ordenaran de izquiera a derecha." +
        "Deja el valor en blanco para saltar ese espacio. Escribe -1 para dejar de añadir valores")
        valor=" "
        while valor!="-1":
            valor=input(f"Introduzca el valor {counter}: ")
            if valor=="":
                valor=None
                valores.append(valor)
                counter+=1
            else:
                valores.append(int(valor))
                counter+=1
        valores.pop()
        root=build(valores)
        return root

def recorrido(arbol,numero):
    """
    Recorrido de un arbol
    """
    while True:
        if numero==2:
            print("Con gusto! Estos son los valores de tu recorrido Preorden")
            print(arbol)
            return arbol.preorder
        elif numero==3:
            print("Con gusto! Estos son los valores de tu recorrido PostOrden")
            print(arbol)
            return arbol.postorder
        elif numero==4:
            print("Con gusto! Estos son los valores de tu recorrido Inorder")
            print(arbol)
            return arbol.inorder
        elif numero==5:
            return "Hemos terminado con la seccion de arboles"

#Listas Enlazadas

class Nodo():
    """
    Clase utilizada para construir un Nodo
    """

    def __init__(self,valor):
        self.valor=valor
        self.next=None

    def __str__(self):
        return self.valor

class lista_enlazada():
    """
    Clase utilizada para crear una lista enlazada
    """

    def __init__(self,name):
        self.first=None
        self.size=0
        self.name=name

    def add(self,valor):
        """
        Permite adicionar un Nodo
        """

        MiNodo=Nodo(valor)
        if self.size==0: 
            self.first=MiNodo
        else:
            current=self.first
            while current.next!=None:
                current=current.next 
            current.next=MiNodo

        self.size+=1

        return MiNodo

    def remove(self,valor):
        """
        Permite remover un nodo
        """

        if self.size==0:
            return False
        else:
            current=self.first
            try:
                while current.next.valor!=valor:
                    current=current.next
                deleted_node=current.next
                current.next=deleted_node.next
            except AttributeError:
                return False
        self.size-=1
        return deleted_node

    def __len__(self):
        return self.size

    def __str__(self):
        string="["
        current=self.first
        for i in range(len(self)):
            string+=str(current)
            if i!=len(self)-1:
                string+=str("->")
            current=current.next
        string+="->NULL]"

        return string



if __name__=="__main__":
    """
    Programa Principal
    """

    pilas=[]
    colas=[]
    my_list=""
    trabajo=''
    arbol="" 

    while True:
        opc=menu()
        if opc==1:
            while True:
                os.system('clear')
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
                        if trabajo=="El elemento no esta en lista":
                            print(trabajo)
                            time.sleep(2.5)
                            continue
                        else:
                            print(f"\nExcelente! Ahora trabajas con la pila {trabajo}")

                else:
                    print("\nActualmente en nuestro sistema no hay ninguna pila")
                    nombre=input("\nIntroduzca un nombre para crear una pila: ")
                    pila=Pila(nombre)
                    pilas.append(pila)
                    print("\nPila Creada Satisfactoriamente!")
                    trabajo=pila
                    print(f"\nAhora trabajaras con la pila: {trabajo.name} ")

                while True:     
                    accion=menuPilas()
                                
                    if accion==1:
                        continuar=""
                        while True:
                            valor=input(f"\nIntroduzca el valor alfanumerico que desea añadir a la pila {trabajo.name}: ")
                            trabajo.insertar(valor)
                            continuar=input("\nDesea Insertar otro valor? [si/no]: ")
                            if continuar.lower()=="si":
                                continue
                            else:
                                break

                    elif accion==2:
                        while True:
                            try:
                                trabajo.extraer()
                            except:
                                print("\nLa Pila esta vacia")
                                break
                            continuar=input("\nDesea Extraer otro valor? [si/no]: ")
                            if continuar.lower()=="si":
                                continue
                            else:
                                break

                    elif accion==3:
                        print("\nTu Pila esta compuesta de los siguientes elementos: ")
                        trabajo.visualizar()
                                
                    elif accion==4:
                        print(f"\nHa concluido el uso de la pila {trabajo.name}")
                        break

                    else:
                        print("\nOpcion no valida")

        elif opc==2:
            while True:
                os.system('clear')
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
                        if trabajo=="El elemento no esta en lista":
                                print(trabajo)
                                time.sleep(2.5)
                                continue
                        else:
                            print(f"\nExcelente! Ahora trabajas con la cola {trabajo}")

                else:
                    print("\nActualmente en nuestro sistema no hay ninguna cola")
                    nombre=input("\nIntroduzca un nombre para crear una cola: ")
                    cola=Cola(nombre)
                    colas.append(cola)
                    print("\nCola Creada Satisfactoriamente!")
                    trabajo=cola
                    print(f"Ahora trabajaras con la cola: {trabajo.name} ")

                while True:     
                    accion=menuPilas()
                                
                    if accion==1:
                        continuar=""
                        while True:
                            valor=input(f"\nIntroduzca el valor alfanumerico que desea añadir a la cola {trabajo.name}: ")
                            trabajo.insertar(valor)
                            continuar=input("\nDesea Insertar otro valor? (si/no): ")
                            if continuar.lower()=="si":
                                continue
                            else:
                                break

                    elif accion==2:
                        while True:
                            try:
                                trabajo.extraer()
                            except:
                                print("La cola esta vacia")
                                break
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
            while True:
                print("Bienvenido al sistema de Arboles!")
                accion=arboles()
                if accion==1:
                    while True:
                        try:
                            arbol=crear_arbol()
                        except:
                            print("Hubo un problema durante la creacion del arbol")
                        else:
                            break
                    print(arbol)
                elif opc in range (2,6):
                    if accion==5:
                        print(recorrido(arbol,accion))
                        break
                    if arbol!="":
                        print(recorrido(arbol,accion))
                    else:
                        print("\nNo se ha creado ningun arbol. Creemos uno")
                        arbol=crear_arbol()
                        print(recorrido(arbol,accion))
        
        elif opc==4:
            while True:
                os.system("clear")
                opc=int(input("Bienvenido al sistema de Listas Enlazadas. \nMenu: \n1.Crear una lista.\n2.Añadir Nodos\n3.Remover Nodos\n4.Recorrer la lista\n5.Salir\n\nElija la opcion de su eleccion: "))
                if opc==1:
                    name=input("\nIntroduzca el nombre de su lista: ")
                    try:
                        my_list=lista_enlazada(name)
                    except:
                        print("\nHa ocurrido un error al momento de crear la lista.")
                    else:
                        print(f"\nLa Lista {my_list.name} ha sido creada con exito!")
                        time.sleep(5)
                
                elif opc==2:
                    add=True
                    while add:
                        valor=input("\nIngrese el valor que desea añadir: ")
                        try:
                            my_list.add(valor)
                        except:
                            print("Ups! Parece ser que no hay ninguna lista creada. Intenta creando una.")
                            time.sleep(5)
                            break
                        cont=input("Desea Adicionar otro valor? [si/no]: ")
                        if cont.lower()!="si":
                            add=False
                        else:
                            continue

                elif opc==3:
                    remove=True
                    while remove:
                        valor=input("\nIngrese el valor que desea eliminar o escriba quit para salir: ")
                        if valor=="quit":
                            remove=False
                            break
                        else:
                            try:
                                removido=my_list.remove(valor)
                            except:
                                print("Ups! Parece ser que no hay ninguna lista creada. Intenta creando una.")
                                time.sleep(5)
                                break
                            if removido==False:
                                print(f'El nodo con nombre {valor}, no se encuentra dentro de la lista enlazada')
                                continue
                            cont=input("Desea eliminar otro valor? [si/no]: ")
                            if cont.lower()!="si":
                                remove=False
                            else:
                                continue
                
                elif opc==4:
                    if my_list!="":
                        if len(my_list)>=1:
                            print(f"Los elementos en la lista enlazada son: {my_list}")
                            time.sleep(10)
                        else:
                            print("La lista enlazada esta vacia.")
                            time.sleep(5)
                    else:
                        print("No has creado ninguna lista")
                        time.sleep(5)

                elif opc==5:
                    break

                else:
                    print("Opcion Invalida")

        elif opc==5:
            os.system('clear')
            print(colored("🚀 Gracias por utilizar nuestro Programa 🚀","green"))
            break

        else:
            os.system('clear')
            print("Opcion Invalida")







    
