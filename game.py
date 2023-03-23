from random import choice, randrange
from datetime import datetime
# Operadores posibles
operators = ["+", "-", "*", "/"]
# Cantidad de cuentas a resolver
times = 5
# Contador inicial de tiempo.
# Esto toma la fecha y hora actual.
init_time = datetime.now()
print(f"¡Veremos cuanto tardas en responder estas {times} operaciones!")


correctas =0
incorrectas= 0

for i in range(0, times):
  # Se eligen números y operador al azar
  number_1 = randrange(10)
  number_2 = randrange(10)
  operator = choice(operators)

  match operator: 
    case "+" : 
        resultado = number_1 + number_2
    case "-": 
        resultado = number_1 - number_2
    case "*": 
        resultado = number_1 * number_2
    case "/": 
         # no puedo dividir por cero asi que agrego una sentencia que fuerce otro denominador 
         while number_2 == 0 : 
            number_2= randrange(10)

         resultado = number_1 / number_2

         # Me quedo solo con la parte entera y un decimal del numero 
         resultado = (int (resultado * 10) / 10)
          
      
       
         

  print(f"{i+1}- ¿Cuánto es {number_1} {operator} {number_2}?")

  # Le pedimos al usuario el resultado
  result = float(input("resultado: "))

  # Me quedo solo con la parte entera y un decimal del numero 
  result = (int (result*10)/ 10)


  
  if result == resultado :
    print("Correcto")
    correctas += 1
  else: 
    print ("Incorrecto")
    incorrectas += 1

# Al terminar toda la cantidad de cuentas por resolver.
# Se vuelve a tomar la fecha y la hora.
end_time = datetime.now()
# Restando las fechas obtenemos el tiempo transcurrido.
total_time = end_time - init_time

# Mostramos ese tiempo en segundos.
separador = "_" * 35
print(separador)
print(f"\n Tardaste {total_time.seconds} segundos.")


print ("Respuestas correctas:" , correctas, "\nRespuestas incorrectas: ", incorrectas )
print(separador)