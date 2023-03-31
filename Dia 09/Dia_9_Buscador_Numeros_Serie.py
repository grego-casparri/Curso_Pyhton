import os
import re
import datetime
import time

# Función para encontrar números de serie en un archivo
def buscar_numero_serie(archivo):
    with open(archivo, 'r') as f:
        contenido = f.read()
        patron = r'N\w{3}-\d{5}'
        resultado = re.findall(patron, contenido)
        if resultado:
            return resultado[0]
        else:
            return None

# Función principal
def buscar_numeros_serie(directorio_raiz):
    # Obtener la fecha de hoy
    fecha_hoy = datetime.date.today().strftime('%d/%m/%y')

    # Iniciar el cronómetro
    tiempo_inicio = time.time()

    # Recorrer el árbol de carpetas
    numeros_serie = []
    for raiz, carpetas, archivos in os.walk(directorio_raiz):
        for archivo in archivos:
            ruta_archivo = os.path.join(raiz, archivo)
            numero_serie = buscar_numero_serie(ruta_archivo)
            if numero_serie:
                numeros_serie.append((ruta_archivo, numero_serie))

    # Detener el cronómetro y calcular la duración de la búsqueda
    tiempo_fin = time.time()
    duracion = round(tiempo_fin - tiempo_inicio)

    # Mostrar los resultados en formato de tabla
    print('-' * 50)
    print(f'Fecha de búsqueda: {fecha_hoy}\n')
    print('ARCHIVO\t\tNRO. SERIE')
    print('-' * 50)
    for archivo, numero_serie in numeros_serie:
        print(f'{archivo}\t{numero_serie}')
    print('-' * 50)
    print(f'\nNúmeros encontrados: {len(numeros_serie)}')
    print(f'Duración de la búsqueda: {duracion} segundos')
    print('-' * 50)

# Ejemplo de uso
buscar_numeros_serie('C:\\Users\\Gregorio Casparri\\Documents\\Cursos\\Python\\Dia 9')
