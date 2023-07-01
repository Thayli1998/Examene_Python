#_________________ Función 1
import numpy as np
def build_population(N, p):
    """
    Construye una población de individuos con dos alelos cada uno.

    Args:
        N (int): El número de individuos en la población.
        p (float): La probabilidad de que un alelo sea "A".

    Returns:
        list: Una lista de tuplas que representan los alelos de cada individuo.
    """
    # Crea una lista vacía para almacenar la población
    population = []

    # Repite N veces para crear N individuos
    for i in range(N):
        # Establece el primer alelo en "A"
        allele1 = "A"

        # Genera un número aleatorio y verifica si es mayor que p
        if np.random.rand() > p:
            # Si es mayor que p, cambia el primer alelo a "a"
            allele1 = "a"

        # Establece el segundo alelo en "A"
        allele2 = "A"

        # Genera otro número aleatorio y verifica si es mayor que p
        if np.random.rand() > p:
            # Si es mayor que p, cambia el segundo alelo a "a"
            allele2 = "a"

        # Agrega la tupla de alelos a la lista de población
        population.append((allele1, allele2))

    # Devuelve la lista de población
    return population



#_________________ Función 2
def compute_frequencies(population):
    """
    Calcula la frecuencia de cada genotipo en una población.

    Args:
        population (list): Una lista de tuplas que representan los genotipos de una población.

    Returns:
        dict: Un diccionario con la frecuencia de cada genotipo en la población.
    """
    # Cuenta el número de individuos con genotipo "AA" en la población
    AA = population.count(("A", "A"))
    # Cuenta el número de individuos con genotipo "Aa" en la población
    Aa = population.count(("A", "a"))
    # Cuenta el número de individuos con genotipo "aA" en la población
    aA = population.count(("a", "A"))
    # Cuenta el número de individuos con genotipo "aa" en la población
    aa = population.count(("a", "a"))
    # Devuelve un diccionario con la frecuencia de cada genotipo
    return({"AA": AA, "aa": aa, "Aa": Aa, "aA": aA})


#_________________ Función 3
def reproduce_population(population):
    """
    Esta función toma una población y genera una nueva generación a través de la reproducción aleatoria.
    
    :param population: Una lista de tuplas que representan a los individuos de la población.
    :return: Una lista de tuplas que representan a los individuos de la nueva generación.
    """
    new_generation = [] # Lista vacía para almacenar la nueva generación
    N = len(population) # Número de individuos en la población
    for i in range(N): # Para cada individuo en la población
        dad = np.random.randint(N) # Se selecciona aleatoriamente un padre
        mom = np.random.randint(N) # Se selecciona aleatoriamente una madre
        chr_mom = np.random.randint(2) # Se selecciona aleatoriamente uno de los dos cromosomas de la madre
        offspring = (population[mom][chr_mom], population[dad][1 - chr_mom]) # se crea un descendiente con un cromosoma de cada padre
        new_generation.append(offspring) # Se agrega el descendiente a la nueva generación
    return new_generation # Devuelve la nueva generación


#_________________ Función 4
def simulate_drift(N, p):
    """
    Simula la deriva genética en una población de tamaño N con una frecuencia inicial de alelos p.
    Devuelve el número de generaciones hasta que se alcanza la fijación y el recuento final de genotipos.
    """
    my_pop = build_population(N, p) # Construye una población inicial
    fixation = False # Establece la variable de fijación en Falso
    num_generations = 0 # Establece el contador de generaciones en 0
    while fixation == False: # Mientras no se alcance la fijación
        genotype_counts = compute_frequencies(my_pop) # Calcula las frecuencias de genotipos
        if (genotype_counts["AA"] == N or genotype_counts["aa"] == N): # Si un alelo alcanza la fijación ( es decir cuando toda la población tiene el mismo alelo)
            print("An allele reached fixation at generation", num_generations) # Imprime el número de generaciones hasta la fijación
            print("The genotype counts are") # Imprime los recuentos finales de genotipos
            print(genotype_counts)
            fixation == True # Establece la variable de fijación en Verdadero
            break # Sale del bucle while
        my_pop = reproduce_population(my_pop) # Reproduce la población para la siguiente generación
        num_generations += 1 # Incrementa el contador de generaciones
    return num_generations, genotype_counts # Devuelve el número de generaciones y los recuentos finales de genotipos
