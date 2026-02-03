from ceasar_cypher import cesar_cifrar, cesar_descifrar

def rot13(mensaje):
    return cesar_cifrar(mensaje, 13)

def rot13_descifrar(mensaje):
    return cesar_descifrar(mensaje, 13)

print("Ejemplo de rot13")
msg = "hola mundo"
cifrado = rot13(msg)
print(" Cifrar 'hola mundo': " + cifrado)
print(" Proceso inverso: " + rot13(cifrado))  # hola mundo
