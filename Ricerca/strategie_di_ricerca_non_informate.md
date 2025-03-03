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

interessante l'algoritmo generale parametrizzato con la strategia di ricerca 
- basta passare strategie di ricerca diverse per ottenere algoritmi di ricerca diversi (A*, greedy, ...)


### Ricerca in ampiezza
Space is the big problem! mantengo in memoria tutti i nodi fino a che non trovo l'obiettivo O(b^d)