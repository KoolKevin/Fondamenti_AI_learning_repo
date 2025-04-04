Molti problemi di AI possono essere visti come problemi di soddisfacimento di vincoli.
- Obiettivo: trovare uno stato del problema che soddisfi un dato insieme di vincoli.
- esempi: 
    - problemi di scheduling con vincoli
    - problemi di ricerca operativa

Un CSP è definito da tra 3 insiemi:
- un insieme **finito** di variabili a cui assegnare dei valori
- un insieme di domini **finiti** di definizione delle variabili
- un insieme di vincoli sulle variabili
    - Un vincolo c(Xi1,Xi2,...Xik) tra k variabili è un sottoinsieme del prodotto cartesiano Di1 х Di2 х ... х Dik che specifica quali valori delle variabili sono compatibili con le altre.

Risolvere un CSP significa trovare una valore per tutte le variabili, ognuna che soddifi tutti i vincoli



### Risoluzione di CSP come ricerca nello spazio degli stati
- **stato** è definito da variabili Xi con valori presi dai domini Di
- **goal test** è un insieme di vincoli che specificano le combinazioni di valori permessi
- **operatori** possono essere assegnamenti di valori a variabili (labeling)

CSP come esplorazione di un albero con DFS
- Stato iniziale: assegnamento vuoto { }
- Funzione Successore: assegna un valore ad una variabile non ancora legata (in modo che sia legale con gli assegnamenti già fatti).
    - Fallisci se non esiste
- Goal test: l’assegnamento è completo (tutte le variabili sono legate).


**approccio naive**
Un possibile albero decisionale per un CSP si ottiene:
- (dopo aver stabilito un ordinamento per l'assegnamento delle variabili)
- facendo corrispondere ad ogni livello dell'albero l'assegnamento di una variabile
- ad ogni nodo corrisponde la scelta di un possibile valore da dare alla variabile corrispondente al livello del nodo stesso.
- Ogni foglia dell'albero rappresenterà quindi un assegnamento di valori a tutte le variabili.
    - Se tale assegnamento soddisfa tutti i vincoli, allora la foglia corrispondente rappresenterà una soluzione del problema,
    - altrimenti rappresenterà un fallimento.
- La ricerca di una soluzione è equivalente all'esplorazione dell'albero decisionale per trovare una foglia-soluzione.

Note:
- Schema identico per tutti i CSPs
- Profondità limitata a n se n sono le variabili.
    - possiamo usare depth-first search! (can we?)
- La strada è irrilevante. 
    - Ci interessa solo l'assegnamento valido di tutte le variabili non l'ordine degli assegnamenti
- Problema commutativo con d^n foglie (se d è la cardinalità dei domini)
    - **NB**: È evidente che la strategia di esplorazione dell'albero risulta di importanza fondamentale al fine di trovare una soluzione per un problema complesso in tempi ragionevolmente brevi (DFS scartato)