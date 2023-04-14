#10. Dada una lista de nombres de estudiantes y dos listas con sus notas en un curso, escriba un
#programa que manipule dichas estructuras de datos para poder resolver los siguientes puntos:
#A. Generar una estructura con todas las notas relacionando el nombre del estudiante con las
#notas. Utilizar esta estructura para la resolución de los siguientes items.
#B. Calcular el promedio de notas de cada estudiante.
#C. Calcular el promedio general del curso.
#D. Identificar al estudiante con la nota promedio más alta.
#E. Identificar al estudiante con la nota más baja


nombres = '''  'Agustin', 'Alan', 'Andrés', 'Ariadna', 'Bautista', 'CAROLINA', 'CESAR',
'David','Diego', 'Dolores', 'DYLAN', 'ELIANA', 'Emanuel', 'Fabián', 'Facundo',
'Francsica', 'FEDERICO', 'Fernanda', 'GONZALO', 'Gregorio', 'Ignacio', 'Jonathan',
'Joaquina', 'Jorge','JOSE', 'Javier', 'Joaquín' , 'Julian', 'Julieta', 'Luciana',
'LAUTARO', 'Leonel', 'Luisa', 'Luis', 'Marcos', 'María', 'MATEO', 'Matias',
'Nicolás', 'Nancy', 'Noelia', 'Pablo', 'Priscila', 'Sabrina', 'Tomás', 'Ulises',
'Yanina'  '''

notas_1 = [81, 60, 72, 24, 15, 91, 12, 70, 29, 42, 16, 3, 35, 67, 10, 57, 11, 69,
12, 77, 13, 86, 48, 65, 51, 41, 87, 43, 10, 87, 91, 15, 44,
85, 73, 37, 42, 95, 18, 7, 74, 60, 9, 65, 93, 63, 74]

notas_2 = [30, 95, 28, 84, 84, 43, 66, 51, 4, 11, 58, 10, 13, 34, 96, 71, 86, 37,
64, 13, 8, 87, 14, 14, 49, 27, 55, 69, 77, 59, 57, 40, 96, 24, 30, 73,
95, 19, 47, 15, 31, 39, 15, 74, 33, 57, 10]



#hago una lista con los nombres de los estudiantes
nombres = nombres.replace("'", "").replace(" '", "").replace(" ","").replace("\n", "").split(",")
#creo una lista que relacione el nombre de los estudiantes con las notas

notas_por_estudiante = dict(zip(nombres, zip(notas_1, notas_2)))


def promedio_general (): 
    """Esta funcion calcula y retorna el promedio general de notas del curso 
    """
    #genero una lista con todas las notas del curso 
    notas = [nota for alumno in notas_por_estudiante.values() for nota in alumno]
    
    #sumo todas las notas de la lista y las divido por la cantidad de elementos 
    return (sum(notas) / len(notas))


def calcularPromedio ():
    """Esta funcion calcula el promedio de cada estudiante
    """
    for nombre in notas_por_estudiante: 
        prom = lambda nota1, nota2: ((nota1+ nota2) / 2)
       
        print(f" promedio de {nombre} : {prom(notas_por_estudiante[nombre][0], notas_por_estudiante[nombre][1])}")
        
def mejor_promedio():
    """ esta funcion retorna el alumno con mejor promedio"""
    #1. creo una lista de tuplas que tiene el nombre del estudiante y su promedio
    #2. con la funcion sorted ordeno la lista de mayor a menor usando como criterio de ordenamiento
    #   el promedio de cada estudiante 
    #3. devuelvo el elemento 0 de la primera tupla que contiene el nombre del estudiante con mayor promedio 
    
    mejores_notas = sorted(notas_por_estudiante.items(), key=lambda x: ((sum(x[1]))/2), reverse=True)
   
    return mejores_notas[0][0]

def nota_mas_baja ():
    """esta funcion retorna el alumno con la nota mas baja"""    
    peores_notas= sorted(notas_por_estudiante.items(), key= lambda x: min(x[1]),   reverse=False)
    return peores_notas[0][0]
    

    

calcularPromedio()
print (f"el promedio general del curso es: {promedio_general()}")
print(f"el estudiante con mejor promedio es: {mejor_promedio()}")
print(f"el alumno con nota mas baja es: {nota_mas_baja()}")