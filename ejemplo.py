from TextoUtils import TextoUtils

# Leer el archivo XML
contenido_xml = TextoUtils.leer_archivo('archivo.xml')

# Quitar los comentarios del archivo XML
contenido_sin_comentarios = TextoUtils.quitar_comentarios(contenido_xml, tipo='xml')

# Imprimir el contenido sin comentarios
print("Contenido sin comentarios:")
print("".join(contenido_sin_comentarios))

# Opcional: Guardar el archivo sin comentarios
TextoUtils.escribir_archivo('archivo_sin_comentarios.xml', contenido_sin_comentarios)

print("El archivo XML sin comentarios ha sido guardado como 'archivo_sin_comentarios.xml'.")
