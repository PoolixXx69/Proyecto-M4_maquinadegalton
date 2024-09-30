import random #genera numeros aleatorios
import matplotlib.pyplot as plt #genera graficas(histogramas)

def maquina_galton(canicas, niveles):
    """
    se simula una máquina de Galton con canicas, bolas y niveles, niveles de obstáculos.
    Devuelve una lista de contenedores con el recuento de bolas en cada uno para poder representarlos en una grafica(histograma)
    El objetivo principal de esta funcion es simular el recorrido de las canicas atraves de los niveles de obstaculos y contar cuantas canicas caen en cada uno de los 12 contenedores
    """
    contenedores = [0] * 12  # Iniciaa 12 contenedores con ceros
    for _ in range(canicas):
        ruta_canica = ""  # se inicia la ruta de canica como cadena vacia 
        for _ in range(niveles):
            ruta_canica += str(random.randint(0, 1))  #Aqui decide aleatoriamente hacia donde ira cada canica 
        indice_contenedor = ruta_canica.count('0') % 12 + 1  # Cuenta el número de ceros en la ruta de la bola y ajusta para que caiga en los contenedores 1-12
        contenedores[indice_contenedor - 1] += 1  # aumenta  el conteo en el contenedor correspondiente

    return contenedores

def plot_histogram(contenedores):
    """
    funcion que crea el histograma con lo pedido de igual forma asignando titulos.
    y formando lo que queremos mostrar en pantalla al usuario 
    """
    plt.bar(range(1, 13), contenedores)  # Muestra solo los contenedores del 1 al 12
    plt.xlabel("CONTENEDORES") #titulo del eje x
    plt.ylabel("CANICAS") #titulo del eje y
    plt.title("LA MAQUINA DE GALTON") #titulo del histograma
    plt.show() #inicia la simulacion en pantalla 

# Simula la máquina de Galton
canicas = 3000  #numero de canicas a mostrar
niveles = 13  #numero de contenedores  a mostrar para que el 0 no se muestre y el 13 tampoco se puso el numero 13 asi acomodamos para que solo muestre el 1,2,3,4,5,6,7,8,9,10,11,12

contenedores = maquina_galton(canicas, niveles)

# Visualiza la distribución de las canicas
plot_histogram(contenedores)