from conversions_binary import binario_decimal
from conversions_base64 import base64_binario
import ascii_dict

def binario_ascii(binario_str):
    """Convierte una cadena de texto en binario a su representación en ASCII.

    Args:
        binario_str (str): Cadena de texto en binario.

    Returns:
        str: Cadena de texto en ASCII.
    """
    # dividir la cadena binaria en bloques de 8 bits
    binario = binario_str.replace(' ', '').strip()
    decimal_values = [binario_decimal(binario[i:i+8]) for i in range(0, len(binario), 8)]

    # convertir bits a carácter ASCII
    ascii_chars = [ascii_dict.dec_ascii_256.get(dv, '') for dv in decimal_values]
    
    return ''.join(ascii_chars)


def base64_ascii(base64_str):
    """Convierte una cadena de texto en Base64 a su representación en ASCII.

    Args:
        base64_str (str): Cadena de texto en Base64.

    Returns:
        str: Cadena de texto en ASCII.
    """
    # decodificar Base64 a binario
    binario = base64_binario(base64_str)

    # convertir binario a caracteres ASCII
    ascii_chars = binario_ascii(binario)
    
    return ''.join(ascii_chars)