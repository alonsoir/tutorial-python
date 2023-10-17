import base64
import os
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad, unpad
import getpass

# Solicitamos la contraseña al usuario de manera segura
contraseña = getpass.getpass(
    "Introduce la contraseña (no aparecerá en pantalla): ", stream=None
)

# Generamos una clave secreta de 128 bits a partir de la contraseña
clave = contraseña.encode("utf-8")
clave = clave + b"\x00" * (16 - len(clave))  # Rellena la clave si es necesario

# Ciframos el código fuente del programa "Hola mundo"
archivo_fuente = open("main.py", "rb")
codigo_fuente = archivo_fuente.read()
archivo_fuente.close()

# Aplicamos el relleno PKCS7 al cifrar
codigo_cifrado = pad(codigo_fuente, AES.block_size)

# Guardamos el código cifrado en un archivo temporal
archivo_temporal = "temp.enc"
archivo_cifrado = open(archivo_temporal, "wb")
archivo_cifrado.write(codigo_cifrado)
archivo_cifrado.close()

# Sobrescribimos la variable clave en la memoria
clave = b"\x00" * len(clave)


# Función para descifrar el código fuente
def descifrar(clave, codigo_cifrado):
    descifrador = AES.new(clave, AES.MODE_ECB)
    codigo_descifrado = descifrador.decrypt(codigo_cifrado)
    codigo_descifrado = unpad(codigo_descifrado, AES.block_size, pkcs7=True)
    return codigo_descifrado


try:
    with open(archivo_temporal, "rb") as archivo_cifrado:
        codigo_cifrado = archivo_cifrado.read()
    codigo_descifrado = descifrar(clave, codigo_cifrado)

    # Borramos el archivo cifrado una vez ejecutado
    os.remove(archivo_temporal)

    # Ejecutamos el programa descifrado
    exec(codigo_descifrado.decode("utf-8"))

    # Codificamos el código en base64
    codigo_base64 = base64.b64encode(codigo_descifrado)

    # Imprimimos el código en base64
    print(codigo_base64.decode())

except Exception as e:
    print("Error al ejecutar el programa cifrado:", e)
