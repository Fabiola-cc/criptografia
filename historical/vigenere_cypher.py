alfabeto_idx = {chr(i): i - ord('a') for i in range(ord('a'), ord('z') + 1)}
alfabeto = [chr(i) for i in range(ord('a'), ord('z') + 1)]

def vigenere_cifrar(mensaje, clave):
    mensaje_cifrado = ""
    len_clave = len(clave)
    for i in range(len(mensaje)):
        char = mensaje[i]
        if char in alfabeto_idx:
            new_index = (alfabeto_idx.get(char) + alfabeto_idx.get(clave[i %len_clave])) % 26
            mensaje_cifrado += alfabeto[new_index]
        else:
            mensaje_cifrado += char
        
    return mensaje_cifrado

def vigenere_descifrar(mensaje, clave):
    mensaje_descifrado = ""
    len_clave = len(clave)
    for i in range(len(mensaje)):
        char = mensaje[i]
        if char in alfabeto_idx:
            new_index = (alfabeto_idx.get(char) - alfabeto_idx.get(clave[i %len_clave])) % 26
            mensaje_descifrado += alfabeto[new_index]
        else:
            mensaje_descifrado += char
        
    return mensaje_descifrado

msg = "hola mundo"
clave = "clave"

cifrado = vigenere_cifrar(msg, clave)
print("Cifrar 'hola mundo' con 'clave': " + cifrado)
print("Descifrado: "+ vigenere_descifrar(cifrado, clave))