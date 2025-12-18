# 1. Cargar librería gráfica
library(ggplot2)

# 2. Crear datos sintéticos (Data Frame)
set.seed(42)
df <- data.frame(
  categoria = c("A", "B", "C", "D"),
  valor = c(10, 23, 15, 30)
)

# 3. Imprimir resumen (Verificar consola)
print("--- RESUMEN DE DATOS ---")
print(summary(df))

# 4. Generar Gráfico (Verificar Panel de Plots)
ggplot(df, aes(x=categoria, y=valor, fill=categoria)) +
  geom_col() +
  theme_minimal() +
  ggtitle("Prueba de R en WSL + Positron: ÉXITO")