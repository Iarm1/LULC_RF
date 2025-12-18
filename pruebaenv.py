import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. Crear datos sintéticos
np.random.seed(42)
df = pd.DataFrame({
    'A': np.random.randn(100),
    'B': np.random.randn(100) + 2
})

# 2. Operación vectorial (Prueba de Numpy/Pandas)
print("--- RESUMEN ESTADÍSTICO ---")
print(df.describe())

# 3. Generar Gráfico (Prueba de integración visual)
plt.figure(figsize=(10, 6))
plt.scatter(df['A'], df['B'], c='crimson', alpha=0.6)
plt.title("Prueba de Entorno WSL + Positron: OK")
plt.xlabel("Variable A")
plt.ylabel("Variable B")
plt.grid(True)
plt.show()