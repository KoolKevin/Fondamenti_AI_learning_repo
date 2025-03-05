...

Strategia di ricerca == quale dei nodi della frontiera scelgo per l'espansione

- **prima** scelgo il nodo (selezione)
- **poi** scelgo se il nodo è goal o meno
- **come?** Applicando una funzione che mi dice si/no dato un nodo

Struttura dati per l'albero di ricerca:
- ...
- in generale mantengo tutte le informazioni che mi permettono di costruire il percorso che mi dice come sono arrivato a quel nodo

frontiera: nodi possibili da espandere (foglie dell'albero)

...

complessità spaziale comincia ad impattare

...

### algoritmo generale di ricerca
sposto il problema dal decidere quale nodo della frontiera scegliere a (creando una coda) scegliere come ordinare la lista

interessante l'algoritmo generale parametrizzato con la strategia di ricerca 
- basta passare strategie di ricerca diverse per ottenere algoritmi di ricerca diversi (A*, greedy, ...)


### BFS
coda FIFO

Space is the big problem! mantengo in memoria tutti i nodi fino a che non trovo l'obiettivo O(b^d)

Si presta bene al parallelismo
- speedup lineare nel numero di computer (se sono fortunato anche sovra lineare)

**NB**: attenzione a quando espandi il goal!
- devi considerare l'ordine di entrata dei nodi nella coda
- non è che se è tutto allo stesso livello e vedo il goal posso selezionare direttamente il goal
- la regola della breadth-first è che espande prima i nodi a profondità minore, se ho più nodi alla stessa profondità posso scegliere a caso



### Ricerca a costo uniforme
generalizzazione della BFS in cui non si considera la profondità (tutti i passaggi hanno costo 1) ma il costo del cammino

non è un'informazione euristica

**OSS**: anche se G è il goal non lo espande dato che B è più promettente.

non è tanto apprezzata...





### DFS
coda LIFO

**OSS sulla non informatarietà della strategia**: non posso sapere quale nodo mi conviene esplorare per prima, esploro tirando dritto in maniera ignorante anche fancedo della fatica inutile. Non c'è molta intelligeneza...

- posso liberare la memoria dei nodi che non mi servono più
- posso inloopparmi nei problemi che hanno uno spazio infinito (sequenza di mosse che si annullano)
    - a quanto pare è un problema comune



### Ricerca a profondità limitata
una combinazione di BFS e DFS che mira a combinare i vantaggi di entrambi

se raggiungo la threshold quel ramo non lo espando più
- chiaramente se mi fermo a profondità 17 e la soluzione è a profondità 18, non trovo la soluzione
- non trova sempre la soluzione



### Iterative deepening
- se aggiorno la threshold devo ripercorrere tutti i nodi che avevo già esplorato
    - bilancio la complessità spaziale con quella temporale