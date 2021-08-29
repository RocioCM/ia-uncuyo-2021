# Reporte de Rendimiento 

Mediciones realizadas sobre escenarios de dimensión 100x100 con una densidad de obstáculos de 0.2 cuya distribución fue generada de forma completamente aleatoria en cada iteración, 
sobre una muestra de 30 iteraciones por algoritmo. 
Sumado a que las posiciones de salida y objetivo del agente también fueron generadas de forma aleatoria y distinta en cada iteración. 

## Rendimiento del Agente usando el algoritmo BFS
29 de 30 agentes tuvieron éxito en llegar al destino.

**Media:**  3882.3 estados

**Desviación Estándar:**  2745.5 estados

## Rendimiento del Agente usando el algoritmo Búsqueda Uniforme
30 de 30 agentes tuvieron éxito en llegar al destino.

**Media:**  4210.0 estados

**Desviación Estándar:**  2527.2 estados


## Rendimiento del Agente usando el algoritmo DFS
28 de 30 agentes tuvieron éxito en llegar al destino.

**Media:**  3672.3 estados

**Desviación Estándar:**  2539.3 estados

## Gráfico comparativo

![imagen](https://user-images.githubusercontent.com/69587750/130880484-f6749c29-f4d2-42a6-b912-21737d40e3ae.png)

## Conclusión

Considerando los resultados promedio de rendimiento de cada algoritmo, se podría pensar que el "algoritmo más eficiente" es búsqueda en profundidad, pero eso en realidad depende del criterio. Si nuestro criterio fuera recorrer la menor cantidad de casillas (estados) para llegar al destino, entonces estaríamos en lo correcto. Pero dado que nuestro objetivo es "encontrar el camino óptimo", es decir, el más corto, el algoritmo eficaz para este fin sería búsqueda en amplitud o búsqueda uniforme. 

Lo interesante del caso es que como para esta implementación se decidió que el costo de desplazarse entre dos casillas cualesquiera fuera constante (es decir, nuestro grafo no es ponderado), el algoritmo de búsqueda uniforme encuentra siempre el camino más corto, al igual que la búsqueda en amplitud, ya que termina barriendo el terreno en un orden equivalente al del algoritmo en amplitud. Si el planteo del problema incluyera que el costo de desplazarse entre dos casillas cualesquiera es variable, entonces el algoritmo eficaz para este caso sería únicamente búsqueda uniforme, ya que se asegura de a cada paso elegir el camino más corto posible, no solo teniendo en cuenta la cantidad de casillas del camino sino también los costos de desplazarse entre ellas.
