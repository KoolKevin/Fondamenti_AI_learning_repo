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
STRIPS = Stanford Research Institute Problem Solving. Comprende: 
- Linguaggio per la rappresentazione di azioni con sintassi molto più semplice del Situation Calculus (meno espressività, più efficienza).
- Algoritmo specifico per la costruzione di piani.


**Linguaggio STRIPS**
- **Rappresentazione dello stato**
    - Insieme di fluent che valgono nello stato
    - Esempio: on(b,a), clear(b), clear(c), ontable(c)
- **Rappresentazione del goal**
    - Insieme di fluent (simile allo stato) con in aggiunta possibili variabili
    - Esempio: on(X,a)
- **Rappresentazione delle azioni** (3 liste di fluenti)
    - PRECONDIZIONI: fluent che devono essere veri per applicare l’azione
    - DELETE: fluent che diventano falsi come risultato dell’azione
    - ADD: fluent che diventano veri come risultato dell’azione

Esempio di azione
Move(X, Y, Z)
    Precondizioni: on(X,Y), clear(X), clear(Z)
    Delete List: clear(Z), on(X,Y)
    Add list: clear(Y), on(X,Z)

A volte ADD e DELETE list sono rappresentate come un'unica EFFECT list con atomi positivi e negativi
    Move(X, Y, Z)
    Precondizioni: on(X,Y), clear(X), clear(Z)
    Effect List: ¬clear(Z), ¬on(X,Y), clear(Y), on(X,Z)

**NB**: Frame problem risolto con la **Strips Assumption**
- Tutto ciò che non è specificato nella ADD e DELETE list resta immutato
- Non devo specificare più tutto quello che non cambia, mi basta definire gli effetti negativi e positivi della mia azione mediante le liste degli add e dei delete









### Ricerca in STRIPS | algoritmo
come al solito una ricerca non informata è impraticabile quando il numero di possibili stati e di regole è elevato. Occorrono delle euristiche per migliorare l’efficienza.

L'algoritmo di STRIPS
- Utilizza il linguaggio STRIPS precedentemente presentato con **regole precondizione -> azione**
- Planner lineare basato su **ricerca backward**
    - dal goal allo stato iniziale
- Assume che lo stato iniziale sia completamente noto (**CWA**)
- Utilizza due **strutture dati**:
    - stack di goal (congiunzioni)
    - descrizione S dello stato corrente
        - formato dall'insieme fluent correntemente veri

**Algoritmo**:
// S rappresenta lo stato corrente formato dall'insieme dei fluent veri in questo momento
//      ad esempio: {on(A, C), clear(A)}.
// All'inizio lo stato corrente è lo stato iniziale
//
// A Rappresenta una formula, che può essere:
//      un fluent (come on(A, C))
//      oppure una congiunzione di fluent: A = a₁ ∧ a₂ ∧ ... ∧ aₙ
// 
// Quindi, A è un goal complesso o semplice, che può essere:
//      già soddisfatto (A ∈ S) oppure
//      scomposto in sottogoal
//
// a:
//      Rappresenta un fluent; Esempi: at(robot, room1), clean(room2), has(key)
// È la forma elementare di un obiettivo o di un precondizione/effetto di un’azione. 


// l'algoritmo cerca di trovare le azioni che mi fanno raggiungere la
// congiunzione dei goal finali andando a ritroso
Inizializza stack con la congiunzione di goal finali
while (stack non è vuoto) do
    if top(stack)=A and theta(A) sottoinsieme di S  // si noti che A puo essere un and di goals o un atomo
        // i fluenti di A appartengono già allo stato corrente e quindi applico solo unificazione
        pop(A) ed esegui sost. theta sullo stack
    else if (top(stack) = a)
        // il fluente a non appartiene allo stato corrente, quindi
        // aggiungo la regola R che me lo aggiungerà non prima però
        // di aver eseguito le precondizione di R 
        // ricorda che le precondizioni sono semplicemente altri fluent
        // e quindi hanno la stessa forma di a
        seleziona regola R con a appartenente Addlist(R),
        pop(a), push(R), push(Precond(R));
    else if top(stack) = a1, a2, …, an
        // sto valutando una congiunzione di fluenti. Questa proviene da
        // una precondizione di una regola. (ADD e DELETE vengono applicate 
        // direttametne ad S)
        //
        // aggiungo i singoli fluenti della congiunzione uno alla volta
        // in modo che vengano processati dal caso sopra
        (*) push(a1), …, push(an)
    else if top(stack) = R
        // applico la regola aggiungendo ad S i fluent della lista di ADD
        // della regola e rimuovendo quelli della lista di DELETE
        pop(R) e applica R trasformando S

