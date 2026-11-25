with open('Archivos de prueba/imagen prueba.webp', 'rb') as file:
    prueba = file.read()

with open('Archivos de prueba/Archivo comprimido.txt', 'wb') as file:
<<<<<<< HEAD
    file.write(prueba)
=======
    ##file.write(prueba)
    file.write('holaaa'.encode('utf-8'))
    file.write('adios'.encode('utf-8'))
>>>>>>> 43f1a96da5c96d280eae97864d4c15c41e99bba6
