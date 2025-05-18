import pygame
import random
import time
from dataclasses import dataclass
from typing import Optional
from enum import Enum



# GRID_SIZE deve essere dispari siccome
# - il perimetro dello schermo voglio che sia murato 
# - l'algoritmo di generazione dei labirinti fa passi 
#   di due blocchi alla volta (in quanto in mezzo ad 
#   ogni strada voglio che ci sia un muro)
GRID_SIZE = 51
CELL_SIZE = 15
# Costanti per la finestra e la griglia
DIM_WINDOW = GRID_SIZE*CELL_SIZE
WIDTH, HEIGHT = DIM_WINDOW, DIM_WINDOW 

# Colori
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)



class TipoCasella(Enum):
    PASSAGGIO = 0
    MURO = 1
    ESPLORATO = 2
    PERCORSO = 3
    START = 4
    END = 5

@dataclass
class SearchState:
    rowPosition: int
    colPosition: int

@dataclass
class SearchNode:
    state: SearchState
    # forward reference tra virgolette in quant SearchNode è una struttura dati ricorsiva
    parent: Optional['SearchNode']  # parent può essere null per la radice e quindi Optional 
    action: tuple[int, int]
    depth: int
    pathCost: int



ColoriCasella = {
    TipoCasella.PASSAGGIO:  WHITE,
    TipoCasella.MURO:       BLACK,
    TipoCasella.ESPLORATO:  YELLOW,
    TipoCasella.PERCORSO:   GREEN,
    TipoCasella.START:      RED,
    TipoCasella.END:        GREEN, 
}

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
                # time.sleep(0.01) # per la visualizzazione
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










def bfs(screen, grid, start, end):
    return general_search(screen, grid, start, end, lambda frontiera, nodiFuturi: frontiera+nodiFuturi) 

def dfs(screen, grid, start, end):
    return general_search(screen, grid, start, end, lambda frontiera, nodiFuturi: nodiFuturi+frontiera) 

def expand(grid, nodo):
    possibiliNodiFuturi = []
    # per un problema generale dovrei implementare una SuccessorFn(stato)
    # che, dato uno stato, mi restituisce tutte le possibili azioni applicabili
    # e i relativi stati futuri
    # 
    # per questo problema posso limitarmi a controllare tutte le direzioni
    for dRow, dCol in Directions:
            # divide per due il passo dato che in Directions è largo 2
            nRow, nCol = nodo.state.rowPosition + dRow//2, nodo.state.colPosition + dCol//2 
            # se la casella trovata è un passaggio o il goal allora è una nuova posizione valida
            if grid[nRow][nCol] == TipoCasella.PASSAGGIO or grid[nRow][nCol] == TipoCasella.END: 
                nodoFuturo = SearchNode(
                    state=SearchState(nRow, nCol),
                    parent=nodo,
                    action=(dRow, dCol),
                    depth=nodo.depth+1,
                    pathCost=nodo.pathCost+1,
                )
                possibiliNodiFuturi.append(nodoFuturo)

    return possibiliNodiFuturi


def general_search(screen, grid, start, end, queueing_function):
    frontiera = []
    initialState = SearchState(start[0], start[1]) 
    initialNode = SearchNode(
        state=initialState,
        parent=None,
        action=None,
        depth=0,
        pathCost=0,
    )
    frontiera.append(initialNode)

    while frontiera:
        nodo = frontiera.pop(0)
        row = nodo.state.rowPosition
        col = nodo.state.colPosition
        # marchio come caselle esplorate tutte quelle che ho espanso tranne start ed end
        if (row != start[0] or col != start[1]) and (row != end[0] or col != end[1]): 
            grid[row][col] = TipoCasella.ESPLORATO
            draw_grid(screen, grid)
            time.sleep(0.02)
        # goal test
        if row == end[0] and col == end[1]:
            return nodo
        nodiFuturi = expand(grid, nodo)
        frontiera = queueing_function(frontiera, nodiFuturi)

    return None

def show_path_to_goal(screen, grid, goalNode): 
        # calcolo il percorso
        percorso = []
        current = goalNode
        while current is not None:
            percorso.append(current)
            current = current.parent
        percorso.reverse()  

        # disegno il percorso
        for p in percorso:
            row = p.state.rowPosition
            col = p.state.colPosition
            grid[row][col] = TipoCasella.PERCORSO
            draw_grid(screen, grid)
            time.sleep(0.02) 










def draw_grid(screen, grid):
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            # argomenti sono posizione e dimensione
            rect = pygame.Rect(col*CELL_SIZE, row*CELL_SIZE, CELL_SIZE, CELL_SIZE)

            if grid[row][col] == TipoCasella.PASSAGGIO:
                pygame.draw.rect(screen, ColoriCasella[TipoCasella.PASSAGGIO], rect)
            elif grid[row][col] == TipoCasella.MURO:
                pygame.draw.rect(screen, ColoriCasella[TipoCasella.MURO], rect)
            elif grid[row][col] == TipoCasella.ESPLORATO:
                pygame.draw.rect(screen, ColoriCasella[TipoCasella.ESPLORATO], rect)
            elif grid[row][col] == TipoCasella.PERCORSO:
                pygame.draw.rect(screen, ColoriCasella[TipoCasella.PERCORSO], rect)
            elif grid[row][col] == TipoCasella.START:
                pygame.draw.rect(screen, ColoriCasella[TipoCasella.START], rect)
            elif grid[row][col] == TipoCasella.END:
                pygame.draw.rect(screen, ColoriCasella[TipoCasella.END], rect)  
          
            pygame.draw.rect(screen, BLUE, rect, 1)  # Griglia
    pygame.display.update()

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Labirinto con Pygame')
    
    start = (1, 1)
    end = (GRID_SIZE - 2, GRID_SIZE - 2) # (devo considerare anche un muro finale)
    grid = generate_maze(screen, start, end)
    
    goalNode = dfs(screen, grid, start, end)
    show_path_to_goal(screen, grid, goalNode)

    running = True
    while running:
        # screen.fill(WHITE)
        draw_grid(screen, grid)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        time.sleep(0.1)
    
    pygame.quit()

if __name__ == '__main__':
    main()
