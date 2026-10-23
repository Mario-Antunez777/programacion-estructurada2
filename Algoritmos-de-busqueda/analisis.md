# Análisis · Algoritmos de búsqueda
Nombre: Mario Andres Antunez Rivera .
Carné: 6B9A59C2

## Proyecto 1 · Tipo de cambio del BCN

| Fecha buscada | Comparaciones lineal                            | Comparaciones binaria                                          |
|---------------|-------------------------------------------------|-------------------------------------------------------------   |
| 2023-10-02    |posición 0 con 1 comparaciones                   | posición 0 con 4 comparaciones                                 |
| 2023-10-20    |22 comparaciones                                 | 5 comparaciones                                                |
| 2023-10-31    |22 comparaciones                                 | 4 comparaciones                                                |
| 2023-10-07    |22 comparaciones                                 | 4 comparaciones                                                |




### Pregunta 1   ¿En cuál de las cuatro la lineal le gana o empata con la binaria, y por qué?

La búsqueda lineal le gana a la binaria porque al buscar la fecha 2023-10-02 , porque la encuentra en la primera posición y solo necesita una comparación, mientras que la binaria necesita cutro
### Pregunta 2 Peor caso de cada algoritmo

La búsqueda lineal tiene un peor  caso de 22 comparaciones, porque revisa todas las fechas cuando el elemento no existe o está al final .

La búsqueda binaria tiene un peor caso de 5 comparaciones con estas 22 fechas. Para comprobarlo,  busca una fecha que no exista, como   2023-11-01, y se cuentan las comparaciones realizadas por el algoritmo.

### Pregunta 3 
La primera fecha dio True porque el 9 de octubre es antes que el 16 de octubre. La segunda dio False porque Python compara primero el año, luego  el mes y luego el día, y como el 31 es mayor que el 02 dio False.
El formato AAAA-MM-DD es mejor porque las fechas quedan en orden, de la más vieja a la más nueva. Con DD/MM/AAAA se desordenan y la búsqueda binaria no funcionaría bien.


### Pregunta 4
En 2023 las tasas iban subiendo poco a poco. En 2025 no sirve buscar por tasa porque el tipo de cambio casi no cambia y muchas fechas tienen la misma tasa.

### Pregunta 5
La búsqueda lineal haría hasta 2,600 comparaciones y la búsqueda binaria aproximadamente 12 comparaciones en el peor caso.
