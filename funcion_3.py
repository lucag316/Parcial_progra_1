#3. Crear una función que se llame ordenarCaracteres que reciba una cadena de caracteres como parámetro  y su responsabilidad es ordenar los caracteres de manera ascendente dentro de la cadena. Ejemplo si le pasamos "algoritmo" la deja como "agilmoort"

def ordenarCaracteres(cadena_caracteres: str):
    """
    Brief: Ordena la lista segun los parametros que le pases
    
    Parameters:
        cadena_caracteres: str -> La cadena que quiero ordenar
        
    
    Return: Devuelve la cadena que le pasaste pero ordenada ascendentemente
    """
    for i in range(len(cadena_caracteres) - 1):
        for j in range(i + 1, len(cadena_caracteres)):
            if cadena_caracteres[i] > cadena_caracteres[j]: # los mismo: not ascendente
                    aux = cadena_caracteres[i]
                    cadena_caracteres[i] = cadena_caracteres[j]
                    cadena_caracteres[j] = aux

