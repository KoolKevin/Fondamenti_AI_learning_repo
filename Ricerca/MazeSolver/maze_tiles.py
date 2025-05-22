from enum import Enum
from config_constans import WHITE, BLACK, YELLOW, GREEN, RED 

class TipoCasella(Enum):
    PASSAGGIO = 0
    MURO = 1
    ESPLORATO = 2
    PERCORSO = 3
    START = 4
    END = 5

ColoriCasella = {
    TipoCasella.PASSAGGIO:  WHITE,
    TipoCasella.MURO:       BLACK,
    TipoCasella.ESPLORATO:  YELLOW,
    TipoCasella.PERCORSO:   GREEN,
    TipoCasella.START:      RED,
    TipoCasella.END:        GREEN, 
}