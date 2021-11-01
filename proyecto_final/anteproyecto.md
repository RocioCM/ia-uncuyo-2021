# Resolución de Cubos Rubik

### **Código del Proyecto:** `rubik-cube`

### **Estudiante:** Rocío Corral

<img src="https://user-images.githubusercontent.com/69587750/139362634-e8ff2b1f-3eed-465d-921e-73705015923b.png" alt="Rubik Cube" width="200"/>

## Descripción

Breve detalle general de la idea. Incluir objetivos, alcance, limitaciones y forma de evaluación (métricas) de los resultados. Por ejemplo, se va a evaluar el tiempo de ejecución, la cantidad de veces que llega a un estado objetivo, la tasa de observaciones correctamente detectadas, etc.. Si se ha consultado bibliografía incluir un link por cada artículo consultado.

---

Se busca implementar un algoritmo de Inteligencia Artificial que aprenda a resolver un cubo rubik de 3x3 sin ningún conocimiento a priori más que el estado objetivo y los 12 movimientos posibles que se pueden hacer en el cubo. En la práctica, el algoritmo debería ser capaz de llegar al estado objetivo a partir de cualquier estado del cubo alcanzado a través de la ejecución de x cantidad de movimientos del cubo partiendo del estado objetivo o armado. Esto se debe a la matemática intrínseca del cubo, ya que si se elige la distribución de colores o piezas del cubo de forma completamente aleatoria, es posible que el cubo quede en un estado irresolubre utilizando los 12 movimientos posibles del cubo. El desempeño del algoritmo se medirá en primera instancia, considerando si el algoritmo alcanzó el estado objetivo. En caso de no alcanzarlo tras n cantidad de iteraciones, se considerará "qué tan cerca está el cubo estar armado (medido en cantidad de piezas por cara correctamente colocadas). En caso de alcanzar la solución, se medirá en cuántas iteraciones lo logró y cuánto tiempo tomó.

Estas métricas se tomarán sobre x cantidad de ejecuciones del algoritmo partiendo de estados iguales y luego distintos a la hora de tomar la métrica, para verificar cuanto influye del factor aleatorio en estas medidas.

...

## Justificación:

Por que se considerá que se puede aplicar algoritmos de IA. Porque se considera que se puede aplicar algoritmos/técnicas de IA y no solucionar mediante algún otro enfoque.

---

Dada la cantidad de posibles estados de un cubo rubik realizando movimientos de sus caras a partir del estado armado (al rededor de ...) y teniendo en cuenta que el estado objetivo es solo 1, se revela a simple vista que una aproximación por fuerza bruta es inviable. Cuando una persona se enfrenta a este puzzle, la solución se alcanza paso a paso observando el estado actual del cubo, ejecutando una secuencia específica de movimientos para llegar a otro estado más cercano a la solución y repitiendo con secuencias de movimientos cada vez más complejas (para no revertir el trabajo ya hecho en los pasos previos). Desde esta perspectiva, se podría programar un algoritmo de estados finitos, que determine el estado del cubo y en base a esto decida qué secuencia de movimientos de las provistas ejecuta. Pero esto sería obligar a la computadora a resolver el cubo como un humano lo haría. La idea detrás de usar un algoritmo de Inteligencia Artificial como lo es el Reinforcement Learning o un algoritmo genético es lograr no sólo que la computadora resuelva el cubo, sino observar cómo aprende a hacerlo a su vez qué tan eficientemente lo hace, y esto es algo que no se puede lograr a través de los enfoques previos, en donde se le proveen al algoritmo las reglas y únicamente debe aplicarlas en orden.

## Listado de actividades a realizar

Incluir entre 8 y 10 actividades (mientras más desglosadas las actividades, mejor). Incluir una estimación de tiempo de cada actividad.

Actividad 1. Recopilación de bibliografía y/o ejemplos del problema a resolver. [7 días] Actividad 2. Puesta a punto del código fuente de base para resolver el problema [4 días] Actividad 3. Implementación de característica A dentro del código. [4 días] Actividad 4. Implementación de característica B dentro del código. [4 días] Actividad 5. Implementación de característica C dentro del código. [7 días] Actividad 6. Ejecución de los experimentos a fin de validar el objetivo. [1 día] Actividad 7. Análisis de los resultados. [2 días] Actividad 8. Escritura de informe final. [7 días]

## Cronograma estimado de actividades:

Tener en cuenta que pueden haber actividades que pueden realizarse en paralelo y otras que no.
