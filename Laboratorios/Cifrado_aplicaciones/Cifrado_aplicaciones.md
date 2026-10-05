# Laboratorio: Aplicaciones cifrado

## Requisitos previos

- Máquina GNU/Linux: portátil, máquina virtual, o PC laboratorio (Entrar con credencial LDAP).
- Editor de código. En Visual Studio Code, pulsando ctrl+mayus+v renderiza este archivo de manera amigable (Sobre todo para imágenes).
- Herramientas necesarias: OpenSSL (`sudo apt install openssl`), Apache (`sudo apt-get install apache2`).
- Repositorio GitHub de asignatura: puedes subir los programas desarrollados en el laboratorio.

## ¿Qué es Apache?

Apache HTTP Server es un servidor web de código abierto. Se encarga de recibir
las peticiones de los navegadores y devolver páginas web, archivos u otros
recursos mediante HTTP. En este laboratorio se utiliza Apache para publicar el
sitio web y configurarlo posteriormente para aceptar conexiones HTTPS.

## HTTP y HTTPS

**HTTP** es un protocolo de comunicación sin cifrado. La información viaja en
texto claro, por lo que un atacante podría interceptarla o modificarla.

**HTTPS** es HTTP protegido mediante TLS. Cifra la comunicación, ayuda a
garantizar que los datos no se modifican durante el envío y permite comprobar la
identidad del servidor mediante un certificado digital. Por eso HTTPS es la
opción segura para acceder a un sitio web, especialmente cuando se transmiten
contraseñas o datos personales.

## Instalación de Apache

Para crear un sitio web seguro primero hay que instalar un servidor web en nuestro servidor de Google Cloud, en este caso Apache. Para hacerlo, abre una conexión SSH al servidor y ejecuta:

```bash
sudo apt-get install apache2
```

Si visitas la IP de la máquina con el navegador, por ejemplo `http://35.216.188.54`, debería aparecer la página por defecto de Apache. El navegador mostrará que la conexión no es segura, por ejemplo, mediante el mensaje “Not secure”.

![Apache](apache.png)

## Creación de un sitio seguro

Si queremos que las conexiones al sitio web que acabamos de crear sean seguras, usando el protocolo HTTPS en vez de HTTP, debemos usar un certificado de servidor autofirmado y redirigir el tráfico del puerto 80 al puerto 443.

Para ello, en vez de usar la configuración por defecto de Apache, crea un `VirtualHost` que sólo contenga una página web llamada `index.html`, con el siguiente contenido:

```html
<h1>Conexión SSL</h1>
```

Genera un certificado autofirmado con OpenSSL y crea una configuración nueva de Apache con la redirección del puerto 80 al puerto 443.

Al visitar la web mediante HTTPS, aunque tenga un certificado, seguirá apareciendo un mensaje de error. Exporta el certificado y añádelo a tu navegador para que deje de mostrar ese aviso.
