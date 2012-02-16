import numpy as np
import matplotlib.pyplot as plt
"""Un ejemplo de cambiar las propiedades de las etiquetas de una gráfica en matplotlib
"""
# Primero, creamos una serie aleatoria
x = np.random.rand( 1000 ) # Por ejemplo!

plt.hist ( x, bins=20 ) # Histograma

# Cogemos el eje

ax = plt.gca()

# Ahora, vamos a rotar las etiquetas de las abscisas 45 grados, y ponerles una fuente de 14 puntos
plt.setp(ax.get_xticklabels(), rotation='vertical', fontsize=14)
# Para las etiquetas de las ordenadas, una particular y hortera mezcla de...
#
# 1. Fuente de 24 puntos
# 2. Color de fondo amarillo ('y')
# 3. Familia de fuentes "fantasy" (comis-sans)
# 4. Letra negrita

plt.setp(ax.get_yticklabels(), fontsize=24, backgroundcolor="y", family="fantasy", weight='heavy')

plt.show()
