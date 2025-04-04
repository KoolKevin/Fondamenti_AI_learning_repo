Dato un CSP esistono due possibili approcci per la sua risoluzione:
- uno basato sulle Tecniche di Consistenza
- e l'altro su Algoritmi di Propagazione.

Senza perdita di generalità ci riferiremo, nel seguito, a CSP su vincoli binari (vincoli cioè che coinvolgono due variabili).

Algoritmi di Propagazione: gia visti

**Tecniche di Consistenza**
- Basati sulla propagazione dei vincoli per derivare un problema più semplice di quello (completo) originale.
- Tipicamente, prima si applicano Tecniche di Consistenza e poi di Propagazione (oppure integrate durante la ricerca).



## Tecniche di consistenza
Aiutano a buttare via dei valori. Non mi trova necessariamente delle soluzioni ma aiuta le ricerche (FLA, ...) a trovare una soluzione con minor costo computazionale (meno rami da esplorare).

Differenza fondamentale:
al contrario degli algoritmi di propagazione che propagano i vincoli **in seguito a istanziazioni delle variabili**, le tecniche di consistenza riducono il problema originale eliminando dai domini delle variabili i valori che non possono comparire in una soluzione finale.
- non si basano sull'istanziazione delle variabili?
- Possono essere applicate staticamente oppure ad ogni passo di assegnamento (labeling) come potenti tecniche di propagazione per le variabili non ancora istanziate


Tutte le tecniche di consistenza sono basate su una rappresentazione del problema come una grafo di vincoli (Constraint Graph).
- **NB**: nei grafi i vincoli sembrano ad essere orientati ma in realtà stabiliscono solo il verso del ragionamento quando si applica il vincolo. In realtà le frecce sono due, in ambo le direzioni (nota anche l'ordine delle eliminazini/aggiunte nell'algoritmo)

### Node consistency
Un nodo di un grafo di vincoli è consistente se per ogni valore Xi appartenente Di il vincolo unario su Xi è soddisfatto.
- consistenza di grado 1
- banale, in sostanza bisogna ridurre i domini delle variabili con vincoli unari
- Un grafo è node consistent se tutti i suoi nodi sono consistenti.

### Arc consistency
un arco A(i,j) è consistente se **per ogni valore X** appartenente Di, esiste **almeno un valore Y** appartenente Dj tale che il vincolo tra i e j P(i,j) sia soddisfatto
- consistenza di grado 2
- per rendere arc consistent un grafo bisogna eliminare da i (nodo sorgente) i valori per cui non si riesce a trovare valori consistenti in j
    - ERRORE TIPICO ALL'ESAME: eliminare un valore della variabile nella destinazinoe e non nella sorgente


### Procedimento iterativo e raggiungimento della quiescenza (AC)
Ogni volta che rimuovo una valore dal dominio di una variabile per ottnere arc consistency, devo ricontrollare l'arc consistenza di tutte le altre variabili (considerate ora come sorgenti) con cui ho dei vincoli (tutti i nodi adiacenti nel grafo)
- può darsi che io abbia rimosso l'unico valore valido per un determinato valore di un altra variabile, che quindi va rimosso per avere arc-consistency
- questo procedimento deve essere ripetuto finché la rete non raggiunge una configurazione stabile -> **QUIESCENZA**

**NB**: l'ordine non conta

**Considerazioni**:
- negli esercizi, la prima iterazione conviene farla across all variables, per poi considerare le dipendenze in una seconda iterazione e cosi via
- FCA fa meno pruning di AC ma ha minor costo computazionale, per questo viene chiamato AC-1/2
- notare che AC non ha assegnato nessuna variabile prima del pruning 
- Chatgpt: Le tecniche di consistenza, come l'Arc Consistency 1 (AC-1), sono utilizzate nei problemi di soddisfacimento di vincoli (CSP) per ridurre i domini delle variabili eliminando valori che non possono far parte di alcuna soluzione valida. Tuttavia, l'applicazione di AC-1 e di altre forme di consistenza locale non garantisce l'eliminazione della necessità di backtracking durante la ricerca di una soluzione. Questo perché, anche dopo aver reso il problema arc-consistente, possono persistere combinazioni di valori tra variabili che soddisfano le restrizioni binarie ma non portano a una soluzione completa del CSP. In altre parole, l'arc-consistenza può ridurre il numero di valori da considerare, ma non elimina necessariamente tutte le incoerenze che potrebbero causare backtracking. Pertanto, è comune combinare tecniche di consistenza con algoritmi di ricerca come il backtracking per esplorare efficacemente lo spazio delle soluzioni.
- Il controllo della consistenza dell'arco può essere applicato sia prima della ricerca, come preprocessing per produrre un problema semplificato oppure come passo di propagazione (in analogia al look ahead) dopo ogni assegnamento di variabile: è spesso chiamato **Maintaining Arc Consistency** (MAC) in questo caso 



### Path consistency
Si parte da un grafo arc-consistente. Un cammino tra i nodi (i,j,k) è path consistent se, per ogni valore x app. Di, e y app. Dj (che rispettano la node e la arc-consistenza) esiste un valore z app. Dk che soddisfa i vincoli P(i,k) e P(k,j).
- Arc-consistency considera vincoli solo tra coppie, path-consistency considera consistenza di triple
- consistenza di grado 3


... altra roba che non mi interessa sulla k-consistenza


### CSP ed ottimizzazione
Un Constraint Optimization Problem (COP) è un Problema di Soddisfacimento di Vincoli in cui viene aggiunto un obiettivo. Un COP è quindi formalmente descrivibile come un CSP il cui scopo non è solo trovare una soluzione ammissibile, ma la soluzione ottima secondo un certo criterio di valutazione. 
- Dato un algoritmo generale in grado di risolvere qualsiasi CSP si può allora utilizzare tale algoritmo per risolvere anche qualsiasi COP. Infatti, dopo aver descritto il problema in termini di variabili, domini e vincoli, **basta aggiungere una variabile ulteriore che rappresenta la funzione obiettivo**.
- Ogni volta che si trova una soluzione al CSP viene aggiunto un nuovo vincolo che garantisce che ogni soluzione futura avrà un valore della funzione obiettivo migliore. Questo procedimento continua finché non sarà più possibile trovare alcuna soluzione.
- L'ultima soluzione trovata è la soluzione ottima.

**OSS**: nel mondo reale, tipicamente avremo più funzioni obiettivo da ottimizzare, tipicamente in conflitto tra di loro. Come fare?
- somma pesata delle funzioni obiettivo
- ... insomma, si combinano in qualche maniera