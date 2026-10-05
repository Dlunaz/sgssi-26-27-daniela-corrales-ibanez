# Laboratorio: Cifrado asimétrico

## Requisitos previos

- Máquina GNU/Linux: portátil, máquina virtual, o PC laboratorio (Entrar con credencial LDAP).
- Editor de código. En Visual Studio Code, pulsando ctrl+mayus+v renderiza este archivo de manera amigable (Sobre todo para imágenes).
- Herramientas necesarias: OpenSSL (`sudo apt install openssl`), gpg (`sudo apt install gpg`).
- Repositorio GitHub de asignatura: puedes subir los programas desarrollados en el laboratorio.

## Generar claves GPG

[GnuPG (GPG)](https://gnupg.org/) es un programa libre que nos permite cifrar, descifrar y firmar información cumpliendo el estándar [OpenPGP](https://www.openpgp.org/) y así asegurar nuestras comunicaciones. GPG ofrece muchas posibilidades. Es conveniente familiarizarse con ellas:

```bash
gpg --help
```

Para trabajar con GPG, lo primero es generar un par de claves (Pública y privada):

```bash
gpg --generate-key
```

Es muy importante proveer una dirección de email válida. La frase clave es opcional y sirve para proteger el acceso al llavero de claves privadas. En PGP, el llavero es el almacén donde se almacenan las claves con las que se va a trabajar. Existe un llavero de claves privadas, y otro llavero de claves públicas. Es aconsejable proteger el llavero con una frase clave.

Usando el comando `gpg --full-generate-key` se puede especificar qué longitud de clave deseáis usar, y qué algoritmo queréis usar para su creación. GnuPG soporta RSA, DSA y ElGamal. Para la creación del par de claves se usa una medida denominada entropía, que simboliza la cantidad de aleatoriedad o desorden que tiene la clave. A mayor entropía, mayor aleatoriedad y por lo tanto más complicado de realizar un criptoanálisis. En la generación de claves la entropía se obtiene en base a datos de la máquina como el estado de la CPU, la fecha, el número de ventanas abiertas, etc. Así que mientras se genera la clave es aconsejable navegar, abrir ventanas, teclear cosas, etc. para generar una entropía lo mayor posible.

Una vez terminada la generación de las claves se da la posibilidad de crear un certificado de revocación de las claves. El certificado de revocación sirve para indicar que tu clave ya no es válida porque la has perdido, te la han robado, etc. Cread el certificado de revocación y guardadlo.

Una vez creadas las claves, para verlas:

```bash
gpg --list-keys
```

> ¿Qué quiere decir `[ultimate]`?

Es importante que la clave pública esté accesible. Se puede publicar en una página [web personal](https://mikel-egana-aranguren.github.io/contact/), se puede enviar adjunta en un email, o se puede publicar en servidores específicos como **keys.openpgp.org** (Ver más adelante).

Para enviar archivos que han sido cifrados en la línea de comandos mediante GPG simplemente basta con adjuntarlos en el email.

- Cifrad este archivo y enviároslo entre vosotros de forma que consigáis los principios de **Confidencialidad**, **Integridad**, **Autenticidad** y **No Repudio**.

> Razonad qué habéis tenido que hacer para conseguir cada uno de ellos.

## Confianza sobre las claves GPG

Como habéis podido comprobar, es muy fácil crear un par de claves y poner cualquier nombre. No se realiza ningún tipo de comprobación. Por lo que si recibimos un archivo firmado y/o cifrado por una persona, no podemos estar seguros de que realmente sea esa persona a no ser que tengamos alguna manera de preguntarle si esa es realmente su clave. Sin embargo, existen mecanismos para que podamos confiar en las claves de una persona aun sin necesidad de conocerla o haber hablado previamente con ella para comprobar si esa es su clave.

- En cada grupo se designará a uno de los estudiantes como “de confianza”, es decir el profesor tendrá confianza plena en esa persona. Ese estudiante enviará su clave pública al profesor. El grupo tendrá que conseguir que al enviar las claves públicas de los otros estudiantes al profesor aparezcan como de confianza (`[full]`) en el **anillo de claves del ordenador del profesor**.

> Razonad qué habéis tenido que hacer para conseguirlo.

## Anillos públicos de claves GPG

Lo más sencillo para publicar y buscar claves es usar un servicio como [Keys OpenPGP](https://keys.openpgp.org/). Para usarlo hay que añadir la siguiente linea al archivo `/home/{usuario}/.gnupg/gpg.conf`:

```bash
keyserver hkps://keys.openpgp.org
```

- Configura GPG para que funcione con **keys.openpgp.org** desde la terminal.
- Sube tu clave al servidor usando GPG en la terminal.
- Busca las claves de los otros estudiantes y la del profesor usando GPG en la terminal.
- Recrea el ejercicio de la sección anterior, **Confianza sobre las claves**, pero esta vez usa el servidor de claves a través de la terminal en vez de enviar las claves al profesor (Notifica al profesor para que busque las claves de confianza).

## Anillo de claves GPG de la clase SGSSI

Vamos a recrear el anillo de claves de la sección anterior, pero sólo con las claves de los estudiantes de clase y usando eGela. Para ello, el profesor definirá una cadena de confianza designando a ciertos estudiantes, y el resto de estudiantes subirán sus claves públicas asegurando la confianza de manera transitiva (Empezando en los estudiantes de confianza). El profesor comprobará la confianza de la cadena importando todas las claves, pero dándole confianza sólo a la primera (Al importarlas, todas deberían aparecer como de confianza en el ordenador del profesor).

## Firmas GPG

En la página web de los desarrolladores de [Enigmail](http://www.enigmail.net/download) se pueden descargar dos ficheros, la extensión para Thunderbird (`.xpi`) y otro fichero llamado “GPG Signature”.

> ¿Para qué sirve ese segundo fichero?¿Cómo se usa?

En GitHub existe la opción de firmar commits mediante GPG, para aumentar la seguridad y trazabilidad de dichos commits. El profesor ha firmado el commit con el Hash `6176ac9c479797c698b153c7750fa3e4421f445d` de la rama `develop` del repositorio de apuntes de la asignatura [EHU-SGSSI-01](https://github.com/mikel-egana-aranguren/EHU-SGSSI-01), con la clave privada generada a la vez que la siguiente clave pública (`mikel.egana.aranguren@gmail.com`):

```
-----BEGIN PGP PUBLIC KEY BLOCK-----
mDMEaMlpKBYJKwYBBAHaRw8BAQdA9BUe340yfVTGvu5htYNgujz5pGtx6GfIRP8h
CALZ+im0OE1pa2VsIEVnYcOxYSBBcmFuZ3VyZW4gPG1pa2VsLmVnYW5hLmFyYW5n
dXJlbkBnbWFpbC5jb20+iJkEExYKAEEWIQQYFaxDxNCAFSKkZypj4GjUA79N7wUC
aMlpKAIbAwUJBaOagAULCQgHAgIiAgYVCgkICwIEFgIDAQIeBwIXgAAKCRBj4GjU
A79N75+fAQD75ya26vOiPsP18zWcclNbEqbt4f/260ycrRYsAoeNAgD/Wsa8GlSP
DnG2X1SC2GY8/X0rfcavzE3Ib4gJzoOkSQe4OARoyWkoEgorBgEEAZdVAQUBAQdA
4zlL3S3rbtPiUuPBscGteaVhYCRjmVuph+0KE/FUQUoDAQgHiH4EGBYKACYWIQQY
FaxDxNCAFSKkZypj4GjUA79N7wUCaMlpKAIbDAUJBaOagAAKCRBj4GjUA79N71q2
AP0W791v7y2QBsaxNuWlZqW/CNHamHJz1hr7tCWs/Jfa2wD9Gh1rszwCy6zXCNOv
hqLrPTy2euh/O45VyZSigvW+QgM=
=aYb8
-----END PGP PUBLIC KEY BLOCK-----
```

El commit aparece como verificado en GitHub (“Verified”). ¿Esto qué quiere decir?

![GitHub Commit](github_commit.png)

> Verifica ese mismo commit en tu ordenador local. ¿Qué pasos tienes que seguir?

> Usa tus claves GPG para firmar un commit en el repositorio GitHub de la asignatura, de modo que aparezca como “Verified” al verlo en GitHub. Verifica los commits firmados por otros estudiantes.

## Otras funcionalidades GPG

Es importante que seáis capaces de usar vuestras claves en otros equipos, sobre todo de cara al examen.

> ¿Cómo se exporta una clave GPG para poder usarla en otro equipo?

Puede pasar que una clave quede comprometida.

> ¿Cómo revocarías tu clave?

Aunque su función principal es el cifrado asimétrico, GPG también se puede usar para cifrado simétrico.

> ¿Como cifrarías este documento de manera simétrica, y qué pasos seguirías para que el receptor lo descifre?

## RSA

Genera un par de claves RSA con OpenSSL:

```bash
openssl genpkey -algorithm RSA -out clave.pem
```
El archivo `clave.pem` tiene ambas claves, para poder ver su estructura interna: 

```bash
openssl rsa -text -in clave.pem
```

Para extraer la clave pública:

```bash
openssl rsa -pubout -in clave.pem -out clave_publica.pem
```

Encripta un mensaje con la clave publica mediante `openssl pkeyutl -encrypt`. Descífralo con la clave privada y comprueba que el mensaje coincide. 

> RSA sirve para archivos pequeños. ¿Cómo implementarías un cifrado híbrido, usando AES para cifrar el archivo de manera simétrica y RSA para cifrar la clave AES? 

### Cifrado híbrido paso a paso

En este ejemplo se cifra `archivo.txt` con una clave AES aleatoria. Después se cifra
esa clave AES con RSA-OAEP usando la clave pública del receptor. El IV de AES no es
secreto, por lo que se envía junto al archivo cifrado. Además, se calcula un HMAC
para detectar modificaciones del archivo cifrado o del IV.

Todos los comandos siguientes se ejecutan desde el mismo directorio:

1. Crear un archivo de prueba (en un caso real se usaría el archivo que se quiere
   enviar):

   ```bash
   printf 'Documento confidencial\n' > archivo.txt
   ```

2. Generar el par de claves RSA del receptor y extraer su clave pública:

   ```bash
   openssl genpkey -algorithm RSA \
     -pkeyopt rsa_keygen_bits:3072 \
     -out clave_privada.pem

   openssl pkey -in clave_privada.pem \
     -pubout -out clave_publica.pem
   ```

   `clave_privada.pem` debe permanecer únicamente en el equipo del receptor.
   El emisor sólo necesita `clave_publica.pem`.

3. Generar una clave AES de 256 bits y un IV de 128 bits:

   ```bash
   openssl rand -hex 32 > clave_aes.hex
   openssl rand -hex 16 > iv.hex
   ```

4. Cifrar el archivo con AES-256-CBC:

   ```bash
   openssl enc -aes-256-cbc \
     -in archivo.txt \
     -out archivo.txt.aes \
     -K "$(cat clave_aes.hex)" \
     -iv "$(cat iv.hex)"
   ```

5. Cifrar la clave AES con RSA-OAEP y SHA-256:

   ```bash
   openssl pkeyutl -encrypt \
     -pubin -inkey clave_publica.pem \
     -in clave_aes.hex \
     -out clave_aes.hex.rsa \
     -pkeyopt rsa_padding_mode:oaep \
     -pkeyopt rsa_oaep_md:sha256 \
     -pkeyopt rsa_mgf1_md:sha256
   ```

6. Calcular un HMAC sobre el IV y el archivo cifrado. Se utiliza la misma clave
   AES sólo para simplificar el laboratorio:

   ```bash
   cat iv.hex archivo.txt.aes > datos_para_hmac.bin

   openssl dgst -sha256 -mac HMAC \
     -macopt "hexkey:$(cat clave_aes.hex)" \
     -binary datos_para_hmac.bin > datos_para_hmac.sha256
   ```

7. El emisor entrega al receptor únicamente estos archivos:

   ```text
   archivo.txt.aes
   clave_aes.hex.rsa
   iv.hex
   datos_para_hmac.sha256
   ```

   `clave_privada.pem`, `clave_aes.hex` y `datos_para_hmac.bin` no se deben
   enviar. La clave privada RSA se entrega al receptor por un canal seguro.

8. En el equipo del receptor, descifrar la clave AES con la clave privada RSA:

   ```bash
   openssl pkeyutl -decrypt \
     -inkey clave_privada.pem \
     -in clave_aes.hex.rsa \
     -out clave_aes_recuperada.hex \
     -pkeyopt rsa_padding_mode:oaep \
     -pkeyopt rsa_oaep_md:sha256 \
     -pkeyopt rsa_mgf1_md:sha256
   ```

9. Verificar el HMAC antes de descifrar el archivo:

   ```bash
   cat iv.hex archivo.txt.aes > datos_para_hmac_recibidos.bin

   openssl dgst -sha256 -mac HMAC \
     -macopt "hexkey:$(cat clave_aes_recuperada.hex)" \
     -binary datos_para_hmac_recibidos.bin > datos_para_hmac_calculado.sha256

   cmp -s datos_para_hmac.sha256 datos_para_hmac_calculado.sha256 \
     && echo "HMAC correcto: los datos no han sido modificados" \
     || { echo "HMAC incorrecto: no se descifra"; exit 1; }
   ```

10. Descifrar el archivo con AES:

    ```bash
    openssl enc -d -aes-256-cbc \
      -in archivo.txt.aes \
      -out archivo_descifrado.txt \
      -K "$(cat clave_aes_recuperada.hex)" \
      -iv "$(cat iv.hex)"
    ```

11. Comprobar que el archivo original y el descifrado son iguales:

    ```bash
    cmp -s archivo.txt archivo_descifrado.txt \
      && echo "Descifrado correcto" \
      || echo "Los archivos son diferentes"
    ```

El resultado es híbrido porque AES cifra eficientemente cualquier tamaño de
archivo, mientras que RSA sólo cifra la pequeña clave AES. RSA-OAEP protege la
confidencialidad de esa clave y el HMAC aporta integridad. En un sistema nuevo se
debería preferir un formato autenticado como AES-GCM o una herramienta como
OpenPGP/CMS; `openssl enc` no proporciona autenticación AEAD en todas las
versiones.
