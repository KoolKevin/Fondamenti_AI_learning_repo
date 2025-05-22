import pygame
import time

from maze_gen import generate_maze_prim
from draw import draw_grid 
from search import dfs, show_path_to_goal
from config_constans import WIDTH, HEIGHT, MAZE_UPDATE_SLEEP_TIME 



def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Labirinto con Pygame')
    
    start = (1, 1)
    # end = (GRID_SIZE - 2, GRID_SIZE - 2) # (devo considerare anche un muro finale)
    grid, end = generate_maze_prim(screen, start)
    
    goalNode = dfs(screen, grid, start, end)
    show_path_to_goal(screen, grid, goalNode)

    running = True
    while running:
        draw_grid(screen, grid)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        time.sleep(MAZE_UPDATE_SLEEP_TIME)
    
    pygame.quit()

if __name__ == '__main__':
    main()

