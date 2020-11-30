import cv2
import numpy as np
import types


def messageToBinary(message):
    if type(message) == str:
        return ''.join([format(ord(i), "08b") for i in message])
    elif type(message) == bytes or type(message) == np.ndarray:
        return [format(i, "08b") for i in message]
    elif type(message) == int or type(message) == np.uint8:
        return format(message, "08b")
    else:
        raise TypeError("Input type not supported")


def hideData(image, secret_message):
    n_bytes = image.shape[0] * image.shape[1] * 3 // 8

    if len(secret_message) > n_bytes:
        raise ValueError("Error encountered insufficient bytes, need bigger image or less data !!")

    secret_message += "#####"

    data_index = 0
    binary_secret_msg = messageToBinary(secret_message)

    data_len = len(binary_secret_msg)
    for values in image:
        for pixel in values:
            r, g, b = messageToBinary(pixel)
            if data_index < data_len:
                pixel[0] = int(r[:-1] + binary_secret_msg[data_index], 2)
                data_index += 1
            if data_index < data_len:
                pixel[1] = int(g[:-1] + binary_secret_msg[data_index], 2)
                data_index += 1
            if data_index < data_len:
                pixel[2] = int(b[:-1] + binary_secret_msg[data_index], 2)
                data_index += 1
            if data_index >= data_len:
                break

    return image


def showData(image):
    binary_data = ""
    for values in image:
        for pixel in values:
            r, g, b = messageToBinary(pixel)
            binary_data += r[-1]
            binary_data += g[-1]
            binary_data += b[-1]
    all_bytes = [binary_data[i: i + 8] for i in range(0, len(binary_data), 8)]
    decoded_data = ""
    for byte in all_bytes:
        decoded_data += chr(int(byte, 2))
        if decoded_data[-5:] == "#####":
            break

    return decoded_data[:-5]


def Ingresar_Mensaje():
    image_name = "Proyimag1T.png"
    image = cv2.imread("proyimag1T.png")
    tamaño = image.shape
    altura = tamaño[0]
    anchura = tamaño[1]

    print(f"{image_name} tiene de {anchura} de ancho y de {altura} de alto.")
    print("The original image is as shown below: ")
    cv2.imshow("si soy", image)
    Mensaje = input("Introduzca el mensaje de texto a ocultar: ")
    if (len(Mensaje) == 0):
        raise ValueError('No hay ningún mensaje')

    archivo = "Proyimod1T.png"
    encoded_image = hideData(image, Mensaje)
    cv2.imwrite(archivo, encoded_image)


def Extraer_Mensaje():

    image_name = input("Enter the name of the steganographed image that you want to decode (with extension) :")
    image = cv2.imread(image_name)

    print("The Steganographed image is as shown below: ")

    text = showData(image)
    return text


def Escala_Grises():
    image_name = "Proyimag1T.png"
    img = cv2.imread(image_name)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Escala de grises", gray_img)
    cv2.imwrite('proyimgr1T.png', gray_img)


def Salir():
    print("Gracias por usar el programa!")
    print()
    print("Tenga un buen día!")


def Menu():
    while True:
        a = input("APLICACION ESTEGANO \n 1. Insertar mensaje oculto en una imagen \n 2. Extraer mensaje oculto de una imagen \n 3. Convertir la imagen a escala de grises \n 4. Salir \n Opción: ")
        userinput = int(a)
        if (userinput == 1):
            print("OPCIÓN: Insertar mensaje oculto en una imagen")
            Ingresar_Mensaje()

        elif (userinput == 2):
            print("\nDecoding....")
            print("Decoded message is " + Extraer_Mensaje())
        elif (userinput == 3):
            print("\nOPCIÓN: Convertir la imagen a escala de grises")
            print(f"El fichero de la imagen se llama: proyimag1T.png")
            print("Convirtiendo la imagen a escala de grises...")
            Escala_Grises()
        elif (userinput == 4):
            Salir()
            break
        else:
            print()
            print("Opción no válida")
            print()


Menu()