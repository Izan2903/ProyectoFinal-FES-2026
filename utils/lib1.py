import struct

def leerArchivo(ruta):
    with open(ruta, 'r') as file:
        texto = file.read()
        return texto

def contarCaracteres(texto):
    lista = list(texto)
    tabla = []
    for c in set(lista):
        tabla.append((c,lista.count(c)))
    tabla.sort(key=lambda x: x[1],reverse=True)
    return tabla

def crearIndices(tabla):
    for i in range(len(tabla)):
        indice = ""
        for j in range(0, i):
            indice += "1"
        indice += "0"
        tabla[i]=(tabla[i][0],indice)
<<<<<<< HEAD
    return tabla
=======
    return tabla

def escriu_MKI (arxiu: str, nom: str, taula: list, dades: bytearray):
   ## Convertim en bytes lo que se va a guardar
   b_ruta = nom.encode("utf-8") 
   b_taula = str(taula).encode("utf-8")
   b_dades = dades.encode("utf-8")

   with open(arxiu, "wb") as arxiu_MKI:
        arxiu_MKI.write(b"MKI") ## Determinem que es un arxiu .MKI
        
        arxiu_MKI.write(struct.pack("I", len(b_ruta))) ## Primer escribim la llongitud de la cadena
        arxiu_MKI.write(b_ruta) ## Després la informació, aixi sabra fins on llegir
        
        arxiu_MKI.write(struct.pack("H", len(b_taula)))
        arxiu_MKI.write(b_taula)
        
        arxiu_MKI.write(struct.pack("H", len(b_dades)))
        arxiu_MKI.write(b_dades)
>>>>>>> 43f1a96da5c96d280eae97864d4c15c41e99bba6
