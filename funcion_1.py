# 1. Crear una función llamada aplicarAumento que reciba como parámetro el precio de un producto y devuelva el valor del producto con un aumento del 5%. Realizar la llamada desde el main.

def aplicarAumento(precio_producto: float) -> float:
    """
    Brief: Aumenta el 5% al precio pasado por parametro
    
    Parameters:
        precio_producto: float -> El precio al que quiero darle el aumento
        
    Return: Retorna el precio con el aumento, en caso de error retorna -1
    """
    retorno = -1
    if type(precio_producto) == type(float()):
        aumento = precio_producto * 0.05
        precio_con_aumento = precio_producto + aumento
        retorno = precio_con_aumento
    return retorno

#print(aplicarAumento(100.0))