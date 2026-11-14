import struct

arxiu_ex = "Archivos de prueba/arxiu_comp.MKI" ## On veurem el comprimit
dades_ex = "0101101110"
ruta_ex = "C:/UAB/2n.Software/Projecte_Final" ## D'on agafem el descomprimit
taula_ex = [('H', 0), ('o', 10), ('l', 110), ('a', 1110)]

## Dades de prova de funcionament

def escriu_MKI (arxiu, ruta, b_taula, b_dades):
   b_ruta = ruta.encode("utf-8") ## Convertim en bytes
   
   with open(arxiu, "wb") as arxiu_MKI:
        arxiu_MKI.write(b"MKI") ## Determinem que es un arxiu .MKI
        
        arxiu_MKI.write(struct.pack("I", len(b_ruta))) ## Primer escribim la llongitud de la cadena
        arxiu_MKI.write(b_ruta) ## Després la informació, aixi sabra fins on llegir
        
        arxiu_MKI.write(struct.pack("H", len(b_taula)))
        arxiu_MKI.write(b_taula)
        
        arxiu_MKI.write(struct.pack("H", len(b_dades)))
        arxiu_MKI.write(b_dades)

escriu_MKI(arxiu_ex, ruta_ex, str(taula_ex).encode("utf-8"), dades_ex.encode("utf-8")) 

## Prova de funcionament