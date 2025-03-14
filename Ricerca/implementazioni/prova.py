import pygame
import time
import random

# Costanti per la finestra e la griglia
WIDTH, HEIGHT = 800, 800
GRID_SIZE = 20
CELL_SIZE = WIDTH // GRID_SIZE

# Colori
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)

# Funzione di visualizzazione
def draw_grid(screen, grid, open_list, closed_list, path=[], start=None, end=None):
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            
            # Colorazione della griglia
            if (row, col) == start:
                pygame.draw.rect(screen, GREEN, rect)  # Start in verde
            elif (row, col) == end:
                pygame.draw.rect(screen, RED, rect)  # End in rosso
            elif grid[row][col] == 1:  # Ostacolo
                pygame.draw.rect(screen, BLACK, rect)
            elif (row, col) in closed_list:
                pygame.draw.rect(screen, BLUE, rect)  # Closed list in blu
            elif (row, col) in open_list:
                pygame.draw.rect(screen, YELLOW, rect)  # Open list in giallo
            elif (row, col) in path:
                pygame.draw.rect(screen, GREEN, rect)  # Path in verde
            else:
                pygame.draw.rect(screen, WHITE, rect)  # Spazio vuoto in bianco
                
            pygame.draw.rect(screen, BLACK, rect, 1)  # Bordo della cella

    pygame.display.update()

# Algoritmo A* (attualmente non implementato)
def a_star(start, end, grid):
    # Codice A* (spiegato più avanti)
    pass

# Funzione per aggiungere ostacoli casuali alla griglia
def add_obstacles(grid, obstacle_count=50):
    for _ in range(obstacle_count):
        x = random.randint(0, GRID_SIZE - 1)
        y = random.randint(0, GRID_SIZE - 1)
        if (x, y) != (1, 1) and (x, y) != (18, 18):  # Evita di mettere ostacoli su start e end
            grid[y][x] = 1  # 1 rappresenta un ostacolo

# Main loop
def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Visualizzazione A*')

    # Stato iniziale (sotto c'è una maniera idiomatica per inizializzare array in python
    # quello tra quadre viene detto ciclo interno)
    grid = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]  # 0 = spazio vuoto
    start = (0, 0)
    end = (GRID_SIZE-1, GRID_SIZE-1)

    add_obstacles(grid)  # Aggiungi ostacoli casuali

    open_list = [start]
    closed_list = []

    running = True
    while running:
        # Controllo eventi (per esempio, la chiusura della finestra)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Rendi lo sfondo bianco
        screen.fill(WHITE)
        
        # Disegna la griglia con start, end, ostacoli, open list, closed list, e path
        draw_grid(screen, grid, open_list, closed_list, start=start, end=end)

        # Aggiorna lo schermo
        pygame.display.update()

        # Ritarda il loop per non sovraccaricare il processore (ma senza fermarlo completamente)
        time.sleep(0.1)

    pygame.quit()

# Esegui il programma
if __name__ == '__main__':
    main()
