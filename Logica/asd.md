### Il ragionamento e la Logica

**Cos'è il ragionamento?** Il ragionamento è il processo mentale con cui si **trae una conclusione a partire da certe premesse** o informazioni.
- È un’attività dinamica e può essere corretta o sbagliata.
- Serve per risolvere problemi, prendere decisioni, **trarre inferenze**.
- Può avvenire in diversi modi: deduttivo, induttivo, abduttivo, per analogia, ecc.
- È come il “motore” che lavora con ciò che sai per arrivare a ciò che non sai (o credi di sapere).

**Cos'è la logica?** La logica è il sistema formale (insieme di regole) che **definisce quando un ragionamento è corretto**.
- Si occupa della struttura degli argomenti, non del contenuto.
- Può essere formale (logica proposizionale, predicativa) o informale (logica del linguaggio naturale).
- È usata per valutare se la conclusione segue logicamente dalle premesse.
- **La logica è la “grammatica” del ragionamento**: stabilisce le regole su come “giocare bene” con le idee.

**Classificazioni**:
- Ragionamento deduttivo (sillogismo aristotelico – logica deduttiva):
    - Da: Tutti gli uomini sono mortali e Socrate è un uomo -> allora: Socrate è mortale
    - Corretto, ma **non ci consente di “imparare” nuova conoscenza.**

- Ragionamento induttivo (apprendimento, deduzione inversa)
    - Dall'osservazione di svariati uccelli che volano allora Tutti gli uccelli volano (e i pinguini?).
    - Produzione di conoscenza “nuova”, **a scapito della correttezza**.

- Ragionamento ipotetico o abduttivo (duale del deduttivo):
    - Dall’osservazione della morte di Socrate e sapendo che Tutti gli uomini sono mortali ipotizza che Socrate è un uomo. (e se fosse un gatto?).
    - Risale alle cause mediante l’osservazione degli effetti a scapito della correttezza.

- Ragionamento per analogia (metaforico, case-based)
    - Non richiede un modello o molti dati, ma utilizza il principio di somiglianza. Socrate e Giovanni si “assomigliano” e Socrate ama la filosofia allora: Giovanni ama la filosofia.
    - K-Nearest-Neighbor e Support Vector Machine (SVM).
    - Utilizzo di vincoli, probabilità, statistica (teorema di Bayes)

**Nota**: Con inferire ci si può riferire a deduzione, induzione, abduzione... insomma, è l’ombrello sotto cui stanno tutti i tipi di ragionamento.

**Nota 2**: Prolog fa solo inferenze deduttive, e quindi si ha la certezza della correttezza






### Rappresentazione della conoscenza
**Knowledge base (KB)** = insiemi di sentenze scritte in un **linguaggio formale**.
- Le risposte devono “derivare” dalla KB.
- notare che la conoscenza è scritta in un linguaggio formale

**Inference engine**: strutture dati ed algoritmi per utilizzare la KB e arrivare ad una risposta.
- in sostanza è un manipolatore (ricerca e sostituzione) di simboli (base di conoscenza)
- interessante: quando si sceglie un linguaggio per rappresentare la conoscenza, questo linguaggio si porta dietro una espressività che influisce su come questa conoscenza viene utilizzata dall'inference engine per "il ragionamento"

Consideremo come linguaggio formale la **logica dei predicati del primo ordine**: 
- sia come linguaggio di rappresentazione della conoscenza
- sia come metodo di ragionamento (inferenza).




## Logica dei Predicati
Il linguaggio della logica dei predicati del primo ordine è definito da:
- una sintassi, che stabilisce le caratteristiche strutturali del linguaggio formale (mediante una grammatica) senza attribuire alcun significato ai simboli;
- una semantica, che interpreta le frasi sintatticamente corrette del linguaggio. Si dà una interpretazione alle formule **stabilendo se una frase è vera o falsa**.



### Sintassi
Alfabeto, che consiste di cinque insiemi:
- l'insieme dei simboli di **costante**, C;
    - singole entità del dominio del discorso.
    - Es. “maria”, “giovanna”, “3” -> iniziale minuscola

- l'insieme dei simboli di **variabile**, V;
    - entità non note del dominio,
    - Es. X, Y -> iniziale maiuscola

- l'insieme dei simboli di **funzione**, F;
    - generalmente n-aria
    - individua univocamente un oggetto del dominio mediante una relazione tra altri “n” oggetti del dominio.
        - serve a rappresentare operazioni o **mappature tra elementi del dominio**
    - Es. madre(maria), somma(X, Y)
    - Importante: le funzioni, in logica, non presuppongono alcun concetto di valutazione

- l'insieme dei simboli di **predicato** (o relazione), P;
    - generalmente n-ari
    - generica relazione, che **può essere vera o falsa** fra “n” oggetti del dominio del discorso.
        - esprime una proprietà o una relazione tra oggetti.
    - Es. parente(giovanna, maria)
    - **NB**: si differenziano rispetto alle altre entità sintattiche, in quanto solamente a loro si applica la domanda "è vero/falso?"  
        - implicano valutazione

- i **connettivi logici**
    - es: negazione, congiunzione/disgiunzione, implicazione, ..., quantificatori (esistenziali e universali)
    - congiunzione -> ^ -> and
    - disgiunzione -> v -> or

**OSS IMPORTANTE**: pensa al predicato bello(io), c'è un problema... che cosa significa bello? Cambia per tutti e **la logica non lo definisce**


Date queste definizioni principali possiamo definire:
- **Termine** (definito ricorsivamente):
    - in sostanza tutto cio che si riduce ad un elemento del dominio
    - una variabile è un termine;
    - una costante è un termine;
    - se f è un simbolo di funzione n-aria e t1,...tn sono termini, allora f(t1,...,tn) è un termine.

