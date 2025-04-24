**recap**:
nelle logica (proposizionale) abbiamo dei simboli che possono assumere il valore di vero/falso in base all'interpretazione che li si da. A questo punto però bisognerebbe decidere qual'è l'interpretazione giusta da dare ai simboli, ma questo è un problema impossibile. Piuttosto, si preferisce partire da un insieme di fbf che si assumono per vere; ovvero, si considerano solo le interpretazioni che sono modelli. A questo punto ci si può chiedere se un ulteriore formula f è conseguenza logica dell'insieme iniziale; se lo è, tutti sono d'accordo.

Come faccio a dimostrare che f è conseguenza logica? Dimostrare **a livello sintattico** significa trovare una seguenza di fbf nella quale ciascuna: o è un assioma oppure è ricavabile dalle fbf precedenti **mediante una regola di inferenza**. Altrimenti dovremmo dimostrare che ogni modello dell'insieme di partenza è un modello anche per f.

In pratica come si dimostra la conseguenza logica anche nella logica del primo ordine (che è molto più complessa)? Robinson: Risoluzione anche per First order logic ragionando per refutazione e cercando di ricavare la clausola vuota (contraddizione) 




## Dimostrazioni in logica dei predicati del primo ordine
La logica dei predicati è un linguaggio più potente per esprimere KB
- (abbiamo variabili e quantificatori)

Vedremo la dimostrazione di teoremi basata su:
- Risoluzione (corretta e completa per clausole generali)
- Forward chaining (corretta e completa per clausole Horn) Usata nei Database deduttivi (DATALOG)
- Backward chaining (corretta e completa per clausole Horn) **Usata nella Programmazione Logica (PROLOG)**.



### trasformazione clausole
Per dimostrare algoritmicamente la conseguenza logica di una formula f da un insieme di assiomi di partenza, è bene trasformare f nella forma a clausole generali (congiunzione di disgiunzioni di letterali == insieme di formule con dentro or, in and tra di loro )  
- obiettivo finale: avere una formula con dentro solo degli and/or senza quantificatori/implicazione/ecc. tra le scatole

Una qualunque fbf della logica dei predicati si può trasformare in un insieme di clausole generali.
- vanno fatte in questo ordine (dimostrato da Robinson)

1. le variabili non dichiarate si assume che sono quantificati universalmente
...

fino ad ora abbiamo solo riscritto applicando le regole degli operatori logici 

7. skolemizzazione
ogni variabile quantificata esistenzialmente viene sostituita da una funzione delle variabili quantificate universalmente che la precedono. Tale funzione è detta funzione di Skolem. 
- i quantificatori esistenziali equivalgono a dire: "un tizio, esiste un tizio che"
- Skolem dice di sostituire il generico tizio con una costante (di Skolem) 
- tizio: funzione delle variabili quantificate universalmente (il tizio che fa lezione a me è diverso del tizio che fa lezione ad uno della 5.6)
- e quindi abbiamo varie costanti che rappresentano tizi: c1, c2, ...

**NB**: Siamo sicuri di aver mantenuto il significato della formula originale? NO, abbiamo fatto una specializzazione! siamo partiti da un quantificatore esistenziale e siamo arrivati ad tizio c1 specifico
- non ci cambia troppo se l'obiettivo è dimostrare l'insoddisfacibilità 
- teorema: Vale comunque la proprietà che F è insoddisfacibile se e solo se F’ è insoddisfacibile

8. ...

