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

nota: in un certo senso simile a DFS in quanto va in profondità scegliendo ad ogni passo l'alternativa che sembra nell'immediato più vicina 


### Ricerca A*
La ricerca Greedy mostra come sia necessario considerare anche il "costo" nel raggiungere il nodo n dalla radice.

Funzione di valutazione con due contributi:
- g(n): profondità del nodo (quanto ho speso fino ad ora)
- h'(n): distanza di n dal goal
- Scegliamo come nodo da espandere quello per cui questa somma è più piccola

**NB**: combina i vantaggi di DFS (basso utilizzo di memoria) con quelli della ricerca a costo uniforme (ottimalità della soluzione)
- DFS: h'(n) mi guida in profondità verso l'obiettivo senza spazzare in ampiezza l'albero 
    - mi da un contributo che ad ogni decisione di espansione mi spinge ad espandere il nodo che sembra più vicini all'obiettivo
    - mi dà una **direzionalità**
- UCS: g(n) = costo del cammino dall'origine al nodo; identica a UCS
    - mi da un contributo che ad ogni decisione di espansione mi spinge ad espandere il nodo con costo cumulativo (distanza dall'origine) più basso
    - mi consente di accorgermi se sto esplorando una strada che **sembrava buona ma che si è rivelata più lunga di altre alternative**

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
Abbiamo assunto fin qui che lo spazio di ricerca sia un albero e non un grafo.
- Non è quindi possibile raggiungere lo stesso stato da strade diverse.
- Se ci sono più strade si procede di nuovo all’espansione dello stato come se fosse nuovo (loop che mi fa fare avanti e indietro).
- Non si tiene quindi traccia degli stati già considerati.

RIPETO: se il problema ha uno spazio ha grafo lo posso comunque esplorare ad albero, ripeterò l'esplorazione di alcuni nodi su cui sono già passato (magari anche entrando in loop, vedi DFS)

L'assunzione è ovviamente semplicistica, come si estendono gli algoritmi precedenti per trattare con i grafi?
- Si deve tenere memoria non solo dei nodi da espandere (nodi aperti) **ma anche dei nodi/stati già espansi** (nodi chiusi)
    - non ho più solo la lista dei nodi di frontiera ma anche la lista dei nodi chiusi

**A* su grafi e ottimalità**
- Se utilizziamo closed (lista dei nodi chiusi) solo per evitare l’espansione ulteriore dei nodi che hanno stati in essa contenuti, siamo relativamente efficienti, ma potremmo non trovare la strada migliore.
- Nel caso dei grafi diventa possibile trovare un nuovo percorso per raggiungere uno stato già espanso con costo minore!

Con una funzione euristica che da una stima troppo ottimista in alcuni nodi (B), C è espanso prima di trovare la strada alternativa che passa per A.

Nel caso dei grafi, per far si che A* continui a trovare la soluzione ottima, bisogna imporre un'ulteriore condizione sulla funzione euristica:

**Consistenza (o monotonicità)**:
una euristica è consistente se per ogni nodo n, ogni successore n' di n generato da ogni azione a, vale:
- h(n) = 0 se lo stato corrispondente coincide con il goal, altrimenti
- h(n) ≤ c(n,a,n') + h(n‘)
    - disuguaglianza triangolare
    - // posso arrivare ad n' con più azioni in generale

Con la monotonicità ogni nodo è raggiunto per la prima volta mediante la strada migliore e quindi può essere inserito nella lista dei nodi chiusi senza preoccupazioni.
- g(n) valuta sempre la distanza minima dello stato/nodo dal nodo di partenza.


Theorema: Se h(n) e’ consistente, A* usando GRAPH-SEARCH e’ ottimale
- inoltre, f(n) non decresce mai lungo un cammino (il costo dell'azione è sempre maggiore rispetto a quello della stima dell'euristica).


**OSS**: Nel caso in cui si utilizzi un’euristica ammissibile, ma non consistente per mantenere l’ottimalità l’algoritmo si complica inserendo in closed gli stati con il loro costo (g(n)) e riespandendo nuovi nodi n con stato già considerrato (e in closed) se sono stati raggiunti da strade a minor costo g(n).
- confronta con Dijkstra




## Algoritmi costruttivi e algoritmi di ricerca locale

## Ricerca locale
approccio alternativo

...



## Metaeuristiche




### Altre tecniche euristiche
multipli nodi della frontiera hanno la stessa funzione di valutazione
- quale scegliere?
- non determinismo!
    - espandere un nodo, piuttosto che un altro può far trovare prima il goal
- capita anche negli esempi facili!

**NB**: conta anche per l'esame! In caso di parità dei nodi vengono fornite delle euristiche per ridurre il numero di espansioni