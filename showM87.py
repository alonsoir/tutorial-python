import ehtim as eht
import matplotlib.pyplot as plt

# Descargar los datos
data = eht.download_data(event="m87")

# Limpiar los datos
data = eht.denoise(data, method="richardson-lucy")

# Procesar los datos
data = eht.normalize(data)

# Modelar la imagen
image = eht.image(data)

# Visualizar la imagen
plt.imshow(image)
plt.show()
