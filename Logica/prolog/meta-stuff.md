## Meta-predicati
tutto è un termine (non capisco bene)

### meta-predicato call
aggiunge il termine T (che può essere qualsiasi cosa) in testa al risolvente attuale, l'interprete prolog continua pio la risoluzione

...

variabili meta-logiche? no grazie

### meta-predicato fail
fa fallire sempre la valutazione **attivando il backtracking**
- esempio interessante su constraint logic programming:
    - imponendo un fallimento posso chiedere un altra soluzione


esempio slide 10: applico il predicato q a tutti gli X che soddisfano p
- osserva che la write(X) non è backtrackabile

**interessante l'uso combinato di cut e fail per la gestione delle eccezioni (ragionamento a default)**
- tuttavia c'è un problema, prima di arrivare al default devo testare tutte le eccezioni (performance pessime)
- strutturazione controintuitiva, il caso di default dovrebbe essere il ramo più veloce


### meta-predicati setof, bagof e findall
consentono di rispondere a query con tutte le soluzioni e non con una singola soluzione alla volta 
- equivalente a digitare ; 


setof(X,P,S).
- S è **l'insieme** delle istanze X che soddisfano il goal P

bagof(X,P,L).
- L è la **lista** delle istanze X che soddisfano il goal P
    - In entrambi i casi, se non esistono X che soddisfano P i predicati falliscono

bagof produce una lista in cui possono essere contenute ripetizioni, setof produce una lista corrispondente ad un insieme in cui non ci sono ripetizioni…
- … spesso non implementato negli interpreti, per motivi di efficienza



sintassi (esclusiva per il setof e il bagof) per la quantificazione esistenziale ... no grazie

Noi useremo la stragrande maggioranza delle volte findall()




NB: interpreti diversi implementano questi predicati in maniera diversa






## Meta-interpreti

predicati dinamici
- non è una differenza logica è una differenza di implementazione
- un predicato statico è un predicato in scritto dentro al mio file .pl


boh, ... discorsi su rappresentazione di un programma prolog come una tabella in un db e indicizzamento


clause ...

assert ...

retract ...

**NB**: stiamo uscendo dal mondo logico e tornando nel mondo imperativo, con queste clausole stiamo interagendo direttamente con l'interprete prolog e gli stiamo chiedendo di fare roba 
- side effect 
- backtracking che non funziona più
- ordine dei predicati che comincia a contare

Esempio interessante: caching dei risultati parziali nel calcolo del numero di fibonacci




interessante siccome possiamo scrivere interpreti, possiamo anche modificarne il loro comportamento
- e.g. not fatto per ultimo in modo da cercare di sculare ed avere variabili ground













```Chiedi al prof reversibilità di no_dupl```