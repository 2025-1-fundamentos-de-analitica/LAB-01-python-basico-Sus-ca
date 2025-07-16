"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """

    letter_sums = {}

    with open("files/input/data.csv", "r") as file:
        for line in file:
            columns = line.strip().split("\t")
            col1_letter = columns[0]
            col5_pairs = columns[4].split(",")
            
            if col1_letter not in letter_sums:
                letter_sums[col1_letter] = 0
            
            for pair in col5_pairs:
                value = int(pair.split(":")[1])
                letter_sums[col1_letter] += value
    
    return letter_sums

if __name__ == "__main__":
    print(pregunta_12())
