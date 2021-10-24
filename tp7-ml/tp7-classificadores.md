## Random classifier

#### Matrix de confusión:

| n = 6383   | Predicted YES | Predicted NO |
| ---------- | ------------- | ------------ |
| Actual YES | 361           | 342          |
| Actual NO  | 2870          | 2810         |

#### Métricas:

| Métrica                   | Valor |
| ------------------------- | ----- |
| Accuracy                  | 0.497 |
| Precision                 | 0.112 |
| Sensitivity               | 0.514 |
| Specificity               | 0.495 |
| Negative predictive value | 0.891 |

## Bigger-class classifier:

#### Matriz de confusión:

| n = 6383   | Predicted YES | Predicted NO |
| ---------- | ------------- | ------------ |
| Actual YES | 0             | 703          |
| Actual NO  | 0             | 5680         |

#### Métricas:

| Métrica                   | Valor                  |
| ------------------------- | ---------------------- |
| Accuracy                  | 0.89                   |
| Precision                 | NaN (division by zero) |
| Sensitivity               | 0                      |
| Specificity               | 1                      |
| Negative predictive value | 0.89                   |
