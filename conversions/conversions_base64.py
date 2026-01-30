import base64_dict
from conversions_binary import decimal_binario, binario_decimal

def base64_binario(base64_str):
    """Convierte una cadena de texto en Base64 a su representación en binario.

    Args:
        base64_str (str): Cadena de texto en Base64.

    Returns:
        str: Cadena de texto en binario.
    """
    # caracteres Base64 a valores decimales # 18 4 29 47 27 4 1 0
    decimal_values = [base64_dict.base64_dict.get(char, 0) for char in base64_str]
    
    # valores decimales a binario
    binary_values = [decimal_binario(dv).zfill(6) for dv in decimal_values]

    # bloques de 8 bits para formar bytes
    return ' '.join(binary_values)


def binario_base64(binario_str):
    """Convierte una cadena de texto en binario a su representación en Base64.

    Args:
        binario_str (str): Cadena de texto en binario.

    Returns:
        str: Cadena de texto en Base64.
    """
    # dividir la cadena binaria en bloques de 6 bits
    binario = binario_str.replace(' ', '').strip()

    # convertir cada bloque de 6 bits a su valor decimal
    decimal_values = [binario_decimal(binario[i:i+6]) for i in range(0, len(binario), 6)]
    
    # convertir los valores decimales a Base64
    base64_str = ""
    for value in decimal_values:
        base64_str += base64_dict.dec_base64.get(value, '')
    
    return base64_str