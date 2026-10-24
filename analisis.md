# Análisis · Algoritmos de búsqueda
Nombre: Mario Andres Antunez Rivera
Carné: 6B9A59C2
 
## Proyecto 1 · Tipo de cambio del BCN
 
| Fecha buscada | Comparaciones lineal                            | Comparaciones binaria                                          |
|---------------|-------------------------------------------------|-------------------------------------------------------------   |
| 2023-10-02    |posición 0 con 1 comparaciones                   | posición 0 con 4 comparaciones                                 |
| 2023-10-20    |posición 14 con 15 comparaciones                 | posición 14 con 4 comparaciones                                |
| 2023-10-31    |posición 21 con 22 comparaciones                 | posición 21 con 5 comparaciones                                |
| 2023-10-07    |22 comparaciones                                 | 4 comparaciones                                                |
 
### Pregunta 1
**¿En cuál de las cuatro la lineal le gana o empata con la binaria, y por qué?**
 
La lineal le gana a la binaria al buscar 2023-10-02, porque la encuentra en la primera posición y solo necesita 1 comparación, mientras que la binaria necesita 4.
 
### Pregunta 2
**Peor caso de cada algoritmo**
 
La búsqueda lineal tiene un peor caso de 22 comparaciones, porque revisa todas las fechas cuando el elemento no existe o está al final.
 
La búsqueda binaria tiene un peor caso de 5 comparaciones con estas 22 fechas. Para comprobarlo se busca una fecha que no exista, como 2023-11-01, y se cuentan las comparaciones que hace el algoritmo.
 
### Pregunta 3
La primera fecha dio True porque el 9 de octubre es antes que el 16 de octubre. La segunda dio False porque Python compara primero el año, luego el mes y luego el día, y como el 31 es mayor que el 02 dio False.
 
El formato AAAA-MM-DD es mejor porque las fechas quedan en orden, de la más vieja a la más nueva. Con DD/MM/AAAA se desordenan y la búsqueda binaria no funcionaría bien.
 
### Pregunta 4
En 2023 las tasas iban subiendo poco a poco. En 2025 no sirve buscar por tasa porque el tipo de cambio casi no cambia y muchas fechas tienen la misma tasa.
 
### Pregunta 5
La búsqueda lineal haría hasta 2,600 comparaciones y la búsqueda binaria aproximadamente 12 comparaciones en el peor caso.
 
---
 
## Proyecto 2 · Consulta de estudiantes por carné UNI
 
| Carné buscado | Comparaciones lineal                            | Comparaciones binaria                                          |
|---------------|-------------------------------------------------|-------------------------------------------------------------   |
|2023-0118U     |10 comparaciones                                 |3 comparaciones                                                 |
|2024-0344U     |10 comparaciones                                 |4 comparaciones                                                 |
|2025-0560U     |10 comparaciones                                 |4 comparaciones                                                 |
|2024-0999U     |10 comparaciones                                 |4 comparaciones                                                 |
 
### Pregunta 1
**¿Por qué uno de los carnés se encuentra con una sola comparación binaria?**
 
Porque es el carné que está justo en el medio de la lista. La binaria siempre empieza mirando el elemento del medio, y si ahí está el carné que busco, lo encuentra de una.
 
### Pregunta 2
**¿Por qué la búsqueda por nombre no puede ser binaria con estas listas? Si quisieras usar la binaria para buscar nombres, ¿qué tendrías que hacerle a las listas y qué cuidado debes tener para que sigan siendo paralelas?**
 
Porque la lista está ordenada por carné, no por nombre. Para usarla tendría que ordenar los nombres de la A a la Z y mover también carnes, carreras y promedios igual, con los mismos índices, para que cada nombre siga con sus datos.
 
### Pregunta 3
**buscar_todos siempre hace 30 comparaciones. ¿Por qué no puede detenerse en la primera coincidencia, como la lineal normal?**
 
Porque busca todas las coincidencias y puede haber más repetidas más adelante. Si para en la primera, se pierde las demás.
 
### Pregunta 4
**Si la UNI tuviera 12,000 estudiantes en esta lista, ¿cuántas comparaciones haría cada algoritmo en el peor caso? ¿Y con 24,000? Explica qué observas al duplicar la cantidad de estudiantes.**
 
- 12,000: lineal 12,000, binaria 14.
- 24,000: lineal 24,000, binaria 15.
Al duplicar, la lineal también se duplica, pero la binaria solo sube 1.
 
### Pregunta 5
**Un estudiante de nuevo ingreso recibe el carné 2026-0001U. ¿En qué posición debe agregarse para que la binaria siga funcionando? ¿Qué pasaría si se insertara al inicio de la lista?**
 
Va al final, porque es el más grande y así la lista sigue ordenada. Si lo pongo al inicio, se desordena y la binaria no lo encontraría.
 