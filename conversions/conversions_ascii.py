import ascii_dict
from conversions_binary import decimal_binario

def ascii_decimal(texto):
    """Convierte una cadena de texto ASCII a su representación en decimal.

    Args:
        texto (str): Cadena de texto en ASCII.

    Returns:
        list: Lista de valores decimales correspondientes a cada carácter.
    """

    decimal_values = []
    for char in texto:
        decimal_values.append(ascii_dict.ascii_256.get(char, 0))
    return decimal_values

def ascii_binario(texto):
    """Convierte una cadena de texto ASCII a su representación en binario.

    Args:
        texto (str): Cadena de texto en ASCII.

    Returns:
        str: Cadena de texto en binario.
    """
    decimal_values = ascii_decimal(texto)
    binary_values = [decimal_binario(dv) for dv in decimal_values]
    return ' '.join(binary_values)