prolog è bellissimo! (Chesani), ma non si presta a risolvere a alcuni problemi... in particolare, è lento... (computazionalmente costoso)
- però è goated a fare i prototipi velocemente (rapid prototyping === prolog)
- The Power of Prolog. Introduction to modern Prolog https://www.metalevel.at/prolog

nota: vscode con plugin per prolog

## Prolog
E’ il più noto linguaggio di Programmazione Logica
- ALGORITMO = LOGICA + CONTROLLO (cosa vs come, **cosa significa?**)
- Manipolatore di SIMBOLI e non di NUMERI
- non c'è l'iterazione, **solo ricorsione**

Un programma Prolog (puro) è un insieme di clausole di Horn
- notare che la sintassi sembra avere più letterali positivi, in realtà se trasformi le implicazioni e neghi il conseguente, la forma di Horn si palesa

...


Un goal viene provato provando i singoli letterali da sinistra a destra
- verso opposto dell'implicazione
- ma questo è il verso con cui dobbiamo concepire i programmi dichiarativi 

...

**OSS**: Non c’è distinzione (sintattica) tra costanti, simboli funzionali e predicativi.
- allora tutto è termine e tutto e manipolabile (metaprogrammazione)

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