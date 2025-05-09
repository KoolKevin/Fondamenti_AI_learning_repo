in Prolog tutto è un **termine**, ricordiamo la definizione:
- tutti i dati vengono rappresentati come termini
    - atomi
    - variabili
    - termini composti ricorsivamente come funtori


In prolog tutto è un termine nel senso che anche i predicati sono termini per determinati operatori

Operatore **:-**
- non associativo
- binario (testa e corpo della clausola)


es.

sum(0,X,X).
sum(s(X),Y,s(Z)) :- sum(X,Y,Z).

diventa:

:-(sum(0,X,X),true).
:-(sum(s(X),Y,s(Z)), (sum(X,Y,Z))).

**NB**: Gli operatori sono predicati definiti con una particolare precedenza e associatività 






## Metapredicati
In Prolog, i metapredicati sono **predicati che prendono altri predicati come argomenti.**

In pratica, un metapredicato non lavora direttamente su dati normali (come numeri o stringhe), ma lavora su altri predicati o su chiamate a predicati.

descrivono:
- Esecuzione dinamica di predicati.
- Applicazione sistematica di predicati a strutture dati (liste, per esempio).
- Raccolta di risultati provenienti da predicati




### meta-predicato call
aggiunge il termine T (che può essere qualsiasi cosa) in testa al risolvente attuale, l'interprete prolog continua poi la risoluzione
- Il predicato call ha come argomento un predicato (termine non variabile e non numerico)

variabili meta-logiche? no grazie


**esempio if**:








### meta-predicato fail
fa fallire sempre la valutazione **attivando il backtracking**
- esempio interessante su constraint logic programming:
    - imponendo un fallimento posso chiedere un altra soluzione


esempio slide 10: applico il predicato q a tutti gli X che soddisfano p
- osserva che la write(X) non è backtrackabile

La combinazione !,fail è interessante ogni qual volta si voglia, all'interno di una delle clausole per una relazione p, generare un fallimento globale per p (e non soltanto un backtracking verso altre clausole per p).
- vedi esempio con la negazione 

**interessante l'uso combinato di cut e fail per la gestione delle eccezioni (ragionamento a default)**
- tuttavia c'è un problema, prima di arrivare al default devo testare tutte le eccezioni (performance pessime)
- strutturazione controintuitiva, il caso di default dovrebbe essere il ramo più veloce









### meta-predicati setof, bagof e findall
consentono di rispondere a query con tutte le soluzioni e non con una singola soluzione alla volta (esistenzialmente)
- equivalente a digitare ; 


setof(X,P,S).
- S è **l'insieme** delle istanze X che soddisfano il goal P

bagof(X,P,L).
- L è la **lista** delle istanze X che soddisfano il goal P

- X è il termine che voglio recuperare (può essere anche complesso)
- P è il predicato che voglio soddisfare (i cui termini possono essere anche diversi da X)
- S/L è il risultato

In entrambi i casi, se non esistono X che soddisfano P i predicati falliscono

bagof produce una lista in cui possono essere contenute ripetizioni, setof produce una lista corrispondente ad un insieme in cui non ci sono ripetizioni…
- … spesso non implementato negli interpreti, per motivi di efficienza


bagof e setof non funzionano come ci si aspetterebbe con predicati con arità > 1 (vedi esempio 'padre()')
- fissano un valore
- io voglio quantificazione esistenziale

Per ottenere la stessa semantica di setof e bagof con quantificazione esistenziale per la variabile non usata nel primo argomento esiste un predicato predefinito:
- findall(X,P,S)
- vero se S è la **lista** (non set) delle istanze X per cui la proprietà P è vera. 
- sintassi (esclusiva per il setof e il bagof) per la quantificazione esistenziale ... no grazie


Se non esiste alcun X per cui P è vera findall non fallisce, ma restituisce una lista vuota
- (errore in SICStusProlog e SWI Prolog se non esiste il predicato chiamato; lista vuota se esiste, ma non ci sono soluzioni)

Noi useremo la stragrande maggioranza delle volte findall()

**NB**: questi metapredicati che mi permettono di raccogliere risultati di un predicato in liste, sono utili se si vuole implementare una sorta di foreach
- basta passare la lista risultante ad un predicato ricorsivo che scorre tutti gli elementi





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