- **Atomo** o formula atomica:
    - la minima cosa valutabile come T/F
    - l’applicazione di un simbolo di predicato n-ario p a n termini t1,...,tn: p(t1,..,tn). 

**Formule ben formate (fbf)**: frasi sintatticamente corrette del linguaggio.
- combinazione di formule atomiche, mediante i connettivi e i quantificatori.

**Letterale**: fbf atomica o la sua negazione.




### Semantica
```bisogna capire implicazioni ed equivalenze come funzionano```
l'implicazione locica (->) è diversa in linguaggio naturale (se -> allora) rispetto a ciò che si intende in logica
- se chesani <18 anni, allora ha il biglietto gratis sull'autobus -> vero 


Abbiamo una difficoltà, accennata nell'osservazione importante di sopra. 
- Con la semantica vogliamo dare un significato ai simboli;
- Ogni sistema formale è la modellizzazione di una certa realtà (ad esempio la realtà matematica).
- Un’interpretazione è la costruzione di un rapporto fra i simboli del sistema formale e tale realtà (chiamata anche dominio del discorso). 

```Ogni formula atomica o composta della logica dei predicati del primo ordine può assumere il valore vero o falso in base alla frase che rappresenta nel dominio del discorso.```

Come risolvere?


**interpretazine**
Dato un linguaggio del primo ordine L, un'interpretazione per L definisce un dominio non vuoto D e assegna:
- a ogni simbolo di costante in C, una costante in D;
- a ogni simbolo di funzione n-ario F, una funzione:
    - F: D^n -> D;
- a ogni simbolo di predicato n-ario in P una relazione in D^n, cioè un sottoinsieme di D^n.
    - In altre parole, la relazione associata al predicato n-ario 𝑃 contiene tutte le n-uple ordinate di elementi di 𝐷 per cui il predicato 𝑃 è "vero

Esempio: Linguaggio del primo ordine, L, nel quale si ha una costante “0”, un simbolo di funzione unaria “s” e un simbolo di predicato binario “p”.
- Interpretazione I1, D: numeri naturali.
    - "0" rappresenta il numero zero.
    - "s" rappresenta il successore di un numero naturale
    - "p" rappresenta la relazione binaria "<="
- Interpretazione I2, D: numeri interi negativi.
    - "0" rappresenta il numero zero.
    - "s" rappresenta il predecessore di un numero naturale
    - "p" rappresenta la relazione binaria "<="

**modelli**
Data un'interpretazione I e una fbf F, **I è un modello per F se e solo se F è vera in I**.
- Esempio: Per la fbf: per ogni Y p(0,Y) l’interpretazione I1 è un modello, mentre I2 non lo è.

Una **fbf è soddisfacibile** se e solo se è vera almeno in una interpretazione,
- ovvero se esiste almeno un modello per essa.

Una fbf che ha valore vero per tutte le possibili interpretazioni è detta **logicamente valida**.
- ogni possibile interpretazione è un modello

Un insieme di formule del primo ordine S è soddisfacibile, se esiste una interpretazione I che **soddisfa tutte le formule di S**
- I è un modello per ciascuna formula di S.
- Tale interpretazione è detta modello di S.

**conseguenza logica**
Una formula F segue logicamente (o è conseguenza logica) da un insieme di formule S (e si scrive S |= F), se e solo se **OGNI interpretazione I che è un modello per S, è un modello per F**
- idea: teorema di pitagora è conseguenza logica dei 5 assiomi della geometria euclidea 

```**NMB**: ragionare per conseguenze logiche è ciò che ci fà scavallare il problema dell'interpretazione! Possiamo lasciare stare l'interpretazione, basta essere daccordo sull'insieme di formule S di partenza e da questo siamo sicuri che qualunque risultato ottenuto è per forza vero anche per altre interpretazioni (...)```
- attenzione bisogna però dimostrare che ogni modello di S è un modello anche per F
- la seconda proprietà sull'insoddisfacibilità dell'unione aiuta (assurdi) ma conviene a lavorare a livello sintattico (sostituzione di simboli) piuttosto che semantico (interpretazioni, modelli)




### Regole di inferenza
sono criteri di manipolazione sintattica, ovvero regole che derivano fbf da altre fbf
- voglio dimenticarmi di che cosa significano i simboli (semantica), voglio solo delle regole con cui posso arrivare ad un risultato vero/falso 
- esempio dell'aritmentica delle elementari (3+3 lo sostituisco con 6 e non mi preoccupo più di tanto)

- modus ponens
- specializzazione
- abduzione 
    - ipotizzo A se vedo B, A->B 
    - diagnosi, ipotesi
    - come gia detto sopra, non sempre corretto
- induzione
    - osservando A(t1), A(t2), ... A(tn) dico: per ogni x A(x)
    - generalizzare concetti da esperienze
    - anche questo non sempre corretto


**Teoria assiomatica**: insieme di fbf assiomatice e insieme di regole di sostituzione

**Decidibilità**
...

**Correttezza e completezza**
- correttezza (soundness): la derivazione produce solo sentenze che sono conseguenza logica.
    - abduzione non è corretta
- completezza (completeness): la derivazione puo’ prdurre tutte le conseguenze logiche
    - le regole di inferenza non sono complete (decidibilità)



**Monotonicità**

se aggiungo degli assiomi, quest'ultimi non mi invalidano i teoremi che ho gia ottenuto con solo gli assiomi precedenti

Assunzione del mondo chiuso:
"ragionamenti per DB", se non c'è nel DB allora è falso
- il DB è il mio mondo

