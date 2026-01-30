def decimal_binario(num):
    """Convierte un número decimal a su representación en binario.

    Args:
        num (int): Número decimal.

    Returns:
        str: Cadena de texto en binario.
    """
    if num == 0:
        return '0'
    if num == 1:
        return '1'
    binary_str = ''
    while num > 0:
        binary_str = str(num % 2) + binary_str
        num = num // 2
    return binary_str

def binario_decimal(bin_str):
    """Convierte una cadena de texto en binario a su representación en decimal.

    Args:
        bin_str (str): Cadena de texto en binario.

    Returns:
        int: Número decimal.
    """
    decimal_value = 0
    bin_str = bin_str[::-1]  # invertir la cadena para facilitar el cálculo
    for index, digit in enumerate(bin_str):
        if digit == '1':
            decimal_value += 2 ** index
    return decimal_value