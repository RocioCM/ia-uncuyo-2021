## Variación de la función h()
En los siguientes gráficos se puede visualizar el valor de la función h a lo largo de las iteraciones de una sola ejecución de cada algoritmo en un tablero de 15 reinas.

![imagen](https://user-images.githubusercontent.com/69587750/133861132-3f3391ea-54af-4e8a-a044-d04825be9282.png)
![imagen](https://user-images.githubusercontent.com/69587750/133861141-9ac5085a-7584-4718-9133-718ea6faa217.png)
![imagen](https://user-images.githubusercontent.com/69587750/133861149-2ad5a16f-79f7-414d-af16-bc31e4c6e266.png)

## Distribución del tiempo
A continuación se puede visualizar la distribución del tiempo para cada algoritmo a lo largo de 30 ejecuciones para los casos de 4, 8, 10, 12 y 15 reinas respectivamente.

![imagen](https://user-images.githubusercontent.com/69587750/133861400-a7e03377-066c-4606-8e16-8958ad99561a.png)
![imagen](https://user-images.githubusercontent.com/69587750/133861405-a2132f1b-6c20-4476-a2f4-1f5bdd3e2b4e.png)
![imagen](https://user-images.githubusercontent.com/69587750/133861418-1771ee9b-bfcb-4237-8448-ae8c48d376cc.png)

## Conclusión

Teniendo en cuenta el rendimiento de mi implementación de estos algoritmos (ya que soy consciente de que el rendimiento puede variar bastante dependiendo de la implementación), creo que el algoritmo más apropiado para resolver este problema es Simulated Annealing. En mi caso, si bien el algoritmo genético logra buenos resultados, creo que consume demasiados recursos y tiempo comparado a los otros algoritmos, que igual logran resultados similares. Creo que el poder de un algoritmo genético podría ser más explotado en otros problemas, sobre todo en aquellos donde los óptimos locales fueran una buena solución al problema. Y si comparamos entre hill climbing y simulated annealing, el que mejor resultados obtiene es simulated annealing, que los obtiene en un mayor número de iteraciones (que hill climbing), pero en menor tiempo total, debido a la baja complejidad de su implementación.
