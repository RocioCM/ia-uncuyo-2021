# Agentes Racionales

## Contenido:

**Ejercicio A**: análisis disponible en `tp2-peas.md`

**Ejercicios B, C y E**: implementación disponible en la carpeta `/code`

**Ejercicio D**: análisis disponible en `tp2-results.md`

**Ejercicio F**: respuestas disponibles en `tp2-aima-questions.md`


## Código

La implementación de los agentes y el entorno se hizo siguiendo el paradigma orientado a objetos. La clase abstracta `Agent` implementa comportamientos comunes a los agentes de tipo aletorio y reflexivo (`RandomAgent` y `ReflexiveAgent`, respectivamente). Mientras que la clase `Environment` implementa funcionalidades correspondientes al entorno. 

En el archivo `main.py` se puede encontrar a modo de ejemplo la instanciación de un entorno, un agente reflexivo y la medición de su desempeño en ese entorno. A su vez, se encuentra comentado el código para el análisis de desempeño de un agente aleatorio en entornos de distintas dimensiones y con distinto grado de suciedad. Esta secuencia se puede ejecutar mediante el comando: 

`py code/main.py`
