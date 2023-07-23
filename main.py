import colorama
import time
import random

def clear_console():
    # Limpia la consola dependiendo del sistema operativo
    import os
    if os.name == "nt":  # Windows
        os.system("cls")
    else:  # UNIX
        os.system("clear")

def print_dynamic_image(width, height):
    # Inicializa colorama para permitir el uso de secuencias de escape ANSI en Windows
    colorama.init(autoreset=True)

    while True:
        image = []

        # Genera una nueva imagen con colores aleatorios
        for y in range(height):
            row = []
            for x in range(width):
                r, g, b = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
                pixel_color = f"\033[48;2;{r};{g};{b}m  \033[0m"
                row.append(pixel_color)
            image.append(row)

        # Imprime la imagen en la consola
        clear_console()
        for row in image:
            print("".join(row))

        # Espera un corto período de tiempo antes de actualizar la imagen
        time.sleep(0.5)

if __name__ == "__main__":
    # Tamaño de la imagen (ancho x alto)
    image_width, image_height = 50, 20

    # Muestra una imagen dinámica en la consola
    print_dynamic_image(image_width, image_height)