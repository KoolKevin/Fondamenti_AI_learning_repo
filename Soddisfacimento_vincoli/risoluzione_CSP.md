Consideriamo una ricerca depth-first in un albero decisionale. Si tende a scendere di livello nell'albero fino a quando:
- o si sono assegnate tutte le variabili
    - e quindi si è trovata una soluzione,
- oppure non è più possibile trovare un valore 
    - la sequenza corrente non può portare a una soluzione ammissibile (vincoli sempre violati);
    - quindi si esegue un'altra scelta sull'ultima variabile della sequenza stessa.

L'algoritmo ha tre gradi di libertà:
- la scelta nell'ordinamento delle variabili;
- la scelta nell'ordine di selezione del valore da attribuire alla variabile corrente;
- **la propagazione effettuata in ciascun nodo**. 

I primi due riguardano le euristiche sulla strategia di ricerca. Il terzo c'è da capire cosa significa ma è ciò che differenzia le varie strategie di ricerca!



## Algoritmi generativi:
Si basano su **check dei vincoli a posteriori**

**Generate & test**
- molto semplice: genero una soluzione esplorando in profondità un ramo dell'albero e verifico se rispetta i vincoli
    - se si -> ho trovato una soluzione
    - se no -> riprovo con un altro ramo
    - non necessariamente devo esplorare tutto l'albero in larghezza, ma almeno una soluzione la devo generare e quindi in profondità si
- Inefficienza di base: i vincoli sono utilizzati per limitare lo spazio delle soluzioni **dopo** che la ricerca è stata effettuata, quindi a posteriori
- sembra stupido ma in realtà in alcune situazioni è una buona soluzione

**Standard backtracking**
- A ogni istanziazione di una variabile si preoccupa di verificare la coerenza della variabile appena istanziata con quelle assegnate **precedentemente**.
    - l'utilizzo dei vincoli è più efficace del precedente perché non si prosegue la ricerca in rami che, ai primi livelli dell'albero, presentano delle contraddizioni
- I vincoli sono utilizzati **all'indietro**
    - ovvero si controllano solo le variabili già assegnate 
- questo porta a una effettiva riduzione dello spazio di ricerca.
- Tuttavia, questa riduzione viene fatta a posteriori, cioè dopo aver effettuato il tentativo. Questo può portare all'esplorazione di lunghi rami che solo alla fine si rivelano morti
    - conseguente lungo backtracking
- La ricerca procede anche nel caso in cui una variabile ancora libera (magari in fondo nella coda di quelle da assegnare), non presenta più posizioni disponibili.


**Limiti dell’uso A Posteriori dei Vincoli**
- Il problema appena visto nello standard backtracking è un difetto da attribuire a tutti i metodi che utilizzano i vincoli passivamente, cioè posteriormente ad un tentativo di istanziazione.
- **Utilizzando anche i vincoli che coinvolgono variabili ancora libere** il problema sarebbe stato rilevato in anticipo evitando così costosi
backtracking.

- posteriori: considero i vincoli delle variabili assegnate
- priori: considero i vincoli di tutte le variabili (anche prima del loro assegnamento) 


### Algoritmi di propagazione
Cosa significa propagare i vincoli? 
- check dei vincoli a priori

L'idea che sta alla base degli algoritmi di propagazione consiste in un utilizzo attivo dei vincoli nella guida del pruning a priori dell'albero decisionale associando, **a ciascuna variabile** (anche quelle libere), l'insieme di valori ammissibili rimanenti dopo ogni assegnazione.
- Questi insiemi (domini) vengono perciò ridotti nel corso della computazione permettendo di scegliere per le variabili ancora libere valori ammissibili con le variabili già istanziate senza più considerare i vincoli che le legano (sono rimasti solo i valori validi)
- utilizzare le relazioni tra le variabili del problema, i vincoli, per ridurre lo spazio di ricerca **prima di arrivare al fallimento**.
    - La propagazione ha l’effetto di ridurre i domini delle variabili future (se un dominio risulta vuoto, fallimento)
    - Vengono così eliminati rami dell'albero che porterebbero ad un sicuro insuccesso limitando (inutili) backtracking.
    - si cerca di prevenire il fallimento piuttosto che rimediarlo (può comunque succedere, in quel caso backtracking)


**Forward checking**
Viene utilizzata, **dopo ogni assegnamento**, la propagazione dei vincoli che consiste nell'eliminazione dei valori incompatibili con quello appena
istanziato dai domini delle variabili **non ancora istanziate**.
- Se il dominio associato ad una variabile libera presenta un solo valore l'assegnamento può essere effettuato senza sforzo computazionale.
- Se ad un certo punto ci si accorge che un dominio associato risulta vuoto, **il meccanismo del Forward Checking fallisce** e fa backtracking.

**NB**: L'assegnazione di un valore ad una variabile ha ripercussioni sull'insieme dei valori disponibili per le variabili ancora libere.
- In questo modo i vincoli agiscono in avanti (forward) e limitano lo spazio delle soluzioni prima che vengano effettuati tentativi su di esso.
- In standard backtracking i vincoli agivano all'indietro in quanto bisognava controllare se un assegnamento fosse concorde con le variabili già assegnate
    - In FC questo è sempre vero in quanto i valori che rimangono sono sempre validi

**NMB**: 
Il forward checking sembra molto meglio rispetto a standard backtracking. Il problema è che ogni volta che assegno un valore ad una variabile vado a scorrere tutte le mie variabili "adiacenti" (quelle con cui ho dei vincoli) e per ognuna di queste tutti i valore del suo dominio per controllare i miei vincoli. **Il costo computazionale del backtracking si è spostato nella propagazione dei vincoli**
- ESAME: a volte nell'esame ci sono i pasti gratis



