# 1. Será la simulación de una máquina de Galton de 3000 canicas.
# 2. En total tendrá 12 niveles de obstáculos -deberás decidir si va a caer a
# un lado o al otro 12 veces.
# 3. El resultado final será un histograma que represente la cantidad de
# canicas en cada contenedor, como el siguiente -No olvides colocar
# nombre a los ejes y un título al gráfico.
# 4. Deberás emplear dos funciones, una para calcular los resultados de las
# canicas y la segunda para la graficación del histograma.

# Importamos matplotlib para poder graficar
import matplotlib.pyplot as plt

# Importamos random para que nos deje randomizar valores
import random

# Variable del numero de obstaculos que tendrán las canicas
obstaculos = 12

# La función Toma como parametro el numero de obstaculos, 0 es izq y 1 es der. 
def simular_canica(obstaculos):
    '''Función que guarda los resultados de los movimientos randomizados izquierda y derecha'''
    resultados = []
    for i in range(obstaculos):
        numero = random.randint(0,1)
        resultados.append(numero)
    contenedor = resultados.count(1)
    return contenedor

# Variable del numero de canicas 
canicas = 3000

# Array vacío que se llenaroa con el ciclo for y mostrará en que contenedores caen todas las canicas
contenedoresFinales = []

for i in range(canicas):
    canica = simular_canica(obstaculos)
    contenedoresFinales.append(canica)

# Función para graficar todo lo anterior
def graficar_histograma(contenedores):
    '''Función que toma como parametro contenedores,
     el argumento será la variable contenedoresFinales y lo grafica '''
    plt.hist(contenedores, bins=range(0, 14), align='left')
    plt.title('Maquina de Galton')
    plt.xlabel('Contenedores')
    plt.ylabel('Cantidad canicas')
    plt.show()

# Llamamos a la función de graficación pasando como argumento nuestro array de contenedoresFinales
graficar_histograma(contenedoresFinales)



    
