import colorama
import time
import random

dead = f"\033[48;2;0;0;0m  \033[0m"
alive = f"\033[48;2;255;255;255m  \033[0m"


def clear_console():
    # Limpia la consola dependiendo del sistema operativo
    import os
    if os.name == "nt":  # Windows
        os.system("cls")
    else:  # UNIX
        os.system("clear")


def create_board(width, height):
    # Crea un tablero con celdas muertas
    return [[0 for _ in range(width)] for _ in range(height)]


def create_cell_alive(board):
    # Crea un tablero con celdas muertas
    for y in range(len(board)):
        for x in range(len(board[0])):
            board[y][x] = random.randint(0, 1)
    return board


def evolve(board):
    new_board = create_board(len(board[0]), len(board))

    for y in range(len(board)):
        for x in range(len(board[0])):
            new_board[y][x] = destiny(board, y, x) if 1 or 0 else board[y][x]
            # print(destiny(board,y,x))
    return new_board


def destiny(board, y, x):
    current_cell = board[y][x]

    destinyty = 1
    vivos = [
        get_top_left(board, y, x),
        get_left_center(board, y, x),
        get_bottom_left(board, y, x),
        get_top_center(board, y, x),
        get_bottom_center(board, y, x),
        get_top_right(board, y, x),
        get_center_right(board, y, x),
        get_lower_right(board, y, x)
    ].count(1)
    # print(vivos, muertos)

    if current_cell == 1:
        # Cualquier célula viva con dos o tres vecinos vivos sobrevive.
        if vivos in (2, 3):
            destinyty = 1
        else:
            destinyty = 0

    else:
        # Cualquier célula muerta con tres vecinos vivos se convierte en una célula viva.
        if vivos == 3:
            destinyty = 1
        else:
            # Todas las demás células vivas mueren en la próxima generación. Del mismo modo,
            # todas las demás células muertas permanecen muertas.
            destinyty = False

    return destinyty


# [*,-,-]
# [-,-,-]
# [-,-,-]
def get_top_left(board, y, x):
    try:
        return board[y-1][x]
    except IndexError:
        return 0

# [-,-,-]
# [*,-,-]
# [-,-,-]


def get_left_center(board, y, x):
    try:
        return board[y][x-1]
    except IndexError:
        return 0


# [-,-,-]
# [-,-,-]
# [*,-,-]
def get_bottom_left(board, y, x):
    try:
        return board[y+1][x-1]
    except IndexError:
        return 0

# [-,*,-]
# [-,-,-]
# [-,-,-]


def get_top_center(board, y, x):
    try:
        return board[y-1][x]
    except IndexError:
        return 0

# [-,-,-]
# [-,*,-]
# [-,-,-]


def get_center_center(board, y, x):
    try:
        return board[y][x]
    except IndexError:
        return 0

# [-,-,-]
# [-,-,-]
# [-,*,-]


def get_bottom_center(board, y, x):
    try:
        return board[y+1][x]
    except IndexError:
        return 0
# [-,-,*]
# [-,-,-]
# [-,-,-]


def get_top_right(board, y, x):
    try:
        return board[y-1][x+1]
    except IndexError:
        return 0
# [-,-,-]
# [-,-,*]
# [-,-,-]


def get_center_right(board, y, x):
    try:
        return board[y][x+1]
    except IndexError:
        return 0
# [-,-,-]
# [-,-,-]
# [-,-,*]


def get_lower_right(board, y, x):
    try:
        return board[y+1][x+1]
    except IndexError:
        return 0


def contar_unos_y_ceros(array):
    # print(array)
    contador_unos = 0
    contador_ceros = 0

    for elemento in array:
        if elemento == 1:
            contador_unos += 1
        elif elemento == 0:
            contador_ceros += 1

    return contador_unos, contador_ceros


def print_board(board, image):
    # Genera una nueva imagen con colores aleatorios
    for y in range(len(board)):
        row = []
        for x in range(len(board[0])):
            num = board[y][x]
            row.append(f"{ alive if num.__eq__(1) else dead }")
        image.append(row)

    # Imprime la imagen en la consola
    for row in image:
        print("".join(row))


def esta_en_el_borde(filas, columnas, fila, columna):
    if fila == 0 or fila == filas - 1:
        return True
    # Verificar si el punto está en el borde izquierdo o derecho
    if columna == 0 or columna == columnas - 1:
        return True
    return False


if __name__ == "__main__":
    # Inicializa colorama para permitir el uso de secuencias de escape ANSI en Windows
    colorama.init(autoreset=True)
    # Tamaño de la imagen (ancho x alto)
    image_width, image_height = 40, 20

    # Crear tablero con celulas muertas
    board = create_board(image_width, image_height)
    # Agregar celulas vivas
    board_alive = create_cell_alive(board)

    image = []
    generation = 0
    while True:
        clear_console()
        generation += 1
        print(f"Generación: { generation }")
        image = []

        print_board(board_alive, image)
        # print_board(current_board,image)

        # time.sleep(1)
        board_alive = evolve(board_alive)
