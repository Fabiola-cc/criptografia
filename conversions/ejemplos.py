"""
EJEMPLOS DE USO DE LAS FUNCIONES DE CRIPTOGRAFÍA
==================================================
Este archivo demuestra cómo usar todas las funciones disponibles en el proyecto.
"""

# ============================================================================
# 1. CONVERSIONES BINARIAS
# ============================================================================
print("\n")
print("1. CONVERSIONES BINARIAS")

from conversions_binary import decimal_binario, binario_decimal

# Ejemplo 1.1: Convertir decimal a binario
decimal = 65
binario = decimal_binario(decimal)
print(f"\nEjemplo 1.1 - Decimal a Binario:")
print(f"  Decimal: {decimal} → Binario: {binario}")

# Ejemplo 1.2: Convertir binario a decimal
binario = "1010101"
decimal = binario_decimal(binario)
print(f"\nEjemplo 1.2 - Binario a Decimal:")
print(f"  Binario: {binario} → Decimal: {decimal}")

# Ejemplo 1.3: Convertir varios números
numeros = [10, 50, 100, 255]
print(f"\nEjemplo 1.3 - Conversiones múltiples:")
for num in numeros:
    print(f"  {num:3d} → {decimal_binario(num)}")


# ============================================================================
# 2. CONVERSIONES ASCII
# ============================================================================
print("\n")
print("2. CONVERSIONES ASCII")

from conversions_ascii import ascii_decimal, ascii_binario

# Ejemplo 2.1: Texto ASCII a decimal
texto = "Hola"
decimales = ascii_decimal(texto)
print(f"\nEjemplo 2.1 - ASCII a Decimal:")
print(f"  Texto: '{texto}'")
print(f"  Decimales: {decimales}")
for char, dec in zip(texto, decimales):
    print(f"    '{char}' → {dec}")

# Ejemplo 2.2: Texto ASCII a binario
texto = "ABC"
binario = ascii_binario(texto)
print(f"\nEjemplo 2.2 - ASCII a Binario:")
print(f"  Texto: '{texto}'")
print(f"  Binario: {binario}")

# Ejemplo 2.3: Conversión con caracteres especiales
texto = "A1!"
decimales = ascii_decimal(texto)
print(f"\nEjemplo 2.3 - ASCII especial a Decimal:")
print(f"  Texto: '{texto}'")
print(f"  Decimales: {decimales}")


# ============================================================================
# 3. CONVERSIONES BASE64
# ============================================================================
print("\n")
print("3. CONVERSIONES BASE64")

from conversions_base64 import base64_binario, binario_base64

# Ejemplo 3.1: Base64 a binario
base64_str = "SGVsbG8="
binario = base64_binario(base64_str)
print(f"\nEjemplo 3.1 - Base64 a Binario:")
print(f"  Base64: {base64_str}")
print(f"  Binario: {binario}")

# Ejemplo 3.2: Binario a Base64
binario = "010100 010101 010110 010111"
base64_str = binario_base64(binario)
print(f"\nEjemplo 3.2 - Binario a Base64:")
print(f"  Binario: {binario}")
print(f"  Base64: {base64_str}")


# ============================================================================
# 4. CONVERSIONES ENTRE ASCII Y BASE64
# ============================================================================
print("\n")
print("4. CONVERSIONES ASCII <-> BASE64")

from conv_base64_ascii import binario_ascii, base64_ascii

# Ejemplo 4.1: Binario a ASCII
binario = "01001000 01100101 01101100 01101100 01101111"  # "Hello"
ascii_texto = binario_ascii(binario)
print(f"\nEjemplo 4.1 - Binario a ASCII:")
print(f"  Binario: {binario}")
print(f"  ASCII: '{ascii_texto}'")

# Ejemplo 4.2: Base64 a ASCII (requiere decodificación)
print(f"\nEjemplo 4.2 - Base64 a ASCII:")
base64_str = binario_base64(binario)
ascii_b64 = base64_ascii(base64_str)
print(f"  Base64: {base64_str}")
print(f"  ASCII: '{ascii_b64}'")