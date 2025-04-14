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