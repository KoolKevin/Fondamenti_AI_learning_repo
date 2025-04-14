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
- L’unificazione rende identici due o più atomi (o termini) (o meglio le loro istanze) attraverso un’opportuna sostituzione.
- Se si considerano solo due atomi (o termini), uno dei quali senza alcuna variabile, si ricade in un caso particolare di unificazione, detto pattern-matching. 
- Un insieme di atomi (o termini) A1, A2 ,..., An è unificabile se esiste una sostituzione s tale che: [A1]s = [A2]s = .... = [An]s. 
- La sostituzione s è detta sostituzione unificatrice (o unificatore)

**NB**: ogni volta che faccio una sostituzione più specifica perdo un po' di informazione (generalità). **Voglio unificare preservando la massima generalità possibile**. In altre parole, voglio trovare la **MGU** (Most General Unifier)
- Sotto-NB: se trovo la MGU, potrei non riuscire a trovare la contraddizione, perchè perdo dell'informazione che magari mi serve dopo



**OCCUR CHECK**
- È il controllo che un termine variabile da unificare con un secondo termine non compaia in quest’ultimo. Necessario per assicurare la terminazione dell'algoritmo e la correttezza del procedimento di unificazione.
- I due termini "X" e "f(X)" non sono unificabili: non esiste una sostituzione per X che renda uguali i due termini.
- Se un termine t ha una struttura complessa, la verifica se X compare in t può essere anche molto inefficiente (costo computazionale elevato).
- Prolog NON utilizza l’occur-check per questo motivo








## Il principio di risoluzione per le clausole generali
...

in sostanza uguale a prima ma dobbiamo applicare l'unificazione
- ricorda di applicare la sostituzione anche alla risolvente




**Regola di inferenza**
[mettici l'immagine]



### Strategie per la scelta dei risolventi
quanti e quali risolventi scelgo se ve ne sono possibili molteplici?
- io voglio scegliere quello che mi fa arrivare prima alla contraddizione

inoltre se le clausole sono molteplici, ho il problema anche di scegliere quali coppie di clausole risolvere?

**esempio con Socrate**:
nota: ricordiamo che dimostrato il teorema, a questo punto ce ne possiamo fregare di che cosa significano uomo() e mortale()! Siamo sicuri che qualunque interpretazione che è un modello per gli assiomi mi rende valido anche il teorema

Robinson diceva di esaminare tutte le coppie, grazie...
- come si fa?
- l'essere umano fa ad occhio! ma una macchina?

**Esistono delle stratgie!**
- **strategia lineare**: risolvo considerando sempre l'ultima clausola 
    - esempio del cane e gatto
    - una sorta di DFS
    - spesso conviene 
    - **completa**

Robinson correttezza e completezza ...


### Strategie non complete
le strategie complete sono costose

- **linear input**: 
    - simile a lineare ma sceglie sempre una clasuola a partire dall'insieme base
    - utilizzata da prolog
    
**non completa**! corro il rischio di non riuscire a dimostrare qualcosa anche se quel qualcosa era conseguenza logica

ma se mi riduco ad un sottoinsieme di clausole la linear input però diventa completa!
- clausole di Horn
- che prezzo pago però? 
- cosa non riesco ad esprimere con le clausole di Horn?





## Clausole di Horn (o definite)
...

nella vita reale le clausole di Horn non escludono formule logiche che sono interessanti
- il prezzo non è troppo alto!

...

Applichiamo risulozione con linear input

...

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