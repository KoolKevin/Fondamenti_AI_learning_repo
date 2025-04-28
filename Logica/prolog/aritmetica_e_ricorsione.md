## Aritmetica
Non esiste, in logica, alcun meccanismo per la valutazione di espressioni/funzioni, operazione fondamentale in un linguaggio di programmazione 

I numeri interi possono essere rappresentati come termini Prolog, mediante la notazione di Peano ma questo non è utilizzabile in pratica.

**Soluzione**: predicati predefiniti per la valutazione di espressioni.

2\*3-6 === -(\*(2,3),6)

**Tutto è un termine in questo linguaggio** (anche le clausole stesse del programma)
- Gli operatori infissi sono in realtà simboli di funzione (sebbene particolari e definiti come operatori)
- Per gli operatori aritmetici binari il Prolog consente tanto una notazione prefissa (funzionale), quanto la più tradizionale notazione infissa
- inoltre, la valutazione di priorità ed associatività è corretta

**Predicati per la valutazione di espressioni**

```predicato predefinito is```

T is expr === is(T, expr)
- L’espressione Expr viene valutata e il risultato della valutazione viene unificato con T
- **NB**: le variabili in Expr DEVONO ESSERE ISTANZIATE al momento della valutazione
- corrisponde ad un assegnamento di una variabili (a singolo assegnamento) in un linguaggio imperativo

:- X is 2+3, X is X+1.
no

NOTA: non corrisponde a un assegnamento dei linguaggi imperativi. Le variabili sono a **singolo assegnamento**.


Nel caso dell'operatore is l'ordine dei goal è rilevante.
1. :- X is 2+3, Y is X+1.
2. :- Y is X+1, X is 2+3.

Mentre il goal (1) ha successo e produce la coppia di istanziazioni (X=5, Y=6) … il goal (2) fallisce.

Il predicato predefinito "is" è un tipico esempio di un **predicato predefinito non reversibile**; come conseguenza le procedure che fanno uso di tale predicato non sono (in generale) reversibili (predicati extra logici perdono le proprietà )














### Operatori relazionali
Il Prolog fornisce operatori relazionali per confrontare i valori di espressioni. Tali operatori sono **utilizzabili come goal** all'interno di una
clausola Prolog ed hanno notazione infissa

listone: >, <, >=, =<, ==, =:=, =\=, \==

Passi effettuati nella valutazione di 'Expr1 REL Expr2':
- vengono valutate Expr1 ed Expr2
    - **NB**: le espressioni devono essere completamente istanziate
- I risultati della valutazione delle due espressioni vengono confrontati tramite l’operatore REL

**Unificazione e uguaglianza tra termini**
```T1 = T2```

Verifica se T1 e T2 sono unificabili.
- Viene generata la sostituzione che unifica i due termini (e vengono pertanto legate le variabili nei due termini).

?- f(X,g(a)) = f(h(c),g(Y)).
    yes X=h(c) Y=a
?- 2+3 = 5.
    no

```T1 == T2```
Verifica se T1 e T2 sono uguali (identici). 
- In particolare, se i due termini contengono due variabili in posizioni equivalenti, perché i termini siano uguali, le due variabili devono essere la stessa variabile.
- Si noti che in questo caso non viene generata alcuna sostituzione.
?- f(a,b) == f(a,b).
    Yes
?- f(a,X) == f(a,b).
    No
?- f(a,X) == f(a,X).
    Yes
?- f(a,X) == f(a,Y).
    no

L'operatore == non effettua valutazioni anche se i termini rappresentano espressioni
?- 2*2 == 4.
    no

```E1 =:= E2```
Verifica se E1 e E2 sono espressioni che hanno lo stesso valore?
?- 2*2 =:= 4.
    yes


...



### Ricorsione
Il Prolog non fornisce alcun costrutto sintattico per l'iterazione (quali, ad esempio, i costrutti while e repeat) e l'unico meccanismo per ottenere iterazione è la definizione ricorsiva. 

Se la ricorsione è poi in coda, quest'ultima si può anche ottimizzare. 
- In Prolog l'ottimizzazione della ricorsione tail è un po' più complicata che non nel caso dei linguaggi imperativi a causa del della presenza di punti di scelta nella definizione delle clausole.
- esempio:
    - p(X) :- c1(X), g(X).
    - (a) p(X) :- c2(X), h1(X,Y), p(Y).
    - (b) p(X) :- c3(X), h2(X,Y), p(Y).

- Due possibilità di valutazione ricorsiva del goal :- p(Z).
    - se viene scelta la clausola (a), si deve ricordare che (b) è un punto di scelta ancora aperto.
        - Bisogna mantenere alcune informazioni contenute nel record di attivazione di p(Z)
    - se viene scelta la clausola (b), non è più necessario mantenere alcuna informazione contenuta nel record di attivazione di p(Z) e la rimozione di tale record di attivazione può essere effettuata (TRO)
        - Più in generale questa ottimizzazione vale sempre quando si considera l'ultima clausola della procedura

**NB**: nella ricorsione dobbiamo distinguere il caso base dal caso ricorsivo ed eseguire questi in **mutua esclusione**. Gli operatori relazionali permettono di fare questa cosa. 
- Vedi N>1 nell'esercizio di specialPrint.