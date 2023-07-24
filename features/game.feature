Feature: Juego de la Vida de Conway
  Como jugador del Juego de la Vida
  Quiero poder interactuar con el tablero
  Para ver cómo evolucionan las células

Scenario: Crear un tablero vacío
  Given que el juego ha comenzado
  When creo un tablero vacío de 5x5
  Then el tablero debe estar vacío

Scenario: Colocar una célula viva
  Given que el juego ha comenzado
  And tengo un tablero vacío de 5x5
  When coloco una célula viva en la posición (2, 3)
  Then el tablero debe tener una célula viva en la posición (2, 3)

Scenario: Colocar múltiples células vivas
  Given que el juego ha comenzado
  And tengo un tablero vacío de 5x5
  When coloco células vivas en las posiciones (1, 2), (2, 3), (3, 3)
  Then el tablero debe tener células vivas en las posiciones (1, 2), (2, 3), (3, 3)

Scenario: Evolución del tablero
  Given que el juego ha comenzado
  And tengo un tablero de 5x5 con células vivas en las posiciones (2, 2), (2, 3), (3, 3)
  When paso a la siguiente generación
  Then el tablero debe evolucionar a la configuración con células vivas en las posiciones (2, 3), (3, 2), (3, 3)

Scenario: Comprobar reglas del juego
  Given que el juego ha comenzado
  And tengo un tablero de 5x5 con células vivas en las posiciones (1, 2), (2, 1), (2, 2), (2, 3)
  When paso a la siguiente generación
  Then el tablero debe evolucionar de acuerdo a las reglas del juego

