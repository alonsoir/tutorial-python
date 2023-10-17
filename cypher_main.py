import base64
import gc
import getpass
from random import randint

from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad, unpad  # Agregamos el módulo de relleno PKCS7


def difuminar_contraseña(password):
    # Sobreescribimos la variable clave a un valor aleatorio
    password = "".join([chr(randint(0, 255)) for i in range(len(password))])

    # Liberamos la memoria de la variable clave
    gc.collect()


def decode_base64_python_code(encoded_code):
    """Decodifica un código Python codificado en base64.

    Args:
      encoded_code: El código Python codificado en base64.

    Returns:
      El código Python decodificado.
    """

    decoded_code = base64.b64decode(encoded_code)
    return decoded_code.decode("utf-8")


def execute_python_code(python_code):
    """Ejecuta un código Python.

    Args:
      python_code: El código Python a ejecutar.
    """

    exec(python_code)


# Función para descifrar el código fuente
def descifrar(clave, codigo_cifrado):
    descifrador = AES.new(clave, AES.MODE_ECB)
    codigo_fuente = descifrador.decrypt(codigo_cifrado)
    # Removemos el relleno PKCS7
    codigo_fuente = unpad(codigo_fuente, AES.block_size)
    return codigo_fuente.decode("utf-8")


# Solicitamos la contraseña al usuario
contraseña = getpass.getpass("Introduce la contraseña (no aparecerá en pantalla): ")

# Generamos una clave secreta de 128 bits a partir de la contraseña
clave = contraseña.encode("utf-8")
clave = clave + b"\x00" * (16 - len(clave))  # Rellena la clave si es necesario

# Ciframos el código fuente del programa "Hola mundo"
archivo_fuente = open("main.py", "rb")
codigo_fuente = archivo_fuente.read()
archivo_fuente.close()

# Aplicamos el relleno PKCS7
codigo_fuente = pad(codigo_fuente, AES.block_size)

cifrador = AES.new(clave, AES.MODE_ECB)
codigo_cifrado = cifrador.encrypt(codigo_fuente)

# Guardamos el código cifrado en un archivo
archivo_cifrado = open("main.enc", "wb")
archivo_cifrado.write(codigo_cifrado)
archivo_cifrado.close()

# Desciframos el código fuente
codigo_descifrado = descifrar(clave, codigo_cifrado)

# Sobreescribimos la variable clave a None para liberar la memoria.
# Ponerla a None es poca cosa, por lo que trato de sobreescribir las zonas de memoria asignadas previamente.
difuminar_contraseña(clave)

# Ejecutamos el programa "main.py"
execute_python_code(codigo_descifrado)

# Codificamos el código en base64
codigo_base64 = base64.b64encode(codigo_descifrado.encode())

encoded_code = codigo_base64.decode()

# Decodificamos el código Python codificado en base64.
python_code = decode_base64_python_code(encoded_code)

# Ejecutamos el código Python decodificado.
execute_python_code(python_code)
