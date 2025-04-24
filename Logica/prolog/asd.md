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
- **REGOLE** sugli oggetti e sulle relazioni (SE…..ALLORA)
- **GOAL** (clausole senza testa), sulla base della conoscenza definita

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