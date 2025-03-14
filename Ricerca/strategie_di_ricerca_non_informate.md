## Cosa significa cercare soluzioni?
L’idea è quella di mantenere ed estendere un insieme di sequenze/soluzioni parziali.
- Un agente con diverse opzioni immediate di esito sconosciuto può decidere cosa fare esaminando prima le differenti sequenze possibili di azioni che conducono a stati di esito conosciuto scegliendo, poi, quella migliore.
- Il processo di cercare tale sequenza è chiamato RICERCA.
- È utile pensare al processo di ricerca come la costruzione di un albero di ricerca i cui nodi sono stati e i cui rami sono operatori.

Una volta che viene trovata la soluzione, le azioni suggerite possono essere realizzate.
- Questa fase è chiamata ESECUZIONE ed è contrapposta alla fase di RICERCA.

Generare sequenze di azioni:
- **Espansione**: si parte da uno stato e applicando tutti gli operatori possibili (o la funzione successore) si generano nuovi stati. 
- **Operatore**: un'azione possibile disponibile da parte dell’agente. Equivalentemente, una funzione successore S(x) definita come come coppia \<azione, stato corrente>
- **Strategia di ricerca**: definisce quale dei nodi della frontiera scelgo per l'espansione

Come trovo il goal?
- **prima** scelgo il nodo da espandere (selezione mediante strategia di ricerca)
- **poi** scelgo se il nodo è goal o meno
- **come?** Applicando una funzione che mi dice si/no dato un nodo

Albero di ricerca: rappresenta l’espansione degli stati a partire dallo stato iniziale (la radice dell’albero).
- Le foglie dell'albero rappresentano gli stati da espandere.

**NB**: è evidente che bisogna scegliere una strategia di ricerca appropriata per trovare il nodo goal il prima possibile!
**NB**: siccome la struttura dati è ad albero, io posso fare avanti-indietro tra due nodi e questo si tradurrebbe in un ramo con profondità illimitata 






Struttura dati per l'albero di ricerca:
- ...
- in generale mantengo tutte le informazioni che mi permettono di costruire il percorso che mi dice come sono arrivato a quel nodo

frontiera: nodi possibili da espandere (foglie dell'albero)

...

complessità spaziale comincia ad impattare

...

### algoritmo generale di ricerca
sposto il problema dal decidere quale nodo della frontiera scegliere a (creando una coda) scegliere come ordinare la lista degli stati futuri (successor-FN())

interessante l'algoritmo generale parametrizzato con la strategia di ricerca 
- basta passare strategie di ricerca diverse per ottenere algoritmi di ricerca diversi (A*, greedy, ...)



Le stategie si valutano in base a quattro criteri: 
- **Completezza**: la strategia garantisce di trovare una soluzione quando ne esiste una?
- **Complessità temporale**: quanto tempo occorre per trovare una soluzione?
- **Complessità spaziale**: Quanta memoria occorre per effettuare la ricerca?
- **Ottimalità**: la strategia trova la soluzione di "qualità massima" quando ci sono più soluzioni?



### BFS
la frontiera diventa una coda FIFO
- queueing-FN mette i successori alla fine della CODA

Space is the big problem! mantengo in memoria tutti i nodi fino a che non trovo l'obiettivo O(b^d)
- con b = branching factor
- e d = profondità della soluzione

Si presta bene al parallelismo
- posso assegnare sotto alberi a computer diversi
- speedup lineare nel numero di computer
- se sono fortunato e trovo il goal prima anche sovra lineare

Garantisce complettezza e ottimalità (se il costo coincide con la profondità, altrimenti dovremmo utilizzare un'altra strategia che espande sempre il nodo a costo minimo -> strategia a costo uniforme)

**NB**: attenzione a quando espandi il goal!
- devi considerare l'ordine di entrata dei nodi nella coda
- non è che se è tutto allo stesso livello e vedo il goal posso selezionare direttamente il goal
- la regola della breadth-first è che espande prima i nodi a profondità minore, se ho più nodi alla stessa profondità posso scegliere un ordine aribtrario, **ma devo essere consistente**!



### Ricerca a costo uniforme
generalizzazione della BFS in cui non si considera la profondità (ovvero tutte le espansioni hanno costo 1) ma il costo del cammino per raggiungere un determinato nodo n (non è un'informazione euristica!)

**OSS**: anche se G è il goal non lo espande dato che B è più promettente. e faccio bene dato che trovo una soluzione ottimale.

non è tanto apprezzata...





### DFS
la frontiera diventa una coda LIFO
- queueing-FN mette i successori all'inizio della CODA

Esploro per primi i nodi più profondi sceglieno in maniera arbitraria tra quelli con uguale profonditò:
- posso liberare la memoria dei nodi appartenenti a rami morti (raggiunto le foglie senza trovare il goal)
- posso inloopparmi nei problemi che hanno uno spazio infinito (sequenza di mosse che si annullano)
    - a quanto pare è un problema comune

complessità temporame sempre esponenziale (d'altronde siamo sempre una strategia non informata)

**OSS sulla non informatarietà della strategia**: non posso sapere quale nodo mi conviene esplorare per prima, esploro tirando dritto in maniera ignorante anche fancedo della fatica inutile. Non c'è molta intelligeneza...





### Ricerca a profondità limitata
una combinazione di BFS e DFS che mira a combinare i vantaggi di entrambi
- completa e sviluppa un solo ramo alla volta (fino alla threshold)

Si prevede una PROFONDITÀ MASSIMA di ricerca (threshold). se raggiungo la threshold quel ramo non lo espando più
- DFS fino alla raggiungimento della profondità limite
- BFS della frontiera della profondità limite
- se ancora non trovo ricomincio con DFS di un nodo della frontiere di un livello precedente e così via

Chiaramente se mi fermo a profondità 17 e la soluzione è a profondità 18, non trovo la soluzione
- non trova sempre la soluzione



### Iterative deepening
Invece che scegliere una profondità limite fissa e fallire se la soluzione non si trova entro quella profondità, posso aggiornare iterativamente la profondità limite
- completa e sviluppa un solo ramo alla volta (fino alla threshold)
- ogni volta che aggiorno la threshold devo ripercorrere tutti i nodi che avevo già esplorato
    - bilancio la complessità spaziale con quella temporale