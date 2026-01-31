import base64_dict
from conversions_binary import decimal_binario, binario_decimal

def base64_binario(base64_str):
    """Convierte una cadena de texto en Base64 a su representación en binario.

    Args:
        base64_str (str): Cadena de texto en Base64.

    Returns:
        str: Cadena de texto en binario.
    """
    # Contar caracteres de padding
    padding_count = base64_str.count('=')
    
    # Remover '=' para procesamiento
    base64_clean = base64_str.replace('=', '')
    
    # Caracteres Base64 a valores decimales
    decimal_values = [base64_dict.base64_dict.get(char, 0) for char in base64_clean]
    
    # Valores decimales a binario (cada uno de 6 bits)
    bit_stream = ''.join(decimal_binario(dv).zfill(6) for dv in decimal_values)
    
    # Calcular cuántos bits eliminar según el padding
    # Cada '=' representa 2 bits de padding que deben eliminarse
    bits_to_remove = padding_count * 2
    
    if bits_to_remove > 0:
        binary = bit_stream[:-bits_to_remove]
    else:
        binary = bit_stream
    
    return binary


def binario_base64(binario_str):
    """Convierte una cadena de texto en binario a su representación en Base64.

    Args:
        binario_str (str): Cadena de texto en binario.

    Returns:
        str: Cadena de texto en Base64.
    """
    binario = binario_str.replace(' ', '').strip()
    
    # Base64 trabaja con grupos de 24 bits (3 bytes)
    # Calcular cuántos bits faltan para completar el último grupo de 24
    bits_totales = len(binario)
    bits_faltantes = (24 - (bits_totales % 24)) % 24
    
    # Agregar padding de bits (ceros)
    binario += '0' * bits_faltantes
    
    # Convertir cada grupo de 6 bits a decimal
    decimal_values = [
        binario_decimal(binario[i:i+6])
        for i in range(0, len(binario), 6)
    ]
    
    # Convertir decimales a caracteres Base64
    base64_str = ''.join(
        base64_dict.dec_base64.get(value, '')
        for value in decimal_values
    )
    
    # Calcular padding de caracteres '='
    # Esto depende de cuántos bytes completos tenemos
    bytes_originales = bits_totales // 8
    resto_bytes = bytes_originales % 3
    
    if resto_bytes == 1:
        # 1 byte → 8 bits → necesita 16 bits más para 24 → 2 caracteres '='
        base64_str = base64_str[:-2] + '=='
    elif resto_bytes == 2:
        # 2 bytes → 16 bits → necesita 8 bits más para 24 → 1 carácter '='
        base64_str = base64_str[:-1] + '='
    
    return base64_str