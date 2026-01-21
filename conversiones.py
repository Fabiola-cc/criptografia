import base64
import textwrap

def ascii_binario(texto):
    """Convierte una cadena de texto ASCII a su representación en binario.

    Args:
        texto (str): Cadena de texto en ASCII.

    Returns:
        str: Cadena de texto en binario.
    """
    binary_values = [format(ord(char), '08b') for char in texto]
    return ' '.join(binary_values)

def base64_binario(base64_str):
    """Convierte una cadena de texto en Base64 a su representación en binario.

    Args:
        base64_str (str): Cadena de texto en Base64.

    Returns:
        str: Cadena de texto en binario.
    """
    # caracteres Base64 a valores decimales
    decimal_values = base64.b64decode(base64_str)
    
    # valores decimales a binario
    binary_values = [format(byte, '08b') for byte in decimal_values]

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
    binary_values = textwrap.wrap(binario, 6)

    # convertir cada bloque de 6 bits a su valor decimal
    decimal_values = [int(bv, 2) for bv in binary_values]
    
    # convertir los valores decimales a Base64
    base64_str = ""
    for value in decimal_values: # TODO revisar si esto funciona correctamente
        base64_str += base64.b64encode(bytes([value])).decode('utf-8').rstrip('=') 
    
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
    binary_values = textwrap.wrap(binario, 8)

    # convertir cada bloque de 8 bits a su valor decimal 
    decimal_values = [int(bv, 2) for bv in binary_values]

    # convertir bits a carácter ASCII
    ascii_chars = [chr(dv) for dv in decimal_values]
    
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
texto = "Hola"
print(f"Texto ASCII: {texto}")

binario = ascii_binario(texto)
print(f"ASCII a Binario: {binario}")

base64_str = binario_base64(binario)
print(f"Binario a Base64: {base64_str}")

ascii_reconstruido = base64_ascii(base64_str)
print(f"Base64 a ASCII: {ascii_reconstruido}")