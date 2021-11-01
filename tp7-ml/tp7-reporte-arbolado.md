# Reporte Arbolado Público

### Preprocesamiento

Como primer paso, se tomó una muestra del total del dataset con una cantidad equivalente de árboles clasificados como peligrosos y árboles no peligrosos. Luego de esto, se procedió a eliminar las variables irrelevantes o que no se usarían en el entrenamiento. Estas fueron: ultima_modificacion, circ_tronco_cm, nombre_seccion, area_seccion, long y lat.

### Entrenamiento

Luego de esto, se pasó a la etapa de entrenamiento. Para la fórmula se eligieron las variables de interés especie, altura, diametro_tronco y seccion. Luego de esto, se procedió a entrenar propiamente el modelo mediante el algoritmo de árbol de decisión provisto por la librería rpart.

### Resultados

Dado que el algoritmo incluye un factor aleatorio (la muestra tomada del total del dataset), el desempeño del modelo varía levemente entre iteraciones. Tras probar modificando distintos aspectos de la fórmula, se obtuvieron varias predicciones sobre el dataset de prueba. Todos estos resultados se mantuvieron aproximadamente entre el 66% y el 68% de precisión, pero fue recién el décimo modelo subido el que logró pasar la barrera de 0.68.
