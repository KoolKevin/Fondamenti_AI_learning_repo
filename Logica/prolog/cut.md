Interagisco direttamente con il modello runtime di prolog facendo del pruning sull'albero SLD

### Controllo di un programma Prolog
Nel modello runtime prolog, abbiamo logicamente **due stack**:
- stack di esecuzione
    - contiene i record di attivazione delle varie clausole 
- stack di backtracking
    - contiene l’insieme dei punti di scelta.
    - ad ogni fase della valutazione contiene puntatori alle scelte aperte nelle fasi precedenti della dimostrazione.

**OSS**: in realtà è utilizzato un solo stack, con alternanza di stack frame e choice point;
- le linee rosse indicate rappresentano i choice point


L'effetto del cut è quello di rendere definitive alcune scelte fatte nel corso della valutazione dall'interprete Prolog, ossia quello di **eliminare alcuni choice point dallo stack di backtracking.**
- Il cut altera quindi il controllo del programma
- Effetto collaterale più importante: perdita di dichiaratività


Si consideri la clausola:
    p :- q1, q2,…, qi, !, qi+1, qi+2,…, qn.

L'effetto della valutazione del goal ! (cut) durante la dimostrazione del goal "p" è il seguente:
- tutte le scelte fatte nella valutazione dei goal q1, q2,..., qi E in quella del goal p, vengono rese definitive;
    - in altri termini, tutti i punti di scelta per tali goal vengono rimossi dallo stack di backtracking.
- Le alternative riguardanti i goal seguenti al cut non vengono modificate
- Se la valutazione di qi+1, qi+2,..., qn fallisce, fallisce tutta la valutazione di p. 
    - Infatti, anche se p o q1, q2,..., qi avessero punti di scelta questi sarebbero eliminati dal cut;
- Il cut taglia rami dell'albero SLD !!!
    - Pertanto il cut non può essere definito in modo dichiarativo (può tagliare eventuali soluzioni).

**NB**: il cut taglia solamente i punti di scelta relativi al goal, ed ai relativi sotto-goal, che riguardano il predicato in cui il cut compare. NON taglia nulla che riguarda i predicati **più in alto**.

**Occhio**: perdo la completezza di SLD nel (frammento delle clausole di horn)
- i predicati non rimangono più generativi/bidirezionali

Va usato con molta attenzione:
- il programma diventa decisamente più efficiente ...
- ma vengono anche tagliate possibili soluzioni

La perdita della dichiaratività è il maggiore svantaggio derivante dall'uso del "cut". Tuttavia il suo uso:
- è necessario per la correttezza di alcune classi di programmi (mutua esclusione di clausole)
- ed è utile per l'efficienza di altre classi di programmi.




### cut per imporre la mutua esclusione
- Il cut può essere utilizzato molto semplicemente per rendere deterministica la scelta tra due o più clausole alternative.

Esempio:
    p(X) :- a(X), b.
    p(X) :- c.

Si supponga che la condizione a(X) debba rendere le due clausole mutuamente esclusive per realizzare uno schema del tipo:
- if a(.) then b else c

Utilizzando il predicato predefinito CUT:
    p(X) :- a(X), !, b.
    p(X) :- c.

- Se a(X) è vera, viene valutato il cut che toglie il punto di scelta per p(X).
- Se invece a(X) fallisce, si innesca il backtracking prima che il cut venga eseguito.
- **il cut va inserito DOPO la condizione che determina la mutua esclusione**
- ATTENZIONE: la mancanza del cut rende il programma SCORRETTO
    - come già visto in vari nel capitolo delle liste, mancherebbe la mutua esclusione
    - ovvero, in p(X) :- c non per forza, si ha che a(X) è falso




Anche l'unificazione mi offre già un meccanismo di mutua esclusione
- posso forzare la non unificazione (\=)
- tuttavia, è una mutua esclusione meno generale rispetto al cut




### cut per efficienza
La presenza del "cut" rende in molti casi un programma ricorsivo deterministico e **consente l'applicazione dell'ottimizzazione della ricorsione tail**.
- Sebbene un predicato sia definito in modo tail ricorsivo, la presenza dei punti di scelta ritarda l’ottimizzazione della tail recursion
- con il cut i punti di scelta vengono eliminati e quindi si può ottimizzare



predicati builtin per la verifica del tipo di un termine


