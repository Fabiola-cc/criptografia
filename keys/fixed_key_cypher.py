import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from conversions.ascii_dict import dec_ascii_256, ascii_256
from dynamic_keys import ascii_key

def cifrar_llave_fija(mensaje, llave):
    """
    Cifra un mensaje usando una llave de tamaño fijo que se repite cíclicamente.
    
    Args:
        mensaje: Texto a cifrar
        llave: Llave de cifrado (tamaño fijo)
    
    Returns:
        Texto cifrado
    """
    cifrado = ''
    len_llave = len(llave)
    
    for i in range(len(mensaje)):
        # Obtener valores ASCII
        valor_mensaje = ascii_256.get(mensaje[i])
        valor_llave = ascii_256.get(llave[i % len_llave])  # Se repite cíclicamente
        
        # Operación de cifrado: suma módulo 256
        valor_cifrado = (valor_mensaje + valor_llave) % 256
        
        # Convertir de vuelta a carácter
        cifrado += dec_ascii_256.get(valor_cifrado)
    
    return cifrado


def descifrar_llave_fija(cifrado, llave):
    """
    Descifra un mensaje cifrado con llave de tamaño fijo.
    
    Args:
        cifrado: Texto cifrado
        llave: Llave de descifrado (la misma usada para cifrar)
    
    Returns:
        Texto original
    """
    mensaje = ''
    len_llave = len(llave)
    
    for i in range(len(cifrado)):
        # Obtener valores ASCII
        valor_cifrado = ascii_256.get(cifrado[i])
        valor_llave = ascii_256.get(llave[i % len_llave])
        
        # Operación de descifrado: resta módulo 256
        valor_mensaje = (valor_cifrado - valor_llave) % 256
        
        # Convertir de vuelta a carácter
        mensaje += dec_ascii_256.get(valor_mensaje)
    
    return mensaje


# Ejemplo de uso
if __name__ == "__main__":
    print("CIPHER CON LLAVE DE TAMAÑO FIJO\n")
    
    mensaje_original = "HOLA MUNDO"
    llave = ascii_key(5) # Llave de tamaño fijo (5 caracteres)
    
    print(f"Mensaje original: {mensaje_original}")
    print(f"Llave (tamaño {len(llave)}): {llave}")
    print()
    
    # Cifrar
    mensaje_cifrado = cifrar_llave_fija(mensaje_original, llave)
    print(f"Mensaje cifrado: {mensaje_cifrado}")
    print(f"Valores ASCII cifrados: {[ascii_256.get(c) for c in mensaje_cifrado]}")
    print()
    
    # Descifrar
    mensaje_descifrado = descifrar_llave_fija(mensaje_cifrado, llave)
    print(f"Mensaje descifrado: {mensaje_descifrado}")
    print()
    
    # Verificación
    if mensaje_original == mensaje_descifrado:
        print("Cifrado y descifrado exitoso!")
    else:
        print("Error en el proceso")