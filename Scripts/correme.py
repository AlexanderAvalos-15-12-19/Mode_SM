#pip install matplotlib pandas

import pandas as pd
import matplotlib.pyplot as plt

def plot_xvg(file_path):
    # Leer el archivo .xvg, ignorando las líneas que comienzan con '@', '#', y '&', que son meta-datos
    with open(file_path) as file:
        lines = [line for line in file if not line.startswith(('@', '#', '&'))]
    
    # Convertir las líneas filtradas en un DataFrame
    data = pd.DataFrame([line.split() for line in lines]).astype(float)

    # Asumiendo que la primera columna es el tiempo y la segunda es el valor del RMSD
    time = data[0]
    rmsd = data[1]

    # Crear el gráfico
    plt.figure(figsize=(10, 6))
    plt.plot(time, rmsd)
    plt.title('Root Mean Square Deviation (RMSD)')
    plt.xlabel('Time (ns)')
    plt.ylabel('RMSD (nm)')
    plt.grid(True)
    plt.show()

# Reemplaza 'tu_archivo.xvg' con la ruta de tu archivo .xvg
plot_xvg('rmsd.xvg')
