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

Al probar las dos fechas en Python, la primera fecha salió True porque el 9 de octubre es antes que el 16 de octubre. La segunda fecha salió False porque Python compara primero los días y el 31 es mayor que el 02. El formato AAAA-MM-DD es mejor porque permite ordenar las fechas de la más antigua a la más reciente. Si usamos DD/MM/AAAA, las fechas pueden quedar desordenadas y la búsqueda binaria podría no encontrar una fecha correctamente.


### Pregunta 4
Las tasas aumentaban poco a poco en 2023. En 2025 no tendría mucho sentido buscar por tasa, porque el tipo de cambio se mantiene fijo y varias fechas tendrían la misma tasa.

### Pregunta 5
La búsqueda lineal haría hasta 2,600 comparaciones y la búsqueda binaria aproximadamente 12 comparaciones en el peor caso.
