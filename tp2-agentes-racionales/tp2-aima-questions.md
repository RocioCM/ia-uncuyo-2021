# Preguntas del libro AIMA

### 2.10 Considere una versión modificada del entorno de la aspiradora del ejercicio 2.8, en el que el agente es penalizado restándole un punto por cada movimiento.

### ¿Puede un agente reflexivo simple ser perfectamente racional para este entorno? Explicar.

No, ya que como el agente no guarda registro de cuáles casillas ya recorrió, aunque este sea penalizado, no se puede obtener mejor desempeño que en el caso de que no fuera penalizado.

### ¿Y un agente reflexivo con estado?

En este caso, el agente podría guardar registro de las casillas que ya recorrió (por lo que ya están limpias) y solo moverse hacia casillas que no haya recorrido. De todos modos, el agente no sabe si la casilla a la cuál se está por mover (y por la cuál no ha pasado antes) estará limpia o sucia, por lo cual sigue sin maximizar los resultados, ya que no es capaz de evitar o reducir ese tipo de penalización.

### ¿Cómo cambian sus respuestas previas si las percepciones del agente le dan el estado de limpio o sucio de todas las baldosas del entorno?

En este caso, ambos agentes logran ser completamente racionales, ya que conociendo el estado del tablero completo, podrían ser capaces de, a cada movimiento, calcular cuál es la casilla sucia más cercana a su posición, de modo de dirigirse hacia ella y lograr la menor penalización posible, a la vez que el mayor rendimiento en limpieza. También el agente puede percibir cuando todas las casillas ya están limpias, de modo de detener su movimiento y evitar penalizaciones por tiempo indefinido (ya que se moverá sin nunca limpiar más casillas), logrando con esta implementación maximizar su desempeño.

### 2.11 Considere una versión modificada del entorno de la aspiradora del ejercicio 2.8, en el que la geografía del ambiente —su extensión, límites y obstáculos— se desconoce, al igual que la configuración inicial de suciedad (el agente puede ir hacia arriba y hacia abajo, así como hacia la izquierda y hacia la derecha).

### ¿Puede un agente reflexivo simple ser perfectamente racional para este entorno?

Teniendo en cuenta que el agente puede percibir si hay suciedad en la casilla en la que se encuentra y que no importa el número de movimientos que realiza (ya que no es penalizado), la respuesta es sí. Ya que en un número indeterminado de movimientos, el agente logrará limpiar toda la suciedad, es decir, maximizar su desempeño.

### ¿Puede un agente reflexivo simple con una función de agente aleatoria superar a un agente reflexivo simple?

No, ya que puede realizar acciones incoherentes (desde el punto de vista del objetivo y maximizar el rendimiento), como por ejemplo, moverse de una casilla sucia sin limpiarla o "no hacer nada" (ya sea en una casilla limpia o sucia).

### ¿Puede diseñar un entorno en el que su agente aleatorio tenga un desempeño deficiente? Muestre sus resultados.

Según lo experimentado (y gran parte reflejado en la tabla del ejercicio E.), el agente aleatorio tiene bajo desempeño en entornos muy amplios; en entornos medianos o amplios con un bajo nivel de suciedad (comparado a su desempeño en entornos del mismo tamaño pero con mayor suciedad); o en entornos donde la distribución de la suciedad es uniforme y con mucha distancia, es decir, no hay "islas" de suciedad, sino casillas de suciedad lejanas unas de otras; y por último, en general el agente aleatorio es ineficiente limpiando la suciedad de los bordes externos del entorno/tablero, por lo tanto un escenario donde la suciedad se encuentra concentrada en algunos bordes o esquinas del tablero podrían ser desventajoso para este agente.

### ¿Puede un agente reflexivo con estado superar a un agente reflexivo simple? ¿Puede diseñar un agente racional de este tipo?

Sí, ya que el agente con estado puede guardar registro de las casillas ya recorridas y/o limpiadas, por lo que puede elegir moverse a casillas que no ha explorado, logrando en menos movimientos los mismos resultados que podría lograr el agente sin estado.