**Partial & full look-ahead**
Ad ogni istanziazione viene garantita, come per il Forward Checking, la compatibilità dei vincoli contenenti la variabile appena assegnata
con le precedenti (istanziate) e le successive (libere). **In più viene sviluppato il look ahead**, che controlla l'esistenza, nei domini associati alle variabili ancora libere, di valori compatibili con i vincoli contenenti solo variabili non istanziate.

In FC, la propagazione dei vincoli mi faceva rimanere nelle variabili non istanziate dei valori sicuramente validi con i vincoli delle variabili istanziate.
Tuttavia, non c'è alcun controllo sui vincoli tra le variabili non istanziate. 
- **Il backtracking avveniva quando i valori rimanenti di quest'ultime non erano compatibili**

I domini associati a ogni variabile vengono ridotti propagando anche le relazioni contenenti **coppie** di variabili non istanziate.
- In altre parole, nei domini delle variabili libere vengono eliminati dai valori rimanenti dopo la propagazione stile FC, anche quei valori non compatibili secondo i vincoli tra le coppie di variabili libere 
    - e.g. per ogni valore in D1 se esiste almeno un valore in D2 e almeno un valore in D3 compatibili (sono eliminati i valori di D1 per i quali non esiste alcun valore compatibile in D2 e in D3).
- Viene verificata quindi la possibilità di una futura assegnazione consistente fra le coppie di variabili libere.

**Strategia di Partial Look Ahead (PLA) o Full Look Ahead (FLA)**
Supponiamo venga assegnata la variabile Xk.
- **PLA**:
    - Per ogni variabile Xh non ancora istanziata si ha una propagazione dei vincoli contenenti la variabile Xh e le variabili "future", ossia le variabili Xh+1,..., Xn
    - Per ogni variabile non ancora assegnata Xk+1,.....,Xn, deve esistere un valore per il quale sia possibile trovare, **per tutte le altre variabili "successive"** non ancora assegnate, almeno un valore compatibile con esso.

- **FLA**:
    - se Vk è il valore appena assegnato alla variabile Xk, si ha una propagazione dei vincoli contenenti la variabile Xh, non ancora istanziata, e tutte le variabili non ancora assegnate, ossia le variabili Xk+1,...Xh-1,Xh+1..,Xn.
    - per ogni variabile non ancora assegnata Xk+1,....,Xn deve esistere un valore per il quale sia possibile trovare, per **tutte le variabili non ancora assegnate**, almeno un valore compatibile con esso
    - chiaramente, FLA elimina più soluzioni sbagliate rispetto a PLA in quanto controlla più vincoli, e quindi possiamo (quasi) dire che ciò che rimane è una soluzione. Questo però, come sempre, a scapito di un costo computazionale maggiore!

Nota: utile vedere l'esempio a slide 52. Notare come i LA vengono calcolati considerando solo **coppie** di variabili non assegnate e non l'interezza

**NB**: anche qua posso fallire con domini non vuoti, e quindi fare backtracking dato che considero solo coppie di variabili libere e non il loro insieme 

Il carico computazionale dovuto alle continue verifiche della consistenza dei vincoli, e quindi alla propagazione piuttosto pesante, non porta al raggiungimento di vantaggi quando le dimensioni del problema diventano considerevoli ai primi livelli dell'albero.
- Nell'esempio delle otto regine infatti i domini ridotti, dopo le prime due istanziazioni, dalle tecniche in esame sono identici ma, mentre il Look Ahead verifica la consistenza dei vincoli su tutte le coppie di variabili ancora libere (la maggioranza), il Forward Checking esegue molte meno verifiche guadagnando in efficienza.



## Euristiche
Sono rimasti gli altri due gradi di libertà!
- La scelta dell'ordinamento delle variabili e la scelta dell'ordine di selezione dei valori rimangono a disposizione del programmatore.
- Le euristiche potranno agire quindi su questi due gradi di libertà per cercare di garantire il raggiungimento di una buona soluzione in tempi ragionevoli anche per i problemi più complessi.

Le euristiche possono essere classificate in:
- **euristiche per la selezione della variabile**:
    - determinano quale deve essere la prossima variabile da istanziare. 
    - Le due euristiche più comunemente usate sono
        - il **first-fail** (o MRV: Minimum Remaing Values): che scegliere la variabile con il dominio di cardinalità minore
        - e il **most-constrained principle**: che sceglie la variabile legata a più vincoli.
        - Entrambe queste euristiche decidono di istanziare prima le variabili più difficili da assegnare.
            - ha senso, sono quelle che causerebbero più backtracking e quindi più tempo perso
- **euristiche per la selezione del valore**:
    - determinano quale valore assegnare alla variabile selezionata.
    - **Least constraining Principle**: Si segue in genere il principio di scegliere prima il valore che si ritiene abbia più probabilità di successo .

Un’ulteriore classificazione è la seguente:
- **Euristiche statiche**: determinano l'ordine in cui le variabili (o i valori) vengono scelti prima di iniziare la ricerca; tale ordine rimane invariato durante tutta la ricerca.
- **Euristiche dinamiche**: scelgono la prossima selezione da effettuare ogni volta che una nuova selezione viene richiesta (quindi ad ogni passo di labeling).
    - quelle viste sopra sono dinamiche

**NB**: Le euristiche dinamiche sono potenzialmente migliori (meno backtracking). Tuttavia, la determinazione dell'euristica perfetta (che non richiede backtracking) è un problema che ha, in genere, la stessa complessità del problema originale. Bisognerà quindi trovare un compromesso