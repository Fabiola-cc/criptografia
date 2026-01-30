import random
import sys
from pathlib import Path

# Agregar el directorio padre al path
sys.path.append(str(Path(__file__).parent.parent))

from conversions.ascii_dict import dec_ascii_256

def ascii_key(length):
    key = ''
    for i in range(length):
        num = random.randint(33, 126) # numero aleatorio de caracteres imprimibles
        key += dec_ascii_256.get(num) # valor en ascii

    return key

if __name__ == "__main__":
    print("Ejemplo: ")
    print("Llave longitud 3 generada: " + ascii_key(3))