alumnos = ["Juan Pérez", "María García", "Carlos López", "Ana Martínez", "Pedro Rodríguez", "Laura Hernández", "Miguel Sánchez", "Isabel Gómez", "FranciscoDíaz", "Elena Fernández"]
import random,csv

L_menor_a_100 = []
L_Créditos_entre_100_150 = []
L_creditos_mayores_150 = []
def menu():
    print("1. Simulación de Créditos en AWS:")
    print("2. Clasificación de Créditos")
    print("3. Cálculo de Estadísticas de Créditos")
    print("4. Generación de Reporte de Créditos")
    print("5. Salir del Programa")
def sim_credito():
    global alumnos 
    global d 
    for i in alumnos:
        d[i] = 0
    for q in d :
        d[q] = random.randint(50,200) 

    return d
def clas_creditos():
    
    global d
    for nombre, valor  in d.items():
        if valor < 100:
            L_menor_a_100.append(nombre)
    
    return L_menor_a_100

def clas_creditos_100_150():
    for nombre, valor  in d.items():
        if valor >=  100 and valor <= 150 :
            L_Créditos_entre_100_150.append(nombre)
    
    return L_Créditos_entre_100_150

def clas_creditos_mayores150():
    for nombre, valor  in d.items():
        if valor > 150 :
            L_creditos_mayores_150.append(nombre)
    
    return L_creditos_mayores_150

def maximo_minimo_credito(diccionario):
    mayor = float("-inf") #infinito negativo
    menor = float("inf") #infinito positivo
    for i in diccionario.values():
        
        if i > mayor :
            mayor = i 
    for i in diccionario.values():
    
        if i < menor :
            menor = i 
    
    
    print("el credito mayor es", mayor)
    print("el crediuto menor es ", menor)

def promedio(diccionario):


    suma = 0
    contador = 0
    for i in diccionario.values():
        suma = suma + i
        contador += 1
    promedio = suma/contador
    print("el promedio de los valores es", round(promedio)) 
    print() #solo para hacer un espacio

def listar_diccionario(diccionario):
    L_contenido = []
    l_personas = []
    for persona, valor in diccionario.items() :
        l_personas.append(persona)
        l_personas.append(valor)
    L_contenido.append(l_personas)   
    return L_contenido 

        

def crear_archivo(contenido):
    arch = open("reporte_creditos.csv.","w",newline ='')
    escritor = csv.writer(arch)
    escritor.writerow(contenido)
    print("archivo creado con exito")
    arch.close()




d = {}
op = ""
while op != "5":
    menu()
    op = input("ingrese una opcion ")

    if op == "1":
        
      
        sim_credito()
        
        print("simulacion creada con exito ")
        print(d)
    
    elif op == "2":
        try:

            clas_creditos()
            clas_creditos_100_150()
            clas_creditos_mayores150()
            print("personas con creditos menores a 100",L_menor_a_100)
            print("personas con creditos entre 100 y 150", L_Créditos_entre_100_150)
            print("personas con creditos mayores a 150 ", L_creditos_mayores_150)
        except:
            print("a ocurrido un error, verifique tener la simulacion creada")

    elif op =="3":
        maximo_minimo_credito(d)
        promedio(d)

    elif op == "4":
        contenido_csv = listar_diccionario(d)
        crear_archivo(contenido_csv)
    
if op == "5":
    print("saliendo del programa.... .. . ")
        
            

        


        
        
        

