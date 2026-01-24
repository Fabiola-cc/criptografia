def is_binary_string(s):
    """
    Verifica si una cadena es una representación binaria válida.
    
    Args:
        s (str): La cadena a verificar.
        
    Returns:
        bool: True si la cadena es binaria, False en caso contrario.
    """
    s = s.replace(' ', '').strip()
    return all(c in '01' for c in s) and len(s) > 0

def xor(mensaje, clave):
    """
    Realiza una operación XOR entre el mensaje y la clave.
    
    Args:
        mensaje (str): El mensaje a cifrar o descifrar. (binario)
        clave (str): La clave utilizada para la operación XOR.
        
    Returns:
        str: El resultado de la operación XOR.
    """
    if not is_binary_string(mensaje):
        raise ValueError("El mensaje debe ser una cadena binaria válida.")
    if not is_binary_string(clave):
        raise ValueError("La clave debe ser una cadena binaria válida.")
    
    mensaje = mensaje.replace(' ', '').strip()
    clave = clave.replace(' ', '').strip()

    resultado = []
    for i in range(len(mensaje)):
        mensaje_bit = mensaje[i]
        clave_bit = clave[i % len(clave)]
        xor_bit = '1' if mensaje_bit != clave_bit else '0'
        resultado.append(xor_bit)
        
    return ''.join(resultado)

print(xor("01000001", "01110100"))  # Ejemplo de uso