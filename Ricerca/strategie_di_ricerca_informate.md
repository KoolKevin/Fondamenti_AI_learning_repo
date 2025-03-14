conoscenza euristica sul dominio
- si traduce in una funzione di valutazione che stima un punteggio per tutti i nodi della frontiera in modo da capire quale conviene espandere per primo
- quanta fatica faccio per raggiungere il goal espandendo un determinato nodo
- tradeoff sul calcolo della funzione di valutazione e espansione con "forza bruta"

bisogna capire qual'è il nodo "più promettente"... come si fa? Ovvero come si definisce una funzione di valutazioni corretta?
- **anticipazione**: una funzione di valutazione che restituisce una distanza minore rispetto a quella reale per arrivare al goal ci piace! Euristica ottimistica



## Ricerca best first
Best-first significa scegliere come nodo da espandere per primo quello che sembra più desiderabile.
- Usa una **funzione di valutazione** che calcola un numero che rappresenta la desiderabilità relativa per l’espansione di un nodo.
- Cerca di muoversi verso il massimo/minimo di tale funzione che "stima" il costo per raggiungere il goal.
- **QueuingFn** inserirà i successori di un nodo espanso in ordine decrescente di desiderabilità.

**NB**: costruendo una QueuingFn che ordina i nodi della frontiera secondo la desiderabilità calcolata dalla funzione di valutazione si ottengono algoritmi di ricerca informati. Casi particolari in base alla funzione di valutazione adottata:
- ricerca greedy (golosa)
- ricerca A*



### Ricerca greedy best-first
Utilizza per la funzione di valutazione la distanza (stimata) di un nodo *n* dal goal.
- espande il nodo che sembra più vicino al goal (distanza euclidea della prossima città dalla destinazione).
- Non considera il costo per raggiungere il nodo n dallo stato iniziale.
- non è detto che trovi la soluzione migliore, ovvero il cammino migliore per arrivare alla soluzione (si pensi all'esempio del labirinto).

Funzione di valutazione f(n) = h(n)
- h(n) (euristica) = stima del costo da n al goal


### Ricerca A*
La ricerca Greedy mostra come sia necessario considerare anche il "costo" nel raggiungere il nodo n dalla radice.

Funzione di valutazione con due contributi:
- g(n): profondità del nodo (quanto ho speso fino ad ora)
- h'(n): distanza di n dal goal
- Scegliamo come nodo da espandere quello per cui questa somma è più piccola

**NB**: impara la notazione dell'esempio del filetto con A* (lo mette all'esame)
- tra parentesi si mette l'ordine di espansione dei nodi


**NB**: l'ottimalità di A* non è sempre garantita, dipende dalla funzione euristica

Si supponga di indicare con h(n) la vera distanza fra il nodo corrente e il goal.
- La funzione euristica h'(n) è **ottimistica** se abbiamo sempre che h'(n) <= h(n). Tale funzione euristica è chiamata **ammissibile**.

Teorema:
- Se h'(n) <= h(n) per ogni nodo, allora l'algoritmo A* troverà sempre il nodo goal ottimale (in caso di alberi TREE-SEARCH).
    - Ovviamente l'euristica perfetta h' = h è sempre ammissibile.
    - Se h' = 0 otteniamo sempre una funzione euristica ammissibile ma questo caso coincide con ricerca breadth-first (ovviamente la depth-first non lo sarà mai)

dimostrazione carina che convince che se l'euristica è ottimale, allora A* sceglie sempre il percorso migliore (ottimale)
- chiaramente eventualmente fa backtracking, però trova la soluzione ottima
- dire che l'euristica è ammissibile è equivalente a dire che A* trova l'ottimo



### FUnzioni euristiche 
Date due funzioni euristiche ammissibili è meglio scegliere quella con costo maggiore per ogni nodo n (ci si allontana da BFS)
- Una euristica che dà un valore più alto fornisce una guida più forte verso la soluzione, facendoti avvicinare più rapidamente all'obiettivo. In pratica:
    - Quando una euristica fornisce un valore più alto, significa che stai prendendo una decisione più "informata" rispetto a quale nodo espandere successivamente.
    - Questo significa che A* sarà più "diretto" nella sua ricerca, esplorando meno nodi irrilevanti rispetto a quella euristica che fornisce valori più bassi (anche se è comunque ammissibile). 

- Bilanciamento tra guida e apertura: La chiave per un buon funzionamento dell'algoritmo A* è trovare un buon bilanciamento tra la forza dell'euristica e la necessità di esplorare una varietà di rami. Se l'euristica è troppo "forte" e dirige troppo rapidamente la ricerca, può ridurre la diversità nella ricerca dei percorsi e far sì che A* si "concentri" troppo su rami potenzialmente sbagliati. Se l'euristica è troppo "debole", A* potrebbe espandere troppi nodi prima di trovare la soluzione.

come si trova la funzione euristica?
- si tolgono alcuni vincoli per ottenere una soluzione ottima su un problema rilassato (linea d'aria)
- massimo tra diverse euristiche

















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