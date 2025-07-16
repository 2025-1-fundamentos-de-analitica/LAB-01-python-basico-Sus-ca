"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """

    with open("files/input/data.csv", "r") as file:
        data = {}
        for line in file:
            letter = line.split("\t")[0]
            value = int(line.split("\t")[1])
            if letter in data:
                data[letter].append(value)
            else:
                data[letter] = [value]

    return [(letter, max(values), min(values)) for letter, values in sorted(data.items())]

if __name__ == "__main__":
    print(pregunta_05())