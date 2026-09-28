#COMO FUNCIONAN LAS FRECUENCIAS
# si en castellano la E aparece el 16,78% de las veces, y sustituyo cada E por una X, 
# entonces en el texto cifrado la X aparecerá también aproximadamente el 16,78% de las veces.

#PASOS
# 1. Contamos cuNtas veces aparece cada letra en el texto cifrado.
# 2. Calculamos el porcentaje de apariciones de cada letra en el texto cifrado.
# 3. Comparamos los porcentajes de apariciones de cada letra en el texto cifrado y vamos emparejando a lo bruto.
# 4. Lo hacemos interactivo para que el usuario pueda ir cambiando las letras y viendo el resultado en tiempo real.

# collections es una libreria que contiene contadores y otras estructuras de datos.
# la vamos a usar para contar cuantas veces aparece cada letra en el texto cifrado.
from collections import Counter

CIFRADO = """RIJ AZKKZHC PIKCE XT ACKCUXJHX SZX, E NZ PEJXKE, PXGIK XFDKXNEQE RIPI
RIPQEHCK ET OENRCNPI AXNAX ZJ RKCHXKCI AX CJAXDXJAXJRCE AX RTENX, E
ACOXKXJRCE AXT RITEQIKERCIJCNPI OKXJHXDIDZTCNHE AX TE ACKXRRCIJ EJEKSZCNHE.
AZKKZHC OZX ZJ OERHIK AX DKCPXK IKAXJ XJ XT DEDXT AX TE RTENX IQKXKE XJ
REHETZJVE XJ GZTCI AX 1936. DXKI AZKKZHC, RIPI IRZKKX RIJ TEN
DXKNIJETCAEAXN XJ TE MCNHIKCE, JI REVI AXT RCXTI. DXKNIJCOCREQE TE
HKEACRCIJ KXVITZRCIJEKCE AX TE RTENX IQKXKE. NZ XJIKPX DIDZTEKCAEA
XJHKX TE RTENX HKEQEGEAIKE, KXOTXGEAE XJ XT XJHCXKKI PZTHCHZACJEKCI XJ
QEKRXTIJE XT 22 AX JIVCXPQKX AX 1936, PZXNHKE XNE CAXJHCOCRERCIJ. NZ
PZXKHX OZX NCJ AZAE ZJ UITDX IQGXHCVI ET DKIRXNI KXVITZRCIJEKCI XJ
PEKRME. NCJ AZKKZHC SZXAI PEN TCQKX XT REPCJI DEKE SZX XT XNHETCJCNPI,
RIJ TE RIPDTCRCAEA AXT UIQCXKJI AXT OKXJHX DIDZTEK V AX TE ACKXRRCIJ
EJEKSZCNHE, HXKPCJEKE XJ PEVI AX 1937 TE HEKXE AX TCSZCAEK TE
KXVITZRCIJ, AXNPIKETCLEJAI E TE RTENX IQKXKE V OERCTCHEJAI RIJ XTTI XT
DINHXKCIK HKCZJOI OKEJSZCNHE."""

# Frecuencias del castellano (en %), de la tabla del enunciado.
FRECUENCIAS_ES = {
    "E": 16.78, "A": 11.96, "O": 8.69, "L": 8.37, "S": 7.88, "N": 7.01,
    "D": 6.87, "R": 4.94, "U": 4.80, "I": 4.15, "T": 3.31, "C": 2.92,
    "P": 2.776, "M": 2.12, "Y": 1.54, "Q": 1.53, "B": 0.92, "H": 0.89,
    "G": 0.73, "F": 0.52, "V": 0.39, "J": 0.30, "Ñ": 0.29, "Z": 0.15,
    "X": 0.06, "K": 0.00, "W": 0.00,
}

ALFABETO = list("ABCDEFGHIJKLMNÑOPQRSTUVWXYZ")

#Devuelve el texto en mayúsculas, quedándonos solo con letras.
def solo_letras(texto):
    #upper: convierte el texto a mayúsculas.
    texto = texto.upper()
    # join: une los elementos de un iterable (en este caso, una lista de caracteres) en una cadena de texto.
    # isalpha: devuelve True si el caracter es una letra, False en caso contrario.
    return "".join(c for c in texto if c.isalpha())

# Cuenta letras y las devuelve como porcentaje sobre el total.
def frecuencias(texto):
    letras = solo_letras(texto)
    total = len(letras)
    # Counter: cuenta cuantas veces aparece cada letra, y devuelve un diccionario {letra: cantidad}.
    contador = Counter(letras)
    # Devolvemos un diccionario {letra: porcentaje} y el total de letras.
    return {letra: (n / total) * 100 for letra, n in contador.items()}, total

# Vamos a mostrar las frecuencias del cifrado y del castellano, para poder emparejarlas visualmente.
def mostrar_tabla_frecuencias(frec_cifrado):
    # Ordenamos las letras por frecuencia, de mayor a menor, para poder emparejarlas visualmente.
    ranking_cifrado = sorted(frec_cifrado.items(), key=lambda kv: -kv[1])
    # Ordenamos las letras del castellano por frecuencia, de mayor a menor, para poder emparejarlas visualmente.
    ranking_es = sorted(FRECUENCIAS_ES.items(), key=lambda kv: -kv[1])
    # Imprimimos la tabla de frecuencias, con el ranking del cifrado a la izquierda y el ranking del castellano a la derecha.
    print(f"\n{'CIFRADO':<20}{'CASTELLANO (esperado)':<25}")
    print("-" * 45)
    n = max(len(ranking_cifrado), len(ranking_es))
    for i in range(n):
        izq = f"{ranking_cifrado[i][0]}: {ranking_cifrado[i][1]:5.2f}%" if i < len(ranking_cifrado) else ""
        der = f"{ranking_es[i][0]}: {ranking_es[i][1]:5.2f}%" if i < len(ranking_es) else ""
        print(f"{izq:<20}{der:<25}")

# Descifra el texto usando la clave de sustitución proporcionada. Las letras que no estén en la clave se muestran como '_'.
# clave es un diccionario {letra_cifrada: letra_clara}.
def descifrar(texto, clave):
    resultado = []
    # recorremos cada caracter del texto, y si es una letra, la sustituimos por la letra correspondiente en la clave. Si no es una letra, la dejamos tal cual.
    for c in texto:
        # upper: convierte el caracter a mayúsculas.
        cu = c.upper()
        # isalpha: devuelve True si el caracter es una letra, False en caso contrario.
        if cu.isalpha():
            # get: devuelve el valor de la clave para la letra cifrada, o None si no está en la clave.
            plano = clave.get(cu)
            if plano:
                # Si la letra es minúscula, la devolvemos en minúscula, si es mayúscula, la devolvemos en mayúscula.
                resultado.append(plano.lower() if c.islower() else plano)
            else:
                resultado.append("_")
        else:
            # Si no es una letra, la dejamos tal cual.
            resultado.append(c)        
    return "".join(resultado)

# Trampa: le damos una clave (diccionario) inicial que empareja las letras más frecuentes del cifrado con las más frecuentes del castellano. 
# Esto no siempre es correcto, pero nos da un punto de partida para ir corrigiendo a mano.
def sugerencia_automatica(frec_cifrado):
    # Ordenamos 
    ranking_cifrado = [l for l, _ in sorted(frec_cifrado.items(), key=lambda kv: -kv[1])]
    ranking_es = [l for l, _ in sorted(FRECUENCIAS_ES.items(), key=lambda kv: -kv[1])]
    clave = {}
    # Emparejamos las letras más frecuentes del cifrado con las más frecuentes del castellano.
    for c_letra, p_letra in zip(ranking_cifrado, ranking_es):
        clave[c_letra] = p_letra
    return clave

# Fuerza bruta' acotada: para UNA letra cifrada, probamos las 27
# letras posibles del alfabeto español (evitando las ya usadas en la
# clave para otras letras) y mostramos cómo queda el texto con cada
# hipótesis, para elegir a ojo/con diccionario la que tenga sentido.
def fuerza_bruta_letra(texto, clave, letra_cifrada):
    # Creamos un conjunto de letras ya usadas en la clave, para no repetirlas.
    usadas = set(clave.values())
    print(f"\nProbando sustituciones para la letra cifrada '{letra_cifrada}':")
    for candidata in ALFABETO:
        if candidata in usadas:
            continue
        # Creamos una copia de la clave y añadimos la nueva sustitución.
        # dict(clave) crea una copia del diccionario clave, para no modificar el original.
        prueba = dict(clave)
        prueba[letra_cifrada] = candidata
        # Desciframos el texto con la clave de prueba y mostramos un fragmento del resultado.
        texto_probado = descifrar(texto, prueba)
        # Mostramos solo un fragmento para que sea legible
        fragmento = texto_probado[:120].replace("\n", " ")
        print(f"  {letra_cifrada} -> {candidata}: {fragmento}...")


# ------------------------------------------------------------------
# 4. Bucle interactivo
# ------------------------------------------------------------------

def imprimir_ayuda():
    print("""
Comandos disponibles:
  freq            Muestra la tabla de frecuencias (cifrado vs castellano)
  auto            Genera una clave inicial emparejando frecuencias
  ver             Muestra el texto descifrado con la clave actual
  clave           Muestra la clave de sustitución actual
  X=Y             Asigna: la letra cifrada X representa la letra clara Y
                  (ejemplo:  R=C   fija que la R cifrada es una C real)
  brute X         Fuerza bruta sobre una sola letra cifrada X: prueba
                  todas las letras candidatas y enseña el resultado
  reset           Borra la clave y empieza de nuevo
  ayuda           Muestra este mensaje
  salir           Termina el programa y muestra el resultado final
""")


def main():
    print("=== Descifrador de sustitución monoalfabética ===")
    frec_cifrado, total = frecuencias(CIFRADO)
    print(f"Total de letras analizadas en el criptograma: {total}")
    mostrar_tabla_frecuencias(frec_cifrado)

    clave = {}
    imprimir_ayuda()

    while True:
        try:
            entrada = input("\n> ").strip()
        except EOFError:
            break
        if not entrada:
            continue

        cmd = entrada.lower()

        if cmd in ("salir", "exit", "quit"):
            break
        elif cmd == "ayuda":
            imprimir_ayuda()
        elif cmd == "freq":
            mostrar_tabla_frecuencias(frec_cifrado)
        elif cmd == "reset":
            clave = {}
            print("Clave reiniciada.")
        elif cmd == "clave":
            if not clave:
                print("(clave vacía)")
            else:
                for k, v in sorted(clave.items()):
                    print(f"  {k} -> {v}")
        elif cmd == "auto":
            clave = sugerencia_automatica(frec_cifrado)
            print("Clave inicial generada por frecuencias:")
            for k, v in sorted(clave.items()):
                print(f"  {k} -> {v}")
            print("\nRecuerda: esta clave es solo un punto de partida y "
                  "normalmente hay que corregirla a mano con X=Y.")
        elif cmd == "ver":
            print(descifrar(CIFRADO, clave))
        elif cmd.startswith("brute "):
            letra = entrada.split()[1].upper()
            if letra not in ALFABETO:
                print("Letra no válida.")
                continue
            fuerza_bruta_letra(CIFRADO, clave, letra)
        elif "=" in entrada and len(entrada.split("=")) == 2:
            izq, der = entrada.split("=")
            izq, der = izq.strip().upper(), der.strip().upper()
            if len(izq) != 1 or len(der) != 1 or izq not in ALFABETO or der not in ALFABETO:
                print("Formato esperado: X=Y (una letra cifrada = una letra clara)")
                continue
            clave[izq] = der
            print(f"Asignado: {izq} -> {der}")
            print(descifrar(CIFRADO, clave)[:300].replace("\n", " ") + " ...")
        else:
            print("Comando no reconocido. Escribe 'ayuda' para ver las opciones.")

    print("\n=== Resultado final ===")
    print(descifrar(CIFRADO, clave))


if __name__ == "__main__":
    main()