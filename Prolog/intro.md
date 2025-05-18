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
(ricorda che A->B === ~A v B)

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


**nomenclatura leggermete diversa rispetto alla logica del primo ordine**:
- Facts and Rules are called Terms
- In prolog con atomo ci si riferisce ad una costante simbolica (stringa alfanumerica).





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


