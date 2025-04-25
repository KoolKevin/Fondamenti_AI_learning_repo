prolog è bellissimo! (Chesani), ma non si presta a risolvere a alcuni problemi... in particolare, è lento... (computazionalmente costoso)
- però è goated a fare i prototipi velocemente (rapid prototyping === prolog)
- The Power of Prolog. Introduction to modern Prolog https://www.metalevel.at/prolog

nota: vscode con plugin per prolog

## Prolog
E’ il più noto linguaggio di Programmazione Logica
- ALGORITMO = LOGICA + CONTROLLO (cosa vs come, **cosa significa?**)
- Manipolatore di SIMBOLI e non di NUMERI
- non c'è l'iterazione, **solo ricorsione**

### Programmi prolog
Un programma Prolog (puro) è un **insieme di clausole di Horn** che rappresentano:
- **FATTI** riguardanti gli oggetti in esame e le relazioni che intercorrono
    - implicazioni senza antecedente
    - p(x) :- true
    - p(x).
- **REGOLE** sugli oggetti e sulle relazioni (SE…..ALLORA)
    - implicazioni sotto forma di clausole di horn
    - p(x) :- a(X), b(Y), ...
- **GOAL** (clausole senza testa), sulla base della conoscenza definita
    - implicazioni senza un conseguente (ovvero una negazione)
    - :- p(x)
    - ?- p(x)

I conseguenti sono in or, gli antecedenti sono in and
- B1 or ... or Bm if A1 and ... and An

NB: che la sintassi sembra avere più letterali positivi, in realtà se trasformi le implicazioni e neghi il conseguente, la forma di Horn si palesa


### Prova di un goal
- Un goal viene provato provando i singoli letterali da sinistra a destra
    - :- collega(X,Y), persona(X), persona(Y).
- Un goal atomico (ossia formato da un singolo letterale) viene provato confrontandolo e unificandolo con le teste delle clausole contenute nel programma 
    - Se esiste una sostituzione per cui il confronto ha successo
        - se la clausola con cui unifica è un fatto, la prova termina;
        - se la clausola con cui unifica è una regola, ne viene provato il Body
    - Se non esiste una sostituzione il goal fallisce


...

**OSS**: Non c’è distinzione (sintattica) tra costanti, simboli funzionali e predicativi.
- allora tutto è termine e tutto e manipolabile (metaprogrammazione)




### Come sono quantificate le variabili
Le variabili all'interno di una clausola sono sempre quantificate universalmente.

Tuttavia è comdo fare una considerazione:
- per le regole abbiamo delel variabili che compaiono solo nel corpo Yk, e delle variabili che compaiono sia nella testa che nel corpo Xk
- tutte queste variabili sono quantificate universalmente
- tuttavia una maniera equivalente più chiara di quantificare le variabili che compaiono solo nel corpo della regola è la quantificazione esistenziale





## Risoluzione in PROLOG
Si considerano solo clausole di Horn (al più un letterale positivo) 
- il letterale positivo corrisponde alla testa della clausola
    - il corpo della clausola è tutto negato (ricorda trasformazione delle implicazioni)

Si adotta una strategia risolutiva particolarmente efficiente 
- RISOLUZIONE SLD (vedremo che corrisponde al Backward chaining per clausole di Horn).
- Non completa per la logica a clausole, ma completa per il sottoinsieme delle clausole di Horn.






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








### Strategia di Selezione e Ricerca in Prolog
Nella risoluzione SLD così come è stata enunciata sihanno due forme di non determinismo:

1. La prima forma di non determinismo è legata alla selezione di un atomo Am del goal da unificare con la testa di una clausola, e viene risolta definendo una particolare regola di calcolo. 
    -  La regola di calcolo influenza solo l'efficienza
    - Non influenza né la correttezza né la completezza deldimostratore.
    - **Indipendenza dalla regola di calcolo**: Dato un programma logico P, l'insieme di successo di Pnon dipende dalla regola di calcolo utilizzata dallarisoluzione SLD.
2. La seconda forma di non determinismo è legata alla scelta di quale clausola del programma P utilizzare in un passo di risoluzione (ne possono esistere molteplici unificabili), e viene risolta definendo una strategia di ricerca.
    - Questa forma di non determinismo implica che **possano esistere più soluzioni alternative per uno stesso goal** (in base ) 

...

Durante la risoluzione, prolog mette la roba in testa
- va in DFS


...


Quando scrivo un programma Prolog devo sapere se sto utilizzando Left-most o Right-most altrimenti rischio di introdurre dei loop

...

possono esistere più soluzioni (anche infinite)

...


La strategia di ricerca di prolog **non è completa**
- d'altronde uso DFS e posso quindi andare in loop

...


Prolog deve decidere una clausola tra quelle con cui può unificare 
- la scelta è quella dell'ordine con cui vengono scritte (ordine sintattico)
    - le soluzioni non cambiano (SLD corretto e completo) ma cambiamo l'ordine di esplorazione e magari evitiamo loop
- punto di scelta 

... incompletezza implementativa dovuta ai loop di DFS

curiosità della notazione:
- in prolog l'and è rappresentato con ,
- l'or con ;
    - utilizzato anche per chiedere altre risposte








## Interpretazione procedurale (molto importante)
interpretazione informale che aiuta a prendere familiarità con la programmazione logica in Prolog

...

uno degli argomenti del mio predicato è destinato a svolgere il ruolo di variabile di ritorno

ma abbiamo anche reversibilità quindi questo parametro di uscita può cambiare


in prolog la firma di un predicato è dettata da nome e arità del predicato
- non esiste il tipo degli argomenti







### Predicati builtin extra-logici
causano side effects