**(\*)NB**: si noti che l’ordine con cui i sottogoal vengono inseriti nello stack rappresenta un **punto di scelta non deterministica** (ordinamento parziale).
- la congiunzione rimane sullo stack e verrà riverificata dopo (provo tutte le combinazioni, vedi dopo)
- interacting goals

Considerazioni:
1. Il goal è la prima pila di obiettivi.
    - Suddividere il problema in sottoproblemi: ciascuno per un componente dell'obiettivo originale. 
    - **NB**: Tali sottoproblemi **possono interagire!**
2. Abbiamo tanti possibili ordini di soluzione.
3. Ad ogni passo del processo di risoluzione si cerca di risolvere il goal in cima alla pila.
    - Quando si ottiene una sequenza di azioni che lo soddisfa, la si applica alla descrizione corrente dello stato ottenendo una nuova descrizione.
4. Si cerca poi di soddisfare l'obiettivo che è in cima alla pila partendo dalla situazione prodotta dal soddisfacimento del primo obiettivo.
5. Il procedimento continua fino allo svuotamento della pila.
6. Quando in cima alla pila si incontra una congiunzione si verifica che tutte le sue componenti siano effettivamente soddisfatte nello stato attuale. Se una componente non è soddisfatta (problema dell’interazione tra goal è spiegato più avanti) si reinserisce nella pila e si continua.



```dov'è la ricerca e dov'è lo spazio degli stati?```
Nell'esempio da slide 39 a 41 si nota che lo spazio degli stati è definito dagli operatori che vengono applicati per ridurre un goal. La ricerca a questo punto è dettata quale mossa si sceglie di applicare per ridurre un goal, e dall'ordine con cui si sceglie di risolvere i goal facenti parte di una congiunzione.



**Alcuni problemi**
1. Grafo di ricerca molto vasto. 
    - Nell’esempio abbiamo visto un cammino ma in realtà ci sono varie alternative
    - Abbiamo delle diramazioni a causa di
        - scelte non deterministiche ordinamento dei goal
        - più operatori applicabili per ridurre un goal
    - soluzione: strategie euristiche
2. Problema dell’interazione tra goal
    - Quando due (o più) goal interagiscono ci possono essere problemi di interazione tra le due soluzioni in quanto l'ordine delle azioni diventa importante
    - Considera una congiunzione di due goal: G1 e G2. L’ordine in cui risolvi i goal cambia la fattibilità:
        - Magari, Se parti da G1, devi tornare indietro perché G2 è un prerequisito.
        - Se parti da G2, invece, tutto funziona.
    - possiamo avere poi dei piani in cui la sequenza di azioni che soddisfa G2 include delle azioni che disfano delle azioni compiuto nel piano per G1
        - **anomalia di Sussmann!**
        - scarsa efficenza del piano, se avessi scambiato l'ordine dei goal magari avremmo ottenuto nessun disfacimento e un piano più efficente

La soluzione di un goal (G1) può dipendere dalla soluzione di un altro (G2).
- Soluzione completa:
    - provare tutti gli ordinamenti dei goal e dei loro sottogoal.
- Soluzione pratica (Strips):
    - provare a risolverli indipendentemente
    - verificare che la soluzione funzioni
    - se non funziona, provare gli ordinamenti possibili uno alla volta attivando il backtracking nel punto di scelta evidenziato prima

