# 2. Crear una función que se llame reemplazarCaracteres que reciba una cadena de caracteres como primer parámetro, un carácter como segundo y otro carácter  como tercero,  la misma deberá reemplazar cada ocurrencia del segundo parámetro por el tercero y devolver la cantidad de veces que se reemplazo ese carácter  en la cadena

def reemplazarCaracteres(cadena: str, caracter: str, caracter_2: str) -> int:
    """
    Brief:La funcion reeemplaza caracteres segun los parametros recibidos y cuenta cuantos se reemplaron
    
    Parameters:
        cadena: str -> La cadena de caracteres que quiero utilizar
        caracter: str -> El caracter que quiere reemplazar
        caracter_2: str -> El caracter por el cual quiere reemplazar
    
    Return: Retorna la cantidad de caracteres reemplzados, -1 en caso de error
    """
    retorno = -1
    if type(cadena) == type(str()) and type(caracter) == type(str()) and type(caracter_2) == type(str()):
        cantidad_reemplazo = cadena.count(caracter)
        reemplazado = cadena.replace(caracter, caracter_2)
        retorno = cantidad_reemplazo
    return retorno


#print(reemplazarCaracteres("hola como estas", "a", "A"))


