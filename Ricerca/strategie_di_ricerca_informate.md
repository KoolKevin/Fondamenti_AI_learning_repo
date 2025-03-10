conoscenza euristica sul dominio
- si traduce in una funzione di valutazione che stima un punteggio per tutti i nodi da espandere
- quanta fatica faccio per raggiungere il goal espandendo un determinato nodo
- tradeoff sul calcolo della funzione di valutazione e espansione con "forza bruta"

bisogna capire qual'è il nodo "più promettente"?

**anticipazione**: una funzione di valutazione che restituisce una distanza minore rispetto a quella reale per arrivare al goal ci piace! Euristica ottimistica


### Ricerca greedy best-first
La ricerca greedy best-first espande il nodo che sembra più vicino al goal

...


### Ricerca A*
due contributi:
- g(n): costo per arrivare al prossimo nodo (quanto ho speso fino ad ora?)
- h(n): distanza dal goal


**NB**: impara la notazione dell'esempio del filetto con A* (lo mette all'esame)
- tra parentesi si mette l'ordine di espansione dei nodi


...

l'ottimalità di A* non è sempre garantita, dipende dalla funzione euristica

dimostrazione carina che convince che se l'euristica è ottimale, allora A* sceglie sempre il percorso migliore (ottimale)
- chiaramente eventualmente fa backtracking, però trova la soluzione ottima
- dire che l'euristica è ammissibile è equivalente a dire che A* trova l'ottimo



### FUnzioni euristiche 
Date due funzioni euristiche ammissibili è meglio scegliere quella con costo maggiore per ogni nodo n (più lontana da BFS) 

come si trova la funzione euristica?
- si tolgono alcuni vincoli per ottenere una soluzione ammissibile su un problema rilassato















## Da alberi a grafi
se il problema ha uno spazio ha grafo lo posso comunque esplorare ad albero, ripeterò l'esplorazione di alcuni nodi su cui sono già passato
...

lista dei nodi chiusi



consistenza

non necessariamente è necessaria la consistenza (vedi riespansione dei nodi della lista chiusa)
- confronta con Dijkstra






## Ricerca locale
approccio alternativo

...






## Altre tecniche euristiche
multipli nodi della frontiera hanno la stessa funzione di valutazione
- quale scegliere?
- non determinismo!
    - espandere un nodo, piuttosto che un altro può far trovare prima il goal
- capita anche negli esempi facili!

**NB**: conta anche per l'esame! In caso di parità dei nodi vengono fornite delle euristiche per ridurre il numero di espansioni