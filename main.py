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


def create_board(width, height):
    # Crea un tablero con celdas muertas
    return [[0 for _ in range(width)] for _ in range(height)]

def create_cell_alive(board):
    # Crea un tablero con celdas muertas
    for y in range(len(board)):
        for x in range(len(board[0])):
            board[y][x]=random.randint(0, 1)   
    return board

def print_dynamic_image(width, height):
    # Inicializa colorama para permitir el uso de secuencias de escape ANSI en Windows
    colorama.init(autoreset=True)
    
    

    while True:
        image = []

        # Genera una nueva imagen con colores aleatorios
        for y in range(height):
            row = []
            for x in range(width):
                num = random.randint(0, 1)  
                row.append(f"{ alive if num.__eq__(1) else dead }")
            image.append(row)

        # Imprime la imagen en la consola
        clear_console()
        for row in image:
            print("".join(row))

        # Espera un corto período de tiempo antes de actualizar la imagen
        time.sleep(1)

if __name__ == "__main__":
    # Tamaño de la imagen (ancho x alto)
    image_width, image_height = 10, 10

    # Muestra una imagen dinámica en la consola
    # print_dynamic_image(image_width, image_height)
    
    # Crear tablero con celulas muertas 
    board = create_board(image_width, image_height)
    for x in board:
        print(x)
    
    print()
    
    board_alive = create_cell_alive(board)
    for x in board_alive:
        print(x)
    
    
    
    
    
    
    
    