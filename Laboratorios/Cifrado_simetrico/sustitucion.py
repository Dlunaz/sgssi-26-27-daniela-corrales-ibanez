
texto_entrada = "RIJ AZKKZHC PIKCE XT ACKCUXJHX SZX, E NZ PEJXKE, PXGIK XFDKXNEQE RIPI RIPQEHCK ET OENRCNPI AXNAX ZJ RKCHXKCI AX CJAXDXJAXJRCE AX RTENX, E ACOXKXJRCE AXT RITEQIKERCIJCNPI OKXJHXDIDZTCNHE AX TE ACKXRRCIJ EJEKSZCNHE. AZKKZHC OZX ZJ OERHIK AX DKCPXK IKAXJ XJ XT DEDXT AX TE RTENX IQKXKE XJ REHETZJVE XJ GZTCI AX 1936. DXKI AZKKZHC, RIPI IRZKKX RIJ TEN DXKNIJETCAEAXN XJ TE MCNHIKCE, JI REVI AXT RCXTI. DXKNIJCOCREQE TE HKEACRCIJ KXvITZRCIJEKCE AX TE RTENX IQKXKE. NZ XJIKPX DIDZTEKCAEA XJHKX TE RTENX HKEQEGEAIKE, KXOTXGEAE XJ XT XJHCXKKI PZTHCHZACJEKCI XJ QEKRXTIJE XT 22 AX JIvCXPQKX AX 1936, PZXNHKE XNE CAXJHCOCRERCIJ. NZ PZXKHX OZX NCJ AZAE ZJ UITDX IQGXHCvI ET DKIRXNI KXvITZRCIJEKCI XJ PEKRME. NCJ AZKKZHC SZXAI PEN TCQKX XT REPCJI DEKE SZX XT XNHETCJCNPI, RIJ TE RIPDTCRCAEA AXT UIQCXKJI AXT OKXJHX DIDZTEK V AX TE ACKXRRCIJ EJEKSZCNHE, HXKPCJEKE XJ PEVI AX 1937 TE HEKXE AX TCSZCAEK TE KXvITZRCIJ, AXNPIKETCLEJAI E TE RTENX IQKXKE V OERCTCHEJAI RIJ XTTI XT DINHXKCIK HKCZJOI OKEJSZCNHE."
frecuencias = ['e', 'a', 'o', 'l', 's', 'n', 'd', 'r', 'u', 'i', 'c', 't', 'p', 'm', 'y', 'q', 'b', 'h', 'g', 'f', 'v', 'j', 'ñ', 'z', 'x', 'k', 'w']

def contar_frecuencias(texto):
    frecuencia_texto = {}
    for letter in "abcdefghijklmnñopqrstuvwxyz":
        frecuencia_texto[letter] = 0

    for character in texto:
        character = character.lower()
        if character not in frecuencias:
            continue
        frecuencia_texto[character] += 1
    return frecuencia_texto

def diccionario_a_lista_ordenada(dict_frecuencias):
    lista_tuplas = list(dict_frecuencias.items()) # lo convertimos en una lista de tuplas, [('a', 1), ('b', 0) ...

    def obtener_frecuencia(tupla): # Devuelve la frecuencia (segundo elemento de la tupla)
        return tupla[1]  
    
    # Ordenar la lista por frecuencia de mayor a menor, la key hace que lo que se compare sea la frecuencia
    lista_ordenada_tuplas = sorted(lista_tuplas, key=obtener_frecuencia, reverse=True)
    lista_ordenada = []
    for letra, frec in lista_ordenada_tuplas:
        lista_ordenada.append(letra)
    
    return lista_ordenada



def sustituir(texto_cifrado, lista_ordenada, clave_ant= None):
    texto_descifrado = {}
    clave = {} # guardamos qué letra representa cual, por ejemplo, la a es la b al descifrar
    # queda algo como {'a': 'e', 'h': 'a', 'l': 'o', 'o':
    if clave_ant == None:
        for i, letter in enumerate(lista_ordenada):
            clave[letter] = frecuencias[i]
    else:
        clave = clave_ant
    texto_final = "" 
    for char in texto_cifrado: # iteramos sobre cada caracter del input
        char = char.lower()
        if char not in frecuencias: # si el caracter no es una letra, lo añadimos al output y saltamos
            texto_final += char
            continue
        texto_final += clave[char]
    return texto_final, clave

def descifrar_simple_bucle(texto):
    diccionario_frec = contar_frecuencias(texto)
    lista_ordenada = diccionario_a_lista_ordenada(diccionario_frec)
    texto_final, clave = sustituir(texto, lista_ordenada)
    



    while True:
        print("RESULTADO")
        print(texto_final)

        print("ESCRIBE EXIT PARA SALIR ")
        letra_1 = input("Qué letra quieres cambiar?")

        letra_1 = letra_1.lower()
        if letra_1.lower() == "exit":
            break
        else:            
            letra_2 = input("Qué letra quieres que se convierta?")
            letra_2 = letra_2.lower()

        # El cambio es, lo que creo que apunta a la letra_1, debe apuntar a la letra_2
        # Guardar lo que actualmente tiene letra_1

        letra_que_apunta_a_letra1 = None
        letra_que_apunta_a_letra2 = None

        for k, v in clave.items():
            if v == letra_1:
                letra_que_apunta_a_letra1 = k
            if v == letra_2:
                letra_que_apunta_a_letra2 = k

        # Hacer el intercambio, 
        clave[letra_que_apunta_a_letra1] = letra_2  # Lo que apuntaba a letra_1 ahora apunta a letra_2
        clave[letra_que_apunta_a_letra2] = letra_1  # Lo que apuntaba a letra_2 ahora apunta a letra_1

        texto_final, clave = sustituir(texto, lista_ordenada, clave)
        print(clave)
    return texto_final

if __name__ == "__main__":
    print(descifrar_simple_bucle(texto_entrada))

