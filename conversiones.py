import ascii_dict
import base64_dict

def decimal_binario(num):
    """Convierte un número decimal a su representación en binario.

    Args:
        num (int): Número decimal.

    Returns:
        str: Cadena de texto en binario.
    """
    if num == 0:
        return '0'
    if num == 1:
        return '1'
    binary_str = ''
    while num > 0:
        binary_str = str(num % 2) + binary_str
        num = num // 2
    return binary_str

def binario_decimal(bin_str):
    """Convierte una cadena de texto en binario a su representación en decimal.

    Args:
        bin_str (str): Cadena de texto en binario.

    Returns:
        int: Número decimal.
    """
    decimal_value = 0
    bin_str = bin_str[::-1]  # invertir la cadena para facilitar el cálculo
    for index, digit in enumerate(bin_str):
        if digit == '1':
            decimal_value += 2 ** index
    return decimal_value

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

def base64_binario(base64_str):
    """Convierte una cadena de texto en Base64 a su representación en binario.

    Args:
        base64_str (str): Cadena de texto en Base64.

    Returns:
        str: Cadena de texto en binario.
    """
    # caracteres Base64 a valores decimales
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
    binary_values = [binario_decimal(binario[i:i+6]) for i in range(0, len(binario), 6)]

    # convertir cada bloque de 6 bits a su valor decimal
    decimal_values = [int(bv, 2) for bv in binary_values]
    
    # convertir los valores decimales a Base64
    base64_str = ""
    for value in decimal_values:
        base64_str += base64_dict.dec_base64.get(value, '')
    
    return base64_str

def binario_ascii(binario_str):
    """Convierte una cadena de texto en binario a su representación en ASCII.

    Args:
        binario_str (str): Cadena de texto en binario.

    Returns:
        str: Cadena de texto en ASCII.
    """
    # dividir la cadena binaria en bloques de 8 bits
    binario = binario_str.replace(' ', '').strip()
    binary_values = [binario_decimal(binario[i:i+8]) for i in range(0, len(binario), 8)]

    # convertir cada bloque de 8 bits a su valor decimal 
    decimal_values = [decimal_binario(bv) for bv in binary_values]

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

print("Pruebas de conversión:")
print("Decimal a Binario de 10:", decimal_binario(10))  # Salida: '1010'

print("ASCII a Decimal de 'Hola':", ascii_decimal("Hola"))  # Salida: [72, 111, 108, 97]