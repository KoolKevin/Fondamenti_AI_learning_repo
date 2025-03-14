import pygame
import random
import time

# Costanti per la finestra e la griglia
WIDTH, HEIGHT = 800, 800
GRID_SIZE = 21  # Deve essere dispari per un buon labirinto
CELL_SIZE = WIDTH // GRID_SIZE

# Colori
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)

# Direzioni per il movimento nel labirinto (alto, basso, sinistra, destra)
# due celle alla volta per garantire che tra due celle ci sia sempre un muero
DIRECTIONS = [(-2, 0), (2, 0), (0, -2), (0, 2)]

def generate_maze(screen, start, end):
    # 1 = muro, 0 = passaggio; inizialmente tutto murato, l'algoritmo "scava" i passaggi
    grid = [[1 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]  
    # Iniziamo dal punto (1,1)
    start_x, start_y = 1, 1  
    grid[start_x][start_y] = 0
    stack = [(start_x, start_y)]

    while stack:
        x, y = stack[-1] # equivale ad una peek
        random.shuffle(DIRECTIONS)  # Mischia le direzioni per generare percorsi casuali
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            # se il punto trovato è un muro appartenente alla griglia lo "scavo"
            if 1 <= nx < GRID_SIZE and 1 <= ny < GRID_SIZE and grid[nx][ny] == 1:
                grid[nx][ny] = 0  # Apri il percorso
                # scavo la cella intermedia (crea un percorso tra la cella vecchia e quella nuova)
                grid[x + dx // 2][y + dy // 2] = 0  
                stack.append((nx, ny)) # per dfs
                # stack.insert(0, (nx, ny)) # per bfs (non è che generi un buon labirinto)

                time.sleep(0.1) # per la visualizzazione
                draw_grid(screen, grid, start, end)
                break
        # in python un for può avere un else che viene eseguito 
        # quando dentro al ciclo non viene eseguito break
        else: 
            # se non ci sono nuove celle valide in nessuna direzione
            # la cella non è più da esplorare
            stack.pop()
    return grid

def draw_grid(screen, grid, start, end):
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            if grid[row][col] == 1:
                pygame.draw.rect(screen, BLACK, rect)  # Muro
            elif (row, col) == start:
                pygame.draw.rect(screen, GREEN, rect)  # Inizio
            elif (row, col) == end:
                pygame.draw.rect(screen, RED, rect)  # Fine
            else:
                pygame.draw.rect(screen, WHITE, rect)  # Percorso
            pygame.draw.rect(screen, BLUE, rect, 1)  # Griglia
    pygame.display.update()

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Labirinto con Pygame')
    
    start = (1, 1)
    end = (GRID_SIZE - 2, GRID_SIZE - 2) # (devo considerare anche un muro finale)

    grid = generate_maze(screen, start, end)
    
    running = True
    while running:
        # screen.fill(WHITE)
        draw_grid(screen, grid, start, end)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        time.sleep(0.1)
    
    pygame.quit()

if __name__ == '__main__':
    main()
