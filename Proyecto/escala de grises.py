from PIL import Image

foto = Image.open("proyimag1T.png")
datos = foto.getdata()
#para el calculo del promedio se utilizara la division entera con el operador de division doble "//" para evitar decimales

promedio = [(datos[x][0] + datos[x][1] + datos[x][2]) // 3 for x in range(len(datos))]
imagen_gris = Image.new("L", foto.size)
imagen_gris.putdata(promedio)
imagen_gris.save("C:/Users/34620/Desktop/Trabajo Programación/fotofinal.png")
foto.close()
imagen_gris.close()
