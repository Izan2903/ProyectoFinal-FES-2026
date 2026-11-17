with open('Archivos de prueba/imagen prueba.webp', 'rb') as file:
    prueba = file.read()

with open('Archivos de prueba/Archivo comprimido.txt', 'wb') as file:
    ##file.write(prueba)
    file.write('holaaa'.encode('utf-8'))
    file.write('adios'.encode('utf-8'))