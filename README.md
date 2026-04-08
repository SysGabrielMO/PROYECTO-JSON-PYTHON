# PROYECTO-JSON-PYTHON
Proyecto del módulo de Lenguaje de Marcas en el cual se utiliza JSON y PYTHON

JSON elegido: eurocopa 2024
https://raw.githubusercontent.com/openfootball/euro.json/master/2024/euro.json

Se ha seleccionado un archivo JSON que contiene información sobre los partidos de la Eurocopa 2024.

La estructura del JSON está formada por:

Un objeto principal con:
"name": nombre del torneo.
"matches": array de objetos, donde cada objeto representa un partido.

Cada partido incluye:

Información general: 
"round", "date", "time", "team1", "team2", "ground".
"score": objeto con los resultados (final, descanso, prórroga, penaltis).
"goals1" y "goals2": arrays con los goles de cada equipo (jugador, minuto, etc.).

Modificación realizada
Se ha ampliado el JSON original añadiendo un nuevo campo en cada partido:
"yellow_cards": {
  "team1": X,
  "team2": Y
}

Este campo representa el número de tarjetas amarillas recibidas por cada equipo en el partido.
Los valores han sido generados de forma ficticia (inventados).


EJERCICIOS:

1.Listar información

Enunciado:
Lista todos los partidos del torneo mostrando:
 -Nombre del equipo local (team1)
 -Nombre del equipo visitante (team2)
 -Resultado final
 -Número de tarjetas amarillas de cada equipo



2. Contar información

Enunciado:
Muestra el número total de tarjetas amarillas:
 -En todo el torneo
- El total de tarjetas amarillas por cada equipo


3.Buscar o filtrar información

Enunciado:
Pide por teclado el nombre de un equipo y muestra todos los partidos en los que ha participado, indicando:
 -Rival
 -Resultado
 -Tarjetas amarillas recibidas en cada partido
 
 
4.Buscar información relacionada

Enunciado:
Pide por teclado el nombre de un jugador y muestra:
 -El partido en el que marcó
 -Los equipos que jugaban ese partido
 -El minuto del gol
 -El resultado final del partido
 
 
Ejercicio libre (clasificación por goles)

Enunciado:
Realiza una clasificación de todos los equipos del torneo en función del número total de goles marcados.

Para ello:

Suma todos los goles anotados por cada equipo en todos los partidos (usando goals1 y goals2).
Ordena los equipos de mayor a menor número de goles.

Para cada equipo, además:

Muestra un listado de sus jugadores que han marcado gol.
Ordena los jugadores de ese equipo de mayor a menor número de goles anotados.

La salida debe mostrar:

Nombre del equipo
Total de goles marcados
Lista de jugadores con sus goles, ordenados de mayor a menor



## Complicaciones encontradas durante el desarrollo

Una de las principales complicaciones fue interpretar correctamente la estructura del fichero JSON, ya que contiene varios niveles de información anidada. Esto obligó a trabajar con cuidado el acceso a los datos para evitar errores al recorrer partidos, marcadores y goles.

También surgieron dificultades al modificar el JSON original para añadir el campo de tarjetas amarillas, porque era necesario mantener una estructura homogénea en todos los partidos. Además, hubo que controlar casos en los que algunos campos no aparecían siempre de la misma forma.

Otro aspecto que requirió atención fue la implementación de búsquedas por equipo y jugador, gestionando correctamente mayúsculas, minúsculas y espacios introducidos por el usuario. Finalmente, la clasificación por goles también exigió revisar la lógica de cálculo, sobre todo en situaciones especiales como los goles en propia puerta.
