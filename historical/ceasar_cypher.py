alfabeto_idx = {chr(i): i - ord('a') for i in range(ord('a'), ord('z') + 1)}
alfabeto = [chr(i) for i in range(ord('a'), ord('z') + 1)]

def cesar_cifrar(mensaje, desplazamiento):
    """
    Cifra un mensaje utilizando el Cifrado César.

    Cada letra del mensaje es desplazada un número fijo de posiciones
    en el alfabeto. El cifrado es reversible usando el mismo
    desplazamiento en sentido contrario.

    :param mensaje: texto que se desea cifrar
    :param desplazamiento: número de posiciones a desplazar en el alfabeto
    :return: mensaje cifrado
    """
    mensaje_cifrado = ""
    for char in mensaje:
        if char in alfabeto_idx:
            new_position = (alfabeto_idx[char] + desplazamiento) % 26
            mensaje_cifrado += alfabeto[new_position]
        else:
            mensaje_cifrado += char
        
    return mensaje_cifrado

def cesar_descifrar(mensaje, desplazamiento):
    """
    Descifra un mensaje cifrado con el Cifrado César.

    Aplica el desplazamiento inverso para recuperar el mensaje original.

    :param mensaje: texto cifrado que se desea descifrar
    :param desplazamiento: número de posiciones usadas en el cifrado
    :return: mensaje descifrado
    """
    mensaje_descifrado = ""
    for char in mensaje:
        if char in alfabeto_idx:
            new_position = (alfabeto_idx[char] - desplazamiento) % 26
            mensaje_descifrado += alfabeto[new_position]
        else:
            mensaje_descifrado += char
    
    return mensaje_descifrado

print("Ejemplo de ceasar cypher")
msg = "hola mundo"
cifrado = cesar_cifrar(msg, 4)
print(" Cifrar 'hola mundo' con desplazamiento 4: " + cifrado)
print(" Proceso inverso: " + cesar_descifrar(cifrado, 4))  # hola mundo

