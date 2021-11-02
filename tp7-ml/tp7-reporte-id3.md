# Reporte id3

### Árbol de decisión obtenido para el dataset tennis.csv:

![imagen](https://user-images.githubusercontent.com/69587750/139784525-beef108b-5d2e-4bb8-8aa3-d4cc915c90f9.png)

### Árboles de decisión para datos de tipo real

A la hora de tratar con árboles con datos de tipo real, podemos tener 2 casos:

1. Que uno o más atributos de entrada sean de tipo real.
2. Que el atributo de salida sea de tipo real.

Dado que un dato real puede tomar infinitos valores en un intervalo dado, cuando tratamos con datos de entrada reales no se puede crear una rama en el árbol para cada posible valor del dato. 
Por este motivo es que los árboles de decision para datos de tipo de real tienen un mayor nivel de complejidad, ya que se debe clasificar a los datos por intervalo (al que pertenecen) en vez de por su valor en específico (pudiendo ser intervalos cerrados o abiertos indiferentemente). 
La complejidad radica en que el algoritmo debe tener un criterio que maximice la ganancia al dividir los intervalos, garantizando la máxima pertenencia de cada dato al grupo asignado.

En el segundo caso, cuando debemos predecir el valor de un atributo de tipo real, un algoritmo de clasificación ya no es lo indicado, 
sino que se implementa un árbol de regresión, donde en los nodos terminales del árbol no se encuentra un valor específico del dato como predicción, 
sino una función de regresión lineal en base a algunos atributos para predecir dinámicamente el valor del atributo de salida.
