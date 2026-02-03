from ceasar_cypher import cesar_cifrar, cesar_descifrar

def rot13(mensaje):
    """
    Aplica el cifrado ROT13 a un mensaje.

    ROT13 es un caso especial del Cifrado César con un desplazamiento fijo
    de 13 posiciones. El mismo algoritmo se utiliza tanto para cifrar
    como para descifrar.

    :param mensaje: texto que se desea cifrar o descifrar
    :return: mensaje transformado con ROT13
    """
    return cesar_cifrar(mensaje, 13)

def rot13_descifrar(mensaje):
    return cesar_descifrar(mensaje, 13)

print("Ejemplo de rot13")
msg = "hola mundo"
cifrado = rot13(msg)
print(" Cifrar 'hola mundo': " + cifrado)
print(" Proceso inverso: " + rot13(cifrado))  # hola mundo
