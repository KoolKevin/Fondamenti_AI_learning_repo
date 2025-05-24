Questa è una parte difficile da classificare
- riguarda sia aspetti di rappresentazione della conoscenza
- sia aspetti di ricerca nella spazio degli stati

La pianificazione automatica (planning) è una tipologia specifica di problem solving che consiste nel
- **sintetizzare una sequenza di azioni** che eseguite da un agente
- … a partire da uno **stato iniziale** del mondo…
- … provocano il raggiungimento di uno **stato desiderato**

Dati:
- uno stato iniziale
- un insieme di azioni eseguibili
- un obiettivo da raggiungere (goal)

Un problema di pianificazione consiste nel determinare un piano, ossia un **insieme parzialmente o totalmente ordinato** di azioni necessarie per raggiungere il goal.
- nota che l'ordine delle azioni è importante
- l'ordinamento parziale implica che ci possono essere piani alternativi (ovvero, sequenze di azioni distinte) per raggiungere lo stesso obiettivo che differiscono solo per l'ordine in cui le azioni vengono eseguite
- possono esistere piani alternativi però in cui semplicemente vengono compiute mosse diverse



### Rappresentazione dello stato
è necessario fornire al pianificatore un modello del sistema su cui opera.

In genere lo stato è rappresentato in forma dichiarativa con **una congiunzione di formule atomiche** che esprime una situazione.
- on(book,table) U name(book,xyz) U atHome(table)

Il goal si rappresenta come tutti gli altri stati 
- In questo caso la congiunzione rappresenta una descrizione parziale dello stato finale che si vuole raggiungere
- descrive solo le condizioni che devono essere verificate affinché il goal sia soddisfatto

Lo stato di un sistema spesso può essere osservato solo in modo parziale per una serie di motivi:
- perché alcuni aspetti non sono osservabili;
- perché il dominio è troppo vasto per essere rappresentato nella sua interezza (limitate capacità computazionali per la rappresentazione; catena di congiunzioni troppo lunga);
- perché le osservazioni sono soggette a rumore e quindi si hanno delle osservazioni parziali o imperfette;
- perché il dominio è troppo dinamico per consentire un aggiornamento continuo della rappresentazione.


### Rappresentazione dello azioni
È necessario fornire al pianificatore una descrizione formale delle azioni eseguibili detta Teoria del Dominio.

Ciascuna azione è identificata da un nome e **modellata in forma dichiarativa per mezzo di precondizioni e postcondizioni**.
- Le precondizioni rappresentano le condizioni che devono essere verificate affinché l’azione possa essere eseguita;
- le postcondizioni rappresentano gli effetti dell’azione stessa sul mondo.

A volte la Teoria del Dominio è costituita da **operatori con variabili** che definiscono classi di azioni. 
- a diverse istanziazioni delle variabili corrispondono diverse azioni.


**Esempi**:
Problema: spostare blocchi su un tavolo con un braccio

Azioni:
STACK(X,Y)
    SE: holding(X) and clear(Y)
    ALLORA: handempty and clear(X) and on(X,Y);

UNSTACK(X,Y)
    SE: handempty and clear(X) and on(X,Y)
    ALLORA: holding(X) and clear(Y);



### Classificazioni
**pianificazione classica**
E’ un tipo di pianificazione off-line che produce l’intero piano prima di eseguirlo lavorando su una rappresentazione istantanea (snapshot) dello stato corrente.

È basata su alcune assunzioni forti:
- tempo atomico di esecuzione delle azioni
- determinismo degli effetti
- stato iniziale completamente noto a priori
- esecuzione del piano unica causa di cambiamento del mondo

**pianificazione reattiva**
Metodo di pianificazione on-line
- considera l’ambiente non deterministico e dinamico
- è capace di osservare il mondo sia in fase di pianificazione sia in fase di esecuzione
- spesso alterna il processo di pianificazione a quello di esecuzione reagendo ai cambiamenti di stato



In questo corso consideriamo solo **Tecniche di Pianificazione Classica**:
- Planning Deduttivo
    - Situation Calculus
- Planning mediante ricerca
    - Ricerca nello spazio degli stati, ad es. Planning Lineare
        - STRIPS

(In intelligent systems anche altri tipi di planning)



## Planning Deduttivo
La tecnica di pianificazione deduttiva utilizza la logica per rappresentare stati, goal e azioni e **genera il piano come dimostrazione di un teorema**

### Situation calculus
Linguaggio di modellazione (estensione della FOL) in grado di rappresentare stati e azioni **in funzione del tempo**

Concetti fondamentali:
- **fluente**: una proprietà che può cambiare nel tempo 

