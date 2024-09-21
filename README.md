
# TextoUtils - Biblioteca para Manipulación de Texto en Python

**TextoUtils** es una biblioteca simple y poderosa para realizar operaciones comunes sobre archivos de texto, como buscar, reemplazar, eliminar comentarios, contar palabras, y mucho más. Este módulo está diseñado para ser fácil de usar y personalizar.

## Instalación

1. Clona este repositorio o descarga el archivo `texto_utils.py` y agrégalo a tu proyecto.
2. Importa la clase `TextoUtils` en tu archivo Python para usar las funciones.

## Uso Básico

A continuación se presentan algunos ejemplos sencillos de cómo utilizar `TextoUtils`:

### Leer un archivo
```python
from texto_utils import TextoUtils

contenido = TextoUtils.leer_archivo('archivo.txt')
print(contenido)
```

### Reemplazar texto
```python
contenido_modificado = TextoUtils.reemplazar_texto(contenido, 'Python', 'C++')
```

### Contar palabras
```python
total_palabras = TextoUtils.contar_palabras(contenido)
print(f"El archivo tiene {total_palabras} palabras.")
```

## Funcionalidades

1. **leer_archivo(ruta)**: Lee un archivo de texto y devuelve una lista de líneas.
2. **escribir_archivo(ruta, contenido)**: Escribe una lista de líneas en un archivo.
3. **buscar_texto(texto, palabra, mostrar_lineas=False)**: Busca una palabra en el texto y devuelve sus índices.
4. **reemplazar_texto(texto, antiguo, nuevo, case_sensitive=False)**: Reemplaza una palabra por otra.
5. **quitar_comentarios(texto, tipo='python')**: Elimina comentarios de archivos Python o HTML.
6. **contar_palabras(texto)**: Cuenta cuántas palabras hay en el texto.
7. **extraer_patron(texto, patron)**: Extrae coincidencias usando expresiones regulares.
8. **capitalizar_texto(texto, solo_primera=False)**: Capitaliza el texto según la configuración.
9. **dividir_archivo_en_partes(texto, num_partes)**: Divide el archivo en partes iguales.

## Ejemplos adicionales

Consulta el archivo `ejemplo.py` para ver ejemplos más avanzados de uso.

## Licencia

Este proyecto está bajo la licencia MIT.
