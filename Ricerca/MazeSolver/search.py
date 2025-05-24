import time
import math
from dataclasses import dataclass
from typing import Optional

from maze_gen import Directions
from draw import draw_grid
from maze_tiles import TipoCasella
from config_constans import TILE_EXPLORATION_SLEEP_TIME, GOAL_REACHING_SLEEP_TIME

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



# tutte queste funzioni invocano general_search passandole una queueing-fn,
# ovvero una funziona che ordina la frontiera secondo la logica della ricerca
# durante i passi di espansione
def bfs(screen, grid, start, end):
    return general_search(screen, grid, start, end, lambda frontiera, nodiFuturi: frontiera+nodiFuturi) 

def dfs(screen, grid, start, end):
    return general_search(screen, grid, start, end, lambda frontiera, nodiFuturi: nodiFuturi+frontiera) 

def ucs(screen, grid, start, end):
    def lesserPathCost(frontiera, nodiFuturi):
        newFrontiera = frontiera+nodiFuturi
        newFrontiera.sort(key=lambda nodo: nodo.pathCost)
        return newFrontiera
    
    return general_search(screen, grid, start, end, lesserPathCost) 
     
def a_star(screen, grid, start, end):
    def evalNode(node):
        rowDistance = abs(end[0] - node.state.rowPosition)
        colDistance = abs(end[1] - node.state.colPosition)
        # distanza di manahattan (molto meglio)
        heuristicDistanceFromGoal = rowDistance + colDistance
        # distanza euclidea (troppo ottimista)
        # heuristicDistanceFromGoal = math.sqrt(rowDistance*rowDistance + colDistance*colDistance)
        return node.pathCost + heuristicDistanceFromGoal
    
    def sortByEval(frontiera, nodiFuturi):
        newFrontiera = frontiera+nodiFuturi
        newFrontiera.sort(key=evalNode)
        return newFrontiera
    
    return general_search(screen, grid, start, end, sortByEval)


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
            time.sleep(TILE_EXPLORATION_SLEEP_TIME)
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
            time.sleep(GOAL_REACHING_SLEEP_TIME) 
