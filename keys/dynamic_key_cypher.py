import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from conversions.ascii_dict import dec_ascii_256, ascii_256
from keys.dynamic_keys import ascii_key


def cifrar_llave_dinamica(mensaje):
    """
    Cifra un mensaje generando una llave del mismo tamaño (One-Time Pad).
    
    Args:
        mensaje: Texto a cifrar
    
    Returns:
        Tupla (texto_cifrado, llave_generada)
    """
    # Generar llave del mismo tamaño que el mensaje
    llave = ascii_key(len(mensaje))
    
    cifrado = ''
    
    for i in range(len(mensaje)):
        # Obtener valores ASCII
        valor_mensaje = ascii_256.get(mensaje[i])
        valor_llave = ascii_256.get(llave[i])
        
        # Operación de cifrado: suma módulo 256
        valor_cifrado = (valor_mensaje + valor_llave) % 256
        
        # Convertir de vuelta a carácter
        cifrado += dec_ascii_256.get(valor_cifrado)
    
    return cifrado, llave


def descifrar_llave_dinamica(cifrado, llave):
    """
    Descifra un mensaje cifrado con llave dinámica.
    
    Args:
        cifrado: Texto cifrado
        llave: Llave usada para cifrar
    
    Returns:
        Texto original
    """
    if len(cifrado) != len(llave):
        raise ValueError("La llave debe tener el mismo tamaño que el mensaje cifrado")
    
    mensaje = ''
    
    for i in range(len(cifrado)):
        # Obtener valores ASCII
        valor_cifrado = ascii_256.get(cifrado[i])
        valor_llave = ascii_256.get(llave[i])
        
        # Operación de descifrado: resta módulo 256
        valor_mensaje = (valor_cifrado - valor_llave) % 256
        
        # Convertir de vuelta a carácter
        mensaje += dec_ascii_256.get(valor_mensaje)
    
    return mensaje


# Ejemplo de uso
if __name__ == "__main__":
    print("CIPHER CON LLAVE DE TAMAÑO DINÁMICO\n")
    
    mensaje_original = "ESTE ES UN MENSAJE SECRETO"
    
    print(f"Mensaje original: {mensaje_original}")
    print(f"Longitud del mensaje: {len(mensaje_original)} caracteres")
    print()
    
    # Cifrar (genera llave automáticamente)
    mensaje_cifrado, llave_generada = cifrar_llave_dinamica(mensaje_original)
    
    print(f"Llave generada (tamaño {len(llave_generada)}): {llave_generada}")
    print(f"Mensaje cifrado: {mensaje_cifrado}")
    print(f"Valores ASCII cifrados: {[ascii_256.get(c) for c in mensaje_cifrado[:10]]}... (primeros 10)")
    print()
    
    # Descifrar
    mensaje_descifrado = descifrar_llave_dinamica(mensaje_cifrado, llave_generada)
    print(f"Mensaje descifrado: {mensaje_descifrado}")
    print()
    
    # Verificación
    if mensaje_original == mensaje_descifrado:
        print("Cifrado y descifrado exitoso!")
    else:
        print("Error en el proceso")
    
    print("\nNota: Con llave dinámica (OTP), cada mensaje tiene una llave única")