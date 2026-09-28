# El cifrado Cesar desplaza cada letra un numero
# fijo de posiciones en el alfabeto.
from langdetect import detect

#https://pypi.org/project/langdetect/
# Langdetect es una libreria que detecta el idioma de un texto.
    # Detect es una funcion que detecta el idioma de un texto y devuelve el codigo del idioma.
    # Detect_langs es una funcion que detecta el idioma de un texto y devuelve una lista de objetos con el codigo del idioma y la probabilidad de que sea ese idioma.

mensaje = "Uunejvxb dw vdwmx wdnex jzdr, nw wdnbcaxb lxajixwnb"
abc = "abcdefghijklmnopqrstuvwxyz"

def cesar(mensaje):
    # Detecta el idioma del mensaje y lo imprime.
    for clave in range(26): 
        # Prueba cada clave de desplazamiento.
        resul=""
        for char in mensaje:
            # Si el caracter es una letra, se desplaza y se agrega a la variable resul.
            char=char.lower()
            if char not in abc: 
                # Si el caracter no es una letra, se agrega a la variable resul sin cambios.
                resul+=char
                # continue :el bucle continua con la siguiente iteracion.
                continue 
            #index : devuelve el indice de un elemento en una lista.
            # + clave : se suma la clave al indice del caracter.
            # % 26 : se obtiene el resto de la division entre 26.
            resul+=abc[(abc.index(char)+clave)%26]
   
    # Try porque detect puede lanzar una excepcion si no puede detectar el idioma.
    try: 
        if detect(resul) == "es":
            return resul
    except:
        pass

    return None

if __name__ == "__main__":
    print("Mensaje cifrado: ", mensaje)
    print("Mensaje descifrado: ", cesar(mensaje))