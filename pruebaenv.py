import geopandas as gpd
import rasterio
import rioxarray
import sklearn
from sklearn.ensemble import RandomForestClassifier

print("--- REPORTE DE ESTADO ---")
print(f"✅ GeoPandas: {gpd.__version__}")
print(f"✅ Rasterio:  {rasterio.__version__}")
print(f"✅ Rioxarray: {rioxarray.__version__}")
print(f"✅ Sklearn:   {sklearn.__version__}")
print("✅ Random Forest: Listo para entrenar")