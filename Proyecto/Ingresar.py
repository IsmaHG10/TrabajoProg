from PIL import Image
import math

caracter_terminacion = [1, 1, 1, 1, 1, 1, 1, 1]


def Mostrar_Ancho_Alto():
    imagen = Image.open("proyimag1T.png")
    tamaño = imagen.size
    anchura = tamaño[0]
    altura = tamaño[1]
    print(f"{imagen} tiene de {anchura} de ancho y de {altura} de alto.")
    imagen.show(imagen)

def Ocultar_Texto(mensaje, ruta_imagen_original, ruta_imagen_salida="salida.png"):
    print("Insertando el texto en la imagen......".format(mensaje))


print("OPCIÓN: Insertar mensaje oculto en una imagen")
print()
Mostrar_Ancho_Alto()
print()
Ocultar_Texto(input("Introduzca el mensaje de texto a ocultar: "), "proyimag1T.png", "proyimod1T.png")
print()
print("El fichero proyimag1T.png es diferente a proyimod1T.png")
