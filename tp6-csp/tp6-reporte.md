## Ejercicio 1

El sudoku de 9x9 se podría formular mediante CSP de la siguiente forma:

**Variables**: 81 variables, donde cada variable es una casilla en del sudoku. Podemos notar cada variable como Xij, siendo la variable que representa la casilla en la fila i y la columna j del sudoku.

**Dominio**: {1, 2, 3, 4, 5, 6, 7, 8, 9}. El dominio es este mismo para todas las variables, aunque algunas variables parten con un valor ya asignado de este dominio. Visto de cierto modo, se puede decir que partimos desde una solución parcial del problema (ya que las variables preasignadas cumplen con todas las restricciones del problema).

**Restricciones**: para este problema se tienen restricciones globales o de grado superior (de grado 9, precisamente). Bajo nuestra notación de variables, las restricciones son 3 y pueden ser notadas mediante el operador allDiff (los valores de todas las variables deben ser distintos):

No repetir valores por fila:
allDiff(Xi1, Xi2, Xi3, Xi4, Xi5, Xi6, Xi7, Xi8, Xi9), donde i es una fila del sudoku

No repetir valores por columna:
allDiff(X1j, X2j, X3j, X4j, X5j, X6j, X7j, X8j, X9j), donde j es una columna del sudoku

No repetir valores por recuadro:
allDiff(Xab, Xcd, Xef, Xjk, Xlm, Xnp, Xqr, Xst, Xuv), donde las 9 variables pertenecen al mismo de los 9 recuadros de 3x3 delimitados en el tablero.

**Ejecución**: podría en primera instancia revisar cada casilla vacía para dejarla en un estado consistente respecto a las casillas con números preasignados. A partir de entonces, simplemente sería cuestión de iterar eligiendo la próxima casilla mediante MRV y re-chequeando la consistencia de las casillas de la misma fila, columna y recuadro cada vez que se asigna un número en una casilla.

## Ejercicio 2

Para demostrar que la arco consistencia mediante el algoritmo AC-3 puede detectar la inconsistencia en este caso en particular del problema de colorear el mapa de Australia, lo único que hay que hacer es ejecutar el algoritmo paso a paso y llegaremos a esta conclusión.

Para esta demostración nos servirá de ayuda la representación del problema en forma de grafo. Tras asignar colores a WA y V, sin eliminar ninguna inconsistencia aún tenemos el siguiente grafo:

![imagen](https://user-images.githubusercontent.com/69587750/135764897-8a169411-9d46-47df-9355-a5db02b7d60f.png)

En la primer iteración, se elimina el color azul de los vecinos de V (es decir, de SA y NSW) y el color rojo de los vecinos de WA (que son SA y NT). Luego de hacer esto, SA queda con solo el color verde como posibilidad, por lo tanto se le asigna ese color y se encolan sus vecinos para re-chequear su consistencia (estos son NT, NSW y Q):

![imagen](https://user-images.githubusercontent.com/69587750/135764955-7338b899-8654-49b0-ad66-aed90f70c08f.png)

En la siguiente iteración, se elimina el color verde de los vecinos de SA, quedando NSW con solo el color rojo como posible y NT solo con azul. Por lo tanto ambos asumen tales colores y se encolan sus vecinos para re-chequear su consistencia (el único vecino restante es Q):

![imagen](https://user-images.githubusercontent.com/69587750/135767905-16eb4ac1-ac36-4db2-a7bf-a6cd381117d6.png)

Y en la última iteración, cuando se revisa Q, y se eliminan sus valores posibles inconsistentes, nos encontramos con que no puede tomar ninguno de los tres colores de forma consistente ya que tiene como vecinos a SA de verde, NT de azul y NSW de rojo. Por lo que hemos llegado a nuestra conclusión, es decir, que la asignación parcial dada es inconsistente:  

![imagen](https://user-images.githubusercontent.com/69587750/135768040-932500c7-c966-492d-a6d0-b73578745b7e.png)

De este modo, queda demostrado que el algoritmo AC-3 de arco consistencia es capaz de detectar que la asignación parcial {WA=rojo, V=azul} para este problema es inconsistente.

## Ejercicio 3

Supongamos que tenemos un grafo de restricciones que forma un árbol, entonces si tenemos n variables, tendremos a lo sumo n-1 arcos. Al tener un árbol, cada arco se puede encolar para verificar hasta una vez y es suficiente para garantizar su consistencia.  Además, suponiendo que cada variable puede tomar d valores distintos, sabemos que la consistencia de un arco se puede validar en tiempo O(d^2).

Entonces, tenemos en nuestro peor caso, n-1 arcos, que se encolarán 1 vez cada uno y con una complejidad de verificarlos de O(d^2), lo que nos da como resultado un tiempo de O((n-1)\*1\*d^2), simplificado como O(n\*d^2) para nuestro peor caso.

## Ejercicio 4

Podríamos guardar para cada valor de Xk, cuántos valores de Xi satisfacen ese valor de Xk dado. De modo que cuando se elimina un valor del dominio de Xi, se restaría uno al contador de los arcos (Xi, Xk) para los Xk que corresponda. Cuando este contador llegue a cero, entonces el arco se considera inconsistente con respecto a los valores restantes de Xi y debe ser re-evaluado. Teniendo en cuenta que la consistencia de un arco se puede validar en tiempo O(d^2) y que cuando tenemos n variables tenemos O(n^2) arcos, al evitar con esta implementación que cada nodo sea evaluado hasta d veces, obtenemos una complejidad total de O(n^2\*d^2), una mejora con respecto a la complejidad original de O(n^2\*d^3).

## Ejercicio 5

