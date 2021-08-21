# Rendimiento

Se va a evaluar para cada tipo de agente el rendimiento que logra en cada entorno. El rendimiento se expresa en porcentaje (0% a 100%) de suciedad total limpiado después de 1000 acciones.

## Agente aleatorio

| Dirt Rate / Entorno | 2x2  | 4x4  | 8x8  | 16x16 | 32x32 | 64x64 | 128x128 |
| ------------------- | ---- | ---- | ---- | ----- | ----- | ----- | ------- |
| 0.1                 | 100% | 100% | 100% | 34%   | 15%   | 2%    | 0.7%    |
| 0.2                 | 100% | 100% | 92%  | 21%   | 7%    | 2%    | 0.5%    |
| 0.4                 | 100% | 100% | 80%  | 24%   | 8%    | 2%    | 0.5%    |
| 0.8                 | 100% | 100% | 59%  | 29%   | 10%   | 2%    | 0.6%    |

## Agente reflexivo

| Dirt Rate / Entorno | 2x2  | 4x4  | 8x8  | 16x16 | 32x32 | 64x64 | 128x128 |
| ------------------- | ---- | ---- | ---- | ----- | ----- | ----- | ------- |
| 0.1                 | 100% | 100% | 100% | 80%   | 12%   | 5%    | 2%      |
| 0.2                 | 100% | 100% | 100% | 88%   | 27%   | 6%    | 1.6%    |
| 0.4                 | 100% | 100% | 100% | 74%   | 25%   | 7%    | 2%      |
| 0.8                 | 100% | 100% | 100% | 80%   | 26%   | 5%    | 2%      |

## Conclusión

Es notorio que para tamaños pequeños ambos agentes tienen el mismo rendimiento, mientras que para tamaños mayores, es visible la ventaja del agente reflexivo por sobre el aleatorio (el agente reflexivo suele doblar el desempeño del aleatorio a partir de 16x16). Resulta interesante cómo, para un mismo tamaño de tablero, el rendimiento suele ser menor para un dirt rate de 0.1 que para porcentajes superiores.
