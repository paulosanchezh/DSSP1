def validar_dni(dni):
    """
    Valida un DNI español (Documento Nacional de Identidad).
    
    El DNI debe tener el formato: 8 dígitos seguidos de una letra.
    
    Args:
        dni (str): El DNI a validar
        
    Returns:
        tuple: (es_valido, mensaje)
    """
    
    # Letras válidas para DNI según el algoritmo de validación
    LETRAS_DNI = "TRWAGMYFPDXBNJZSQVHLCKE"
    
    # Limpiar espacios y convertir a mayúsculas
    dni = dni.strip().upper()
    
    # Validar formato básico
    if len(dni) != 9:
        return False, f"El DNI debe tener exactamente 9 caracteres (8 dígitos + 1 letra). Ingresado: {len(dni)}"
    
    # Separar número y letra
    numero_str = dni[:8]
    letra = dni[8]
    
    # Validar que los primeros 8 caracteres sean dígitos
    if not numero_str.isdigit():
        return False, "Los primeros 8 caracteres deben ser dígitos"
    
    # Validar que el último carácter sea una letra
    if not letra.isalpha():
        return False, "El último carácter debe ser una letra"
    
    # Convertir número a entero
    numero = int(numero_str)
    
    # Calcular la letra correcta usando el algoritmo
    indice = numero % 23
    letra_correcta = LETRAS_DNI[indice]
    
    # Validar que la letra sea correcta
    if letra != letra_correcta:
        return False, f"La letra es incorrecta. Esperaba: {letra_correcta}, Recibido: {letra}"
    
    return True, "DNI válido"


def main():
    """Función principal para probar el validador"""
    
    print("=" * 50)
    print("VALIDADOR DE DNI ESPAÑOL")
    print("=" * 50)
    print()
    
    # Casos de prueba
    casos_prueba = [
        "12345678Z",  # DNI válido
        "12345678A",  # DNI inválido (letra incorrecta)
        "12345678",   # DNI incompleto
        "12345678ZZ", # DNI con caracteres extra
        "ABCDEFGHZ",  # DNI sin dígitos
        "11111111H",  # DNI válido
        "00000000T",  # DNI válido (ceros)
    ]
    
    for dni in casos_prueba:
        es_valido, mensaje = validar_dni(dni)
        estado = "✓ VÁLIDO" if es_valido else "✗ INVÁLIDO"
        print(f"DNI: {dni:15} | {estado:10} | {mensaje}")
    
    print()
    print("=" * 50)
    print("PRUEBA INTERACTIVA")
    print("=" * 50)
    print()
    
    while True:
        dni = input("Ingrese un DNI a validar (o 'salir' para terminar): ").strip()
        
        if dni.lower() == 'salir':
            print("¡Hasta luego!")
            break
        
        if not dni:
            print("Por favor, ingrese un DNI")
            continue
        
        es_valido, mensaje = validar_dni(dni)
        estado = "✓ VÁLIDO" if es_valido else "✗ INVÁLIDO"
        print(f"Resultado: {estado} - {mensaje}")
        print()


if __name__ == "__main__":
    main()
