



### Risoluzione SLD
Dato:
- un programma logico P (insieme di clausole definite)
- e una clausola goal G0 (clausola Horn)

ad **ogni passo** di risoluzione si ricava, se esiste, un nuovo risolvente Gi+1 ottenuto dalla clausola goal del passo precedente Gi e da una **variante** di una clausola appartenente al programma P (Strategia linear-input)
- prendere varianti delle clausole del programma P è importante per evitare conflitti nei nomi delle variabili (non so cosa significa sta roba)

La Risoluzione SLD: 
- seleziona un atomo Am dal goal Gi secondo un determinato criterio (**funzione di selezione** o Selection rule)
- e lo unifica, se possibile, **con la testa** della clausola Ci attraverso la sostituzione Si più generale (**MOST GENERAL UNIFIER, MGU**)
    - **NB**: nella risoluzione normale non distinguiamo tra testa e corpo di una clausola; con le clausole di Horn possiamo considerare solo le teste e siamo completi (meno roba da considerare nice) 
- Il nuovo risolvente è ottenuto da Gi riscrivendo l’atomo selezionato con la parte destra della clausola Ci ed applicando la sostituzione Si.
    - **NB**: la sostituzione della testa con il corpo è una maniera più intuitiva di pensare alla risoluzione; stiamo eliminando il letterale testa (che ha unificato) trovato nel goal ed aggiungendo il corpo, questo corrisponde ad una sostituzione. 
- notare il **backward chaining**: partiamo dal goal (o meglio dai suoi atomi) e cerchiamo di arrivare alla contraddizione a ritroso 


Una **derivazione SLD** per un goal G0 dall'insieme di clausole definite P è **una sequenza** di:
- clausole goal G0, …, Gn
- **varianti** di clausole del programma C1, …, Cn
- sostituzioni MGU S1, …, Sn

Tali che Gi+1 è derivato da Gi e da Ci+1 attraverso la sostituzione Sn.
- La sequenza può essere anche infinita.

Esistono tre tipi di derivazioni:
1. successo, se per n finito Gn è uguale alla clausola vuota Gn = :-
2. fallimento finito: se per n finito non è più possibile derivare un nuovo risolvente da Gn e Gn non è uguale a :-
3. fallimento infinito: se è sempre possibile derivare nuovi risolventi tutti diversi dalla clausola vuota.
    - ricorda che la logica non è decidibile, se non c'è una risposta non è detto che la computazione termini


**Risultato delle computazioni in Prolog**
- eventuale successo
- legami per le variabili del goal G0, ottenuti componendo le sostituzioni MGU applicate
- i termini “ground” rappresentano i valori di ingresso al programma, mentre i termini variabili sono i destinatari dei valori di uscita.

Dato un programma logico P e un goal G0, una risposta per P U {G0} è una sostituzione per le variabili di G0.








### Strategia di Selezione e Ricerca
Nella risoluzione SLD così come è stata enunciata si hanno due forme di non determinismo:

1. La prima forma di non determinismo è legata alla selezione di un atomo Am del goal da unificare con la testa di una clausola, e viene risolta definendo una particolare regola di calcolo. 
    - La regola di calcolo influenza solo l'efficienza. Non influenza né la correttezza né la completezza del dimostratore.
    - Tuttavia regole di calcolo diverse influiscono sulla struttura dell'albero SLD per quanto riguarda sia l'ampiezza sia la profondità. Quindi, qualunque sia R
        - il numero di cammini di successo (se in numero finito) è lo stesso in tutti gli alberi SLD costruibili per P U {G0}.
        - **NB**: R influenza solo il numero di cammini di fallimento (finiti ed infiniti). Per questo motivo bisogna essere consci della regola di calcolo che si sta adottando durante la scrittura di un programma logico, altrimenti si rischia di introdurre dei cicli infiniti.
    - **Indipendenza dalla regola di calcolo**: 
        - Dato un programma logico P, l'insieme di successo di P non dipende dalla regola di calcolo utilizzata dallarisoluzione SLD.
        - **NB**: Tuttavia bisogna esserne coscienti per evitare di aggiungere strade di fallimento (anche infinite)
2. La seconda forma di non determinismo è legata alla scelta di quale clausola del programma P utilizzare in un passo di risoluzione (ne possono esistere molteplici unificabili), e viene risolta definendo una strategia di ricerca.
    - Questa forma di non determinismo implica che **possano esistere più soluzioni alternative per uno stesso goal**
        - in base all'ordine delle clausolo con cui si sceglie di unificare, possono essere prodotte soluzioni diverse
    - La risoluzione SLD, in quanto completa, deve essere in grado di generare tutte le possibili soluzioni e quindi deve considerare ad ogni passo di risoluzione tutte le possibili alternative.
    - La strategia di ricerca deve garantire questa completezza

**alberi SLD**
Una forma grafica utile per rappresentare la risoluzione SLD e questa forma di non determinismo sono gli alberi SLD. 

- Ad ogni ramo di un albero SLD corrisponde una derivazione SLD.
    - Ogni ramo che termina con il nodo vuoto (:-) rappresenta una derivazione SLD di successo.
- **La regola di calcolo influisce sulla struttura dell'albero** perquanto riguarda sia l'ampiezza sia la profondità.
    - Tuttavia non influisce su correttezza e completezza.
    - Quindi, qualunque sia R, il numero di cammini di successo (se in numero finito) è lo stesso in tutti gli alberi SLD costruibili per P U {G0} .
    - R influenza solo il numero di cammini di fallimento (finiti ed infiniti).



La realizzazione effettiva di un dimostratore basato sulla risoluzione SLD richiede la definizione non solo di una regola di calcolo, ma anche di una **strategia di ricerca che stabilisce una particolare modalità di esplorazione dell'albero SLD alla ricercadei rami di successo**.

Le modalità di esplorazione dell'albero più comuni sono:
- depth first
- breadth first

Entrambe le modalità implicano l'esistenza di un meccanismo di **backtracking per esplorare tutte le strade alternative** che corrispondono ai diversi nodi dell'albero.
- Nel caso di alberi SLD, attivare il “backtracking” implica che tutti i legami per le variabili determinati dal punto di “backtracking” in poi non devono essere più considerati.


**Per quanto riguarda la strategia di selezione, prolog adotta la strategia left-most, scegle di risolvere sempre l'atomo più a sinistra**







### Strategia di Selezione e Ricerca in PROLOG
Il linguaggio Prolog, adotta la **strategia in profondità con "backtracking"** perché può essere realizzata in modo efficiente attraverso un unico stack di goal.
- tale stack rappresenta il ramo che si sta esplorando e contiene opportuni riferimenti a rami alternativi da esplorare in caso di fallimento (punti di backtracking).

Per quello che riguarda la scelta fra nodi fratelli, sempre per motivi di efficenza, la strategia Prolog li **ordina seguendo l'ordine testuale delle clausole** che li hanno generati.
- **NB**: La strategia di ricerca adottata in Prolog è dunque **non completa**.
- possono crearsi dei loop infiniti anche se una soluzione esiste
- importante per il programmatore prolog tenere a mente questa cosa ed ordinare le clausole correttamente


**Riassumendo**:
- Dato un letterale G1 da risolvere, viene selezionata la prima clausola (secondo l’ordine delle clausole nel programma P) la cui testa è unificabile con G1.
- Nel caso vi siano più clausole la cui testa è unificabile con G1,la risoluzione di G1 viene considerata come un **punto di scelta** (choice point) nella dimostrazione.
- In caso di fallimento in un passo di dimostrazione, Prolog ritorna in backtracking all'ultimo punto di scelta in senso cronologico (il più recente), e seleziona la clausola successiva utilizzabile in quel punto per la dimostrazione.
- In pratica, durante la risoluzione prolog gestisce i punti di scelta con uno stack 
    - va in DFS e quindi aggiunge i punti di scelta in testa, in caso di backtracking fa un pop





**Ripetiamo**:
Prolog deve decidere una clausola tra quelle con cui può unificare 
- la scelta è quella dell'ordine con cui vengono scritte (ordine sintattico)
    - le soluzioni non cambiano (SLD corretto e completo) ma cambiamo l'ordine di esplorazione e magari evitiamo loop
    - ... **incompletezza implementativa** dovuta ai loop di DFS




**risposte multiple e curiosità della notazione**:
Possono esistere più sostituzioni di risposta per una “query”.
- Per richiedere ulteriori soluzioni è sufficiente forzare un fallimento nel ramo della soluzione corrente innescando il backtracking.
- Tale meccanismo porta ad espandere ulteriormente l'albero di dimostrazione SLD alla ricerca del prossimo cammino di successo.
- In Prolog standard tali soluzioni possono essere richieste mediante l'operatore “;“.


Il carattere ";" può essere interpretato come
- un operatore di disgiunzione che separa soluzioni alternative.
- all'interno di un programma Prolog per esprimere la disgiunzione
- la congiunzione si esprime con la ,









## Interpretazione procedurale (molto importante)
interpretazione informale che aiuta a prendere familiarità con la programmazione logica in Prolog


In prolog una procedura è un insieme di clausole di P le cui teste hanno lo stesso simbolo predicativo e lo stesso numero di argomenti (arità).
- Gli argomenti che compaiono nella testa della procedura possono essere visti come i **parametri formali**.
- Una “query” del tipo: :- p(t1,t2,...,tn). è la **chiamata della procedura p**.
    - Gli argomenti di p (ossia i termini t1,t2,...,tn) sono i **parametri attuali**.
- **NB**: se dentro una query (chiamata di procedura) specifico delle costanti, esse sono dei parametri di ingresso; al contrario, se specifico delle variabili, quest'ultime sono considerabili come parametri d'uscita  
    - L’unificazione è il meccanismo di passaggio dei parametri.
    - Non vi è alcuna differenza intrinseca tra parametri di ingresso e parametri di uscita (reversibilità).
    - Posso specificare in una query alcuni come costanti ed altri come variabili, ed in una query successiva posso fare l'opposto

in prolog la firma di un predicato è dettata da nome e arità del predicato
- non esiste il tipo degli argomenti
- tutte le **variabili sono a singolo assegnamento**.
    - Il loro valore è unico durante tutta la computazione e slegato solo quando si cerca una soluzione alternativa (“backtracking”).

Il corpo di una clausola può a sua volta essere visto come una **sequenza di chiamate** di procedure.
- Due clausole con le stesse teste corrispondono a due definizioni alternative del corpo di una procedura.




### Predicati builtin extra-logici
Al Prolog puro devono, tuttavia, essere aggiunte alcune caratteristiche per poter ottenere un linguaggio di programmazione utilizzabile nella pratica
- causano side effects