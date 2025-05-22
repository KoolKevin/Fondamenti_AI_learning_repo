import pygame

from config_constans import GRID_SIZE
from config_constans import CELL_SIZE
from maze_tiles import TipoCasella
from maze_tiles import ColoriCasella

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
          
            # pygame.draw.rect(screen, BLUE, rect, 1)  # Griglia
    pygame.display.update()