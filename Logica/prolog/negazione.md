Siamo portati a pensare con la CWA.
- se qualcosa non è conseguenza logica dei dati nel DB, allora possiamo inferire che è falsa

...


La CWA diventa problematica se si cerca di modellare un sistema dinamico che **evolve nel tempo**
- dato che qualcosa può essere vero fino ad oggi ma non essere più vero domani
- non sempre quindi la possiamo usare 
- soluzioni? tre valori di verità, ...





### Negazione per fallimento











### Risoluzione SLDNF

...

metto da parte il not e prima cerco di dimostrare senza, poi lo recupero e lo applico al risultato ottenuto. Tutto questo solo per robe ground?
- riciclo il codice SLD

...

la regola di selezione del prolog non è safe
- la realizzazione di SLDNF non corretta (già prolog non era completo)

- è safe solo se la roba è ground



### NAF, variabili e quantificatori

se ho delle variabili il tutto non è più safe dato che quest'ultime vengono quantificate in maniera opposta








la regola di selezione è problematica (non corretta) ma è semplice correggerla con i metainterpreti
- tuttavia rimediando creo problemi da altre parti (riordinamento del programma)




...




la regola di selezione non è safe per chiarezza di comunicazione con il programmatore.
- se non andasse in ordine il programmatore vedrebbe l'esecuzione delle clausole che ha scritto (pensandole in quel modo) in ordine ricombinato 