**NB**: Qualunque teoria del primo ordine T può essere trasformata in una teoria T’ in forma a clausole.
- Anche se T non è logicamente equivalente a T’ (a causa dell'introduzione delle funzioni di Skolem), vale comunque la seguente proprietà 
- teorema: Sia T una teoria del primo ordine e T’ una sua trasformazione in clausole. Allora T è insoddisfacibile se e solo se T’ è insoddisfacibile.
- Ricorda: T è ottenuto come assiomi + una formula negata ~F, se la teoria è insoddisfacibile allora F è conseguenza logica degli assiomi








## Unificazione
Per applicare la risoluzione ho bisogno di avere un simbolo (di costante) A da una parte e ~A dall'altra. Ma nella logica del primo ordine ho delle variabili! Per applicare il principio di risoluzione alle clausole non “ground” è necessario introdurre il concetto di unificazione.
- **Unificazione**: procedimento di manipolazione formale utilizzato per stabilire **quando due espressioni possono coincidere (A e ~A)** procedendo a opportune sostituzioni.
- **Sostituzione s**: insieme di legami di termini Ti a simboli di variabili Xi (i=1,..,n).
    - s = {X1/T1, X2/T2,...,Xn/Tn}
    - T1, ..., TN possono essere variabili come costanti come funzioni e non è detto che debba sostituire tutte le X dell'espressione
        - non ci sono vincoli

Data un'espressione E
- [E]s è detta istanza di E se almeno una variabile è stata sostituita da una costante.
• Renaming: sostituzioni che cambiano semplicemente il nome ad alcune delle variabili di E, [E]s è una variante di E.

**Sostituzione unificatrice**:
L’unificazione **rende identici due o più atomi** (o termini) (o meglio le loro istanze) attraverso un’opportuna sostituzione. 
- Un **insieme** di atomi (o termini) A1, A2 ,..., An è unificabile se esiste una sostituzione s tale che:
    - [A1]s = [A2]s = .... = [An]s. 
    - La sostituzione s è detta **sostituzione unificatrice** (o unificatore)

Se si considerano solo due atomi (o termini), uno dei quali senza alcuna variabile, si ricade in un caso particolare di unificazione, detto pattern-matching.
- l'unificazione può quindi essere considerata il caso generale del pattern matching
    - solo due termini, di cui uno è già definito
    - posso trasformare il termine non ground nella costante?
    - detta in un altro modo, la costante rispetta le regole del pattern?



**parentesi algoritmo di unificazione | caso costante vs termine composto**
Tu stai dicendo: "Non posso scegliere una X = c in modo che f(c) = a?"

Questo però non è valido in logica del primo ordine, perché:
- a e f(X) hanno natura diversa:
- a è un simbolo costante, tipo "rosso", "3", "marte"...
- f(X) è un termine composto, costruito applicando una funzione/simbolo di funtore (f) a un argomento.

Non esiste alcuna sostituzione che possa rendere f(X) identico a a, perché non c'è modo di smontare o trasformare a in f(c) – i simboli sono presi come "opachi", non si possono espandere o riscrivere.

🔍 Un'analogia:
Immagina che a sia una mela, e f(X) sia una "scatola con dentro qualcosa". Non puoi mai dire che una mela è uguale a una scatola contenente qualcosa, indipendentemente da cosa ci metti dentro la scatola.








### Most General Unifier
ogni volta che faccio una sostituzione più specifica perdo un po' di informazione (generalità). **Voglio unificare preservando la massima generalità possibile**. In altre parole, voglio trovare la **MGU** (Most General Unifier)
- completa generata al passo precedetente , la seconda clausola può essere uana qualunque 
- NB: se non trovo la MGU, potrei non riuscire a trovare la contraddizione, perchè perdo dell'informazione che magari mi serve dopo



**OCCUR CHECK**
- È il controllo che un termine variabile da unificare con un secondo termine non compaia in quest’ultimo. Necessario per assicurare la terminazione dell'algoritmo e la correttezza del procedimento di unificazione.
- I due termini "X" e "f(X)" non sono unificabili: non esiste una sostituzione per X che renda uguali i due termini.
- Se un termine t ha una struttura complessa, la verifica se X compare in t può essere anche molto inefficiente (costo computazionale elevato).
- Prolog NON utilizza l’occur-check per questo motivo








## Il principio di Risoluzione per le clausole generali
Siano C1 e C2 due clausole del tipo:
- C1 = A1 v ... v An, C2 = B1 v ... v Bm
- dove Ai (i=1..n) e Bj (j=1..m) sono atomi positivi o negativi (letterali) in cui possono comparire variabili.

Se esistono due letterali Ai e Bj tali che [Ai]s = [~Bj]s , dove s è la MGU, allora si può derivare una nuova
clausola C3 (il risolvente):
- [A1 v ... v Ai-1 v Ai+1 v ... v An v B1 ... Bj-1 v Bj+1 v ... v Bm]s
- Date due clausole C1 e C2, il loro **risolvente C3 è conseguenza logica di C1 U C2**
    - di conseguenza può essere aggiunto alla teoria
    - **NB**: la sostituzione unificatrice va applicata anche a C3

in sostanza uguale a prima ma dobbiamo applicare l'unificazione
- ricorda di applicare la sostituzione anche al risolvente



### Correttezza e completezza della risoluzione
Si può dimostrare che sotto opportune strategie di scelta delle clausole da risolvere, la risoluzione è corretta e completa.

**Teorema**: Un insieme di clausole è insoddisfacibile se e solo se l'algoritmo di risoluzione termina con successo in un numero finito di passi, generando la clausola vuota.
- insomma possiamo fare affidamente  la risoluzione 





### Strategie per la scelta dei risolventi
**OSS:** Il metodo di risoluzione procede esaustivamente generando tutti i possibili risolventi ad ogni passo.
- **esplosione combinatoria**: devo considerare ad ogni iterazione tutte le combinazioni di due clausole su cui posso applicare la risoluzione

Per motivi di efficienza è opportuno adottare delle **strategie**!
- quanti e quali risolventi scelgo se ve ne sono possibili molteplici?
- io voglio scegliere quello che mi fa arrivare prima alla contraddizione




**esempio con Socrate**:
nota: ricordiamo che dimostrato il teorema, a questo punto ce ne possiamo fregare di che cosa significano uomo() e mortale()! Siamo sicuri che qualunque interpretazione che è un modello per gli assiomi mi rende valido anche il teorema

Robinson diceva di esaminare tutte le coppie, grazie...
- come si fa?
- l'essere umano fa ad occhio! ma una macchina?

**Esistono delle stratgie!**
- **strategia lineare (completa)**: risolvo considerando sempre l'ultima clausola generata al passo precedente, la seconda clausola può essere una qualunque 
    - esempio del cane e gatto
    - **una sorta di DFS**
    - spesso conviene 
    - **completa**

Robinson correttezza e completezza ...






### Strategie non complete
le strategie complete sono costose. Sia in termini computazionali che di memoria (devo mantenere tutte le clausole generate nei passi precedenti)

**linear input**: 
- simile a lineare ma la clausola "libera"  viene sempre scelta tra quelle dell'insieme base
- utilizzata da prolog

**vantaggio**: memorizzo solo l'ultimo risolvente (e le clausole di base)    
**non completa**! corro il rischio di non riuscire a dimostrare qualcosa anche se quel qualcosa era conseguenza logica

**NB**: ma se mi riduco ad un sottoinsieme di clausole la linear input però diventa completa!
- clausole di Horn
- che prezzo pago però? 
- cosa non riesco ad esprimere con le clausole di Horn?





## Clausole di Horn (o definite)
La logica a clausole di Horn è un sottoinsieme della logica a clausole
```Le clausole di Horn hanno al più un letterale positivo```

nella vita reale le clausole di Horn non escludono formule logiche che sono interessanti
- il prezzo non è troppo alto!

Risoluzione per le clausole di Horn:
- risoluzione SLD resolution with:
    - Selection rule: Si sceglie solo un atomo alla volta da risolvere
        - In un goal come:  ?- padre(X, Y), madre(Y, Z).
        - ci sono due atomi da soddisfare: padre(X, Y) e madre(Y, Z)
        - "Risolvere un atomo alla volta" significa che:
            - si sceglie il primo atomo da risolvere (padre(X, Y)),
            - si cerca una clausola nella base di conoscenza che può farci derivare padre(X, Y) (cioè un fatto o una regola con una testa unificabile),
            - si applica l’unificazione, si sostituiscono le variabili, e si genera un nuovo goal con l’atomo risolto eliminato (o sostituito con il corpo della regola, se era una regola).
            - Solo dopo si passa al prossimo atomo, aggiornando le variabili con le sostituzioni ottenute finora. 
    - Linear input strategy
    - for Definite clauses: clausole di Horn
- Risoluzione SLD opera per contraddizione e quindi si procede negando la formula F da dimostrare.
- Poiché F è una congiunzione di formule atomiche quantificate esistenzialmente, la sua negazione produrrà una disgiunzione di formule atomiche negate quantificata universalmente, cioè una **clausola di Horn goal**.



In this paper, we shall avoid the awkwardness of the clausal definition of subset by concentrating attention on clauses which contain **at the most one conclusion**. Such clauses, called Horn clauses, can be further classified into four kinds:
- **assertions**:               B <-
- **procedure declarations**:   B <- A1, ..., An
- **denials**:                    <- A1, ..., An
- **and contradiction**:          <-









Due casi particolari di risoluzione:

**Formard Chaining**
- bottom-up 
- parto dai fatti ed arrivo al goal

**Backward Chaining**
- top-down
- parto dal goal ed arrivo ai fatti






Esempio:
...

studente di ingegneria non è sufficiente a dire che uno studia ad ingegneria bisogna rappresentare entrambe le cose

negli esercizi è bene mettere le clausole a cui ho applicato la risoluzione all'inizio (c9 = c5+c8)


or esclusivo difficile
- conviene rappresentarlo come congiunzione di disgiunzioni (forma a clausole)