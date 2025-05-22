# GRID_SIZE deve essere dispari siccome
# - il perimetro dello schermo voglio che sia murato 
# - l'algoritmo di generazione dei labirinti fa passi 
#   di due blocchi alla volta (in quanto in mezzo ad 
#   ogni strada voglio che ci sia un muro)
GRID_SIZE = 51
CELL_SIZE = 10

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

# tempi di sleep per mostrare la ricerca
MAZE_GEN_SLEEP_TIME = 0
MAZE_UPDATE_SLEEP_TIME = 1
TILE_EXPLORATION_SLEEP_TIME = 0.1
GOAL_REACHING_SLEEP_TIME = 0.1