- **Situation**: "fotografia" del mondo e delle proprietà (fluent) che valgono in un determinato istante/stato. 
    - Esempio:
        on(b,a,s0). 
        ontable(c,s0). 
        ontable(a,s0).
        clear(b,s0)
        clear(c,s0)
    - è uno stato corrente definito sotto forma di storico delle azioni che hanno portato a questo stato

- **Azioni**: definiscono quali fluent saranno veri come risultato di un’azione.
    - Esempio:
        on(X,Y,S) and clear(X,S) ->
            ontable(X, do(putOnTable(X), S)) and
            clear(Y, do(putOnTable(X), S))

Nota: si sta assumendo implicitamente la CWA

**Costruzione di un piano**: deduzione si traduce nella dimostrazione di un goal.
Esempio:    
    :- ontable(b,S).
    
Significa: esiste uno stato S in cui è vero ontable(b) ?
- YES per S=do(putOnTable(b), s0)

**NB**: che in questo esempio basta un'azione (s0 = atome che rappresenta lo stato iniziale); tuttavia, prolog è ricorsivo e quindi il piano si costruisce in un qualcosa del tipo:
- S = do(a3, do(a2, do(a1, s0)))
- abbiamo la lista delle azioni compiute per raggiungere ogni stato -> situation
- stiamo facendo fare a prolog tutto il lavoro tramite risoluzione!!!

Le azioni si esprimono con assiomi nella forme a clausole
Ad esempio, l’azione move(X,Y,Z)
- clear(X,S) and clear(Z,S) and on(X,Y,S) and diff(X,Z) ->
    clear(Y,do(move(X,Y,Z),S)), on(X,Z,do(move(X,Y,Z),S)).


Problema: frame problem...


### Frame problem
Occorre specificare esplicitamente tutti i fluent che cambiano dopo una transizione di stato e **anche quelli che NON cambiano** (assiomi dello sfondo: "Frame axioms").
- devo dire tutto ciò che l'azione fa (ragionevole) e tutto ciò che l'azione non fa (crazy)

Per descrivere un’azione occorre una descrizione completa dello stato risultante dall’esecuzione di ciascuna azione (effect axioms).
- effect axiom = una o più regole prolog che mi definiscono come viene modificato il mio stato in seguito ad un'azione 

Oltre agli effect axioms occorre specificare tutti i fluent che NON sono invalidati dall’azione stessa (frame axioms). 
- Nel nostro esempio occorrono i seguenti assiomi:
    - on(U,V,S) and diff(U,X) -> on(U,V,do(move(X,Y,Z),S))  % se non sto spostando un blocco esso rimane dov'era
    - clear(U,S) and diff(U,Z)-> clear(U,do(move(X,Y,Z),S)) % se non sto spostando sopra ad un blocco esso rimane clear

Occorre esplicitare un frame axiom per ogni relazione NON modificata dall'azione. Se il problema è complicato la complessità diventa inaccettabile

Al crescere della complessità del dominio il numero di tali assiomi cresce enormemente. Il problema della rappresentazione della conoscenza diventa intrattabile
 








## Pianificazione classica come ricerca
Gestisce la generazione del piano come un problema di ricerca.

Quello che cambia rispetto al planning deduttivo è la forma dello spazio di ricerca, definito da che cosa sono gli stati e gli operatori:
- Pianificazione deduttiva come dimostrazione di teoremi: stati come insiemi di formule e operatori come regole di inferenza
- Pianificazione nello spazio degli stati: stati come descrizioni di situazioni e operatori come modifiche dello stato

### Planning lineare
Un pianificatore lineare riformula il problema di pianificazione come problema di ricerca nello spazio degli stati e **utilizza le strategie di ricerca classiche**.

Si chiama lineare perchè la sequenza di azioni del piano è lineare

L’algoritmo di ricerca può essere:
- Forward: se la ricerca avviene in modo progressivo partendo dallo stato iniziale fino al raggiungimento di uno stato che soddisfa il goal.
- Backward: quando la ricerca è attuata in modo regressivo a partire dal goal fino a ridurre il goal in sottogoal soddisfatti dallo stato iniziale.



### Strips




Strips assumption per il frame problem
- hanno dovuto specificare gli effetti negativi ed effetti positivi
    - lista degli add e lista dei delete
    
In strips vale comunque la CWA


punto di non determinismo di STRIPS se ho a,b,c in che ordine rimetto dentro lo stack?
- regola di selezione
- problematico se i goal interagiscono

strips fa backtracking
- abbiamo un punto di scelta
- strips prova con un ordine e se non riesce fa backtracking



Anomalia di Sussman