if __name__ == "__main__":
    # Cadena de texto corrupta y al revés
    texto_corrupto = "sainolac 052 anitnoc ed atecer al"

    # Invertir la cadena
    texto_invertido = texto_corrupto[::-1]

    # Separar el texto en partes
    partes = texto_invertido.split(" ")

    # Extraer el nombre de la receta y las calorías
    nombre_receta = " ".join(partes[3:])  # Unir las palabras que forman el nombre de la receta
    calorias = partes[1]  # Obtener el número de calorías

    # Formatear el texto
    resultado = f"La receta de {nombre_receta} contiene {calorias} calorías."

    # Imprimir el resultado
    print(resultado)