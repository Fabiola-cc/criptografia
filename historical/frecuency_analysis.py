frecuencia_es = {
    'e': 0.137,'a': 0.125,'o': 0.087,'s': 0.079,'n': 0.070,'r': 0.069,'i': 0.062,
    'l': 0.049,'d': 0.047,'t': 0.046,'c': 0.044,'u': 0.039,'m': 0.031,'p': 0.025,
    'b': 0.014,'g': 0.010,'v': 0.009,'y': 0.009,'q': 0.009,'h': 0.007,'f': 0.005,
    'z': 0.005,'j': 0.004,'x': 0.001,'k': 0.000,'w': 0.000 #, 'ñ': ~0.003
}

frecuencia_en = {
    'e': 0.127,'t': 0.091,'a': 0.082,'o': 0.075,'i': 0.070,'n': 0.067,'s': 0.063,
    'h': 0.061,'r': 0.060,'d': 0.043,'l': 0.040,'c': 0.028,'u': 0.028,'m': 0.024,
    'w': 0.024,'f': 0.022,'g': 0.020,'y': 0.020,'p': 0.019,'b': 0.015,'v': 0.010,
    'k': 0.008,'j': 0.002,'x': 0.002,'q': 0.001,'z': 0.001
}

from collections import Counter

def frecuencias(mensaje):
    letras = [c for c in mensaje.lower() if 'a' <= c <= 'z']
    total = len(letras)

    if total == 0:
        return {}

    conteo = Counter(letras)

    freq = {
        chr(i): conteo.get(chr(i), 0) / total
        for i in range(ord('a'), ord('z') + 1)
    }

    return freq

def ordenar_frecuencia(freq):
    return sorted(freq.items(), key=lambda x: x[1], reverse=True)


mensaje = "Este es un mensaje de prueba para analizar frecuencias"
    
print("Mensaje original:")
print(mensaje)
print()

freq = frecuencias(mensaje)

print("Frecuencias encontradas (ordenadas):")
for letra, valor in ordenar_frecuencia(freq):
    print(f"{letra}: {valor:.3f}")