import random
import math
import time

from draw import draw_grid
from maze_tiles import TipoCasella
from config_constans import GRID_SIZE, MAZE_GEN_SLEEP_TIME

# Direzioni per il movimento nel labirinto (alto, basso, sinistra, destra)
# - due celle alla volta per garantire che in mezzo a due strade ci sia sempre un muro
Directions = [(-2, 0), (2, 0), (0, -2), (0, 2)]

def generate_maze(screen, start, end):
    # 1 = muro, 0 = passaggio; inizialmente tutto murato, l'algoritmo "scava" i passaggi
    grid = [[TipoCasella.MURO for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]  
    # Iniziamo dal punto (1,1) e non da (0,0) in quanto voglio avere il bordo del labirinto tutto murato
    startRow, startCol = start  
    grid[startRow][startCol] = TipoCasella.START
    
    stack = [start]

    while stack:
        row, col = stack[-1] # equivale ad una peek alla cima dello stack
        random.shuffle(Directions)  # Mischia le direzioni per generare percorsi casuali
        for dRow, dCol in Directions:
            nRow, nCol = row + dRow, col + dCol
            # se il punto trovato è un muro appartenente alla griglia lo "scavo"
            if 1 <= nRow < GRID_SIZE and 1 <= nCol < GRID_SIZE and grid[nRow][nCol] == TipoCasella.MURO:
                grid[nRow][nCol] = TipoCasella.PASSAGGIO 
                # scavo la cella intermedia (crea un percorso tra la cella vecchia e quella nuova)
                grid[row + dRow // 2][col + dCol // 2] = TipoCasella.PASSAGGIO 
                stack.append((nRow, nCol)) # per dfs
                # stack.insert(0, (nRow, nCol)) # per bfs (non è che generi un buon labirinto)
                time.sleep(MAZE_GEN_SLEEP_TIME) # per la visualizzazione
                draw_grid(screen, grid)
                break
        # in python un for può avere un else che viene eseguito 
        # quando dentro al ciclo non viene eseguito break
        else: 
            # se non ci sono nuove celle valide in nessuna direzione
            # la cella non è più da esplorare
            stack.pop()
    
    endRow, endCol = end 
    grid[endRow][endCol] = TipoCasella.END

    return grid



### maze con algoritmo di prim ###

def find_furthest_passage(grid, start):
    max_dist = -1
    furthest = start
    for r in range(GRID_SIZE):
        for c in range(GRID_SIZE):
            if grid[r][c] == TipoCasella.PASSAGGIO:
                dist = math.hypot(r - start[0], c - start[1])
                if dist > max_dist:
                    max_dist = dist
                    furthest = (r, c)
    return furthest


def generate_maze_prim(screen, start):
    grid = [[TipoCasella.MURO for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    startRow, startCol = start
    grid[startRow][startCol] = TipoCasella.PASSAGGIO

    # Lista di muri candidati: ogni elemento è (cella_muro, cella_corrisp)
    walls = []

    def add_walls(r, c):
        for dRow, dCol in Directions:
            nr, nc = r + dRow, c + dCol
            if 1 <= nr < GRID_SIZE - 1 and 1 <= nc < GRID_SIZE - 1:
                if grid[nr][nc] == TipoCasella.MURO:
                    walls.append(((nr, nc), (r + dRow // 2, c + dCol // 2)))

    add_walls(startRow, startCol)

    while walls:
        # Scegli un muro a caso
        (r, c), (between_r, between_c) = random.choice(walls)
        walls.remove(((r, c), (between_r, between_c)))

        # Controlla se la cella "dietro il muro" è ancora un muro
        if grid[r][c] == TipoCasella.MURO:
            # Conta le celle adiacenti "aperte"
            count = 0
            for dRow, dCol in Directions:
                nr, nc = r + dRow, c + dCol
                if 0 <= nr < GRID_SIZE and 0 <= nc < GRID_SIZE:
                    if grid[nr][nc] == TipoCasella.PASSAGGIO:
                        count += 1

            # Se solo una adiacente è già un passaggio, va bene "aprirla"
            if count == 1:
                grid[r][c] = TipoCasella.PASSAGGIO
                grid[between_r][between_c] = TipoCasella.PASSAGGIO
                add_walls(r, c)
                draw_grid(screen, grid)  # facoltativo: visualizzazione animata
                time.sleep(MAZE_GEN_SLEEP_TIME) # per la visualizzazione

    # Imposta inizio e fine
    grid[startRow][startCol] = TipoCasella.START
    end = find_furthest_passage(grid, start)
    grid[end[0]][end[1]] = TipoCasella.END

    return grid, end
