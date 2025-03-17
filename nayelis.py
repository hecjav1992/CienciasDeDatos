import pygame
import math
import requests
from io import BytesIO

# Inicializar pygame
pygame.init()

# Configuración de la pantalla
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Movimiento Lineal y Circular con Fondo desde URL")

# Colores
RED = (255, 0, 0)

# Función para cargar una imagen desde una URL
def load_image_from_url(url):
    try:
        response = requests.get(url, timeout=5)  # Agregar timeout para evitar bloqueos
        response.raise_for_status()  # Lanzar error si la respuesta no es exitosa
        image_data = BytesIO(response.content)
        return pygame.image.load(image_data)
    except requests.RequestException as e:
        print(f"Error al cargar la imagen desde la URL: {e}")
        return None  # Retornar None en caso de error

# Cargar la imagen de fondo desde la URL
background_url = "https://static.vecteezy.com/system/resources/previews/011/484/135/non_2x/pixel-art-shopping-street-with-shops-and-ice-cream-shop-avenue-with-lamp-and-trees-cityscape-background-for-8bit-game-vector.jpg"
background_image = load_image_from_url(background_url)
if background_image:
    background_image = pygame.transform.scale(background_image, (width, height))

# Cargar la imagen del objeto en movimiento
try:
    object_image = pygame.image.load("auto.png")  # Asegurar que el archivo existe
    object_image = pygame.transform.scale(object_image, (50, 50))  # Redimensionar si es necesario
except pygame.error as e:
    print(f"Error al cargar 'auto.png': {e}")
    object_image = None  # Usar None si no se encuentra la imagen

# Tamaño y posición inicial del cuadrado
square_size = 50
square_x = 100
square_y = 550#height // 2 - square_size // 2

# Velocidad del movimiento lineal
speed = 5

# Variables para el movimiento circular
angle = 0
radius = 100
center_x = width // 2
center_y = height // 2

# Estado del movimiento (lineal o circular)
movement_type = "lineal"

# Bucle principal
running = True
clock = pygame.time.Clock()

while running:
    screen.fill((0, 0, 0))  # Limpiar pantalla con negro para evitar residuos
    
    # Dibujar la imagen de fondo si está disponible
    if background_image:
        screen.blit(background_image, (0, 0))

    # Manejo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_l:
                movement_type = "lineal"
            elif event.key == pygame.K_c:
                movement_type = "circular"

    # Movimiento del objeto
    if movement_type == "lineal":
        square_x += speed
        if square_x > width:
            square_x = -square_size
    elif movement_type == "circular":
        angle += 0.02
        square_x = center_x + radius * math.cos(angle) - square_size // 2
        square_y = center_y + radius * math.sin(angle) - square_size // 2

    # Dibujar el objeto en movimiento
    if object_image:
        screen.blit(object_image, (square_x, square_y))
    else:
        pygame.draw.rect(screen, RED, (square_x, square_y, square_size, square_size))  # Dibuja un cuadrado si no hay imagen

    # Actualizar la pantalla
    pygame.display.flip()
    clock.tick(60)

# Salir de pygame
pygame.quit()
