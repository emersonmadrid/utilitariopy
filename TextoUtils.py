import re
import os

class TextoUtils:
    @staticmethod
    def leer_archivo(ruta):
        """Lee el contenido de un archivo y lo devuelve como una lista de líneas. Maneja excepciones si el archivo no existe."""
        if not os.path.exists(ruta):
            raise FileNotFoundError(f"El archivo {ruta} no existe.")
        with open(ruta, 'r', encoding='utf-8') as archivo:
            return archivo.readlines()

    @staticmethod
    def escribir_archivo(ruta, contenido):
        """Escribe una lista de líneas en un archivo. Maneja excepciones si no se puede escribir."""
        try:
            with open(ruta, 'w', encoding='utf-8') as archivo:
                archivo.writelines(contenido)
            print(f"El archivo se ha guardado correctamente en {ruta}.")
        except Exception as e:
            raise IOError(f"No se pudo escribir en el archivo {ruta}. Error: {e}")

    @staticmethod
    def buscar_texto(texto, palabra, mostrar_lineas=False):
        """
        Busca todas las ocurrencias de una palabra en el texto y devuelve sus índices.
        Si mostrar_lineas es True, también muestra las líneas donde se encuentra la palabra.
        """
        indices = [i for i, linea in enumerate(texto) if palabra in linea]
        if mostrar_lineas:
            for i in indices:
                print(f"Línea {i + 1}: {texto[i].strip()}")
        return indices

    @staticmethod
    def reemplazar_texto(texto, antiguo, nuevo, case_sensitive=False):
        """
        Reemplaza todas las ocurrencias de una palabra antigua por una nueva.
        Si case_sensitive es False, no distingue entre mayúsculas y minúsculas.
        """
        if not case_sensitive:
            return [re.sub(re.escape(antiguo), nuevo, linea, flags=re.IGNORECASE) for linea in texto]
        return [linea.replace(antiguo, nuevo) for linea in texto]

    @staticmethod
    def quitar_comentarios(texto, tipo='python'):
        """
        Elimina comentarios de archivos de diferentes lenguajes. 
        Soporta comentarios de Python, HTML y XML.
        """
        if tipo == 'python':
            # Quita comentarios de Python (líneas que comienzan con '#')
            return [linea for linea in texto if not linea.strip().startswith('#')]
        elif tipo in ['html', 'xml']:
            # Quita comentarios en HTML o XML (entre <!-- y -->, soporta comentarios multilínea)
            texto_completo = ''.join(texto)
            texto_sin_comentarios = re.sub(r'<!--[\s\S]*?-->', '', texto_completo)
            return texto_sin_comentarios.splitlines(keepends=True)
        else:
            raise ValueError("Tipo de comentario no soportado. Use 'python', 'html', o 'xml'.")
    @staticmethod
    def contar_palabras(texto):
        """Cuenta el número total de palabras en el texto."""
        palabras = " ".join(texto).split()
        return len(palabras)

    @staticmethod
    def extraer_patron(texto, patron):
        """Extrae todas las coincidencias de un patrón de expresión regular en el texto."""
        coincidencias = []
        for linea in texto:
            coincidencias.extend(re.findall(patron, linea))
        return coincidencias

    @staticmethod
    def capitalizar_texto(texto, solo_primera=False):
        """
        Capitaliza el texto.
        Si solo_primera es True, solo convierte la primera letra de cada línea a mayúscula.
        """
        if solo_primera:
            return [linea.capitalize() for linea in texto]
        return [linea.title() for linea in texto]

    @staticmethod
    def dividir_archivo_en_partes(texto, num_partes):
        """
        Divide el archivo en un número especificado de partes iguales.
        """
        longitud = len(texto)
        tamano_parte = longitud // num_partes
        partes = [texto[i:i + tamano_parte] for i in range(0, longitud, tamano_parte)]
        return partes

