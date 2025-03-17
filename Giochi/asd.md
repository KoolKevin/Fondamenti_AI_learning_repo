I giochi possono essere visti come problemi di ricerca con avversari.

L'intelligenza artificiale considera giochi con le seguenti proprietà:

- giochi a due giocatori (min e max) in cui le mosse sono alternate e le funzioni di utilità complementari (vince e perde)
- conoscenza completa: tutti i giocatori conoscono tutte le informazioni riguardanti lo stato del gioco
    - poker -> conoscenza incompleta
- nel nostro caso gli agenti sono razionali, ovvero fanno sempre la scelta migliore
    - non è sempre detto

Lo svolgersi del gioco si può interpretare come un albero in cui la radice è la posizione di partenza e le foglie le posizioni finali.


Abbiamo sempre una ricerca nello spazio degli stati, la differenza sta nel fatto che le mosse si alternano tra min e max
- a volte si parte da max a volte da min, è indifferente
- **NB**: quando sono al 2^ livello non divento min/max! Sono sempre chi ero prima ma ragiono su quale sia la mossa migliore per min/max

**NB**: caratteristica dei giochi particolare tenere conto delle simmetrie! Nel gioco del tris il fattore di ramificazione è 4 e non 9 dato che le altre mosse sono speculari alle altre e quindi esplorarle porta allo stesso risultato






### ALGORITMO MIN-MAX
```
Guardo gli stati finali possibili, decido se ho vinto/perso, risalgo l'albero e adesso posso decidere quali sono le strade vincenti e quali sono quelle perdenti
```

L’algoritmo minmax è progettato per determinare la strategia ottimale per “Max” e per suggerirgli **la prima mossa migliore da compiere**;
- per fare questo, ipotizza che “Min” faccia la scelta a lui più favorevole.
- Non è interessante la “strada”, ma solo la prossima mossa
- partiamo dai nodi foglia, vediamo controlliamo qual'è la foglia più favorevole e ci propaghiamo verso l'alto per capire che mosssa fare

**IMP**: Un nodo con max che deve muovere ha come label il massimo delle labels dei figli. Viceversa per min.

**algoritmo versione bfs**:
Per valutare un nodo n:
1. Espandi l'intero albero sotto n; (già questo è grave)
2. Valuta le foglie come vincenti per max o min;
3. Seleziona un nodo n' senza etichetta i cui figli sono etichettati. Se non esiste ritorna il valore assegnato ad n;
4. Se n' è un nodo in cui deve muovere min assegna ad esso il valore minimo dei figli, se deve muovere max assegna il valore massimo dei figli. Ritorna a 3.

- Complessità in tempo e spazio = b^d


**algoritmo versione dfs**:
- Si possono assegnare dei valori ai nodi che poi vengono aggiornati quando si espandono i figli.

Per valutare un nodo n in un albero di gioco:
1. Metti in L = (n) i nodi non ancora espansi.
2. Sia x il primo nodo in L. Se x = n e c'è un valore assegnato a esso ritorna questo valore.
3. Altrimenti se x ha un valore assegnato Vx, sia p il padre di x e Vp il valore provvisorio a esso assegnato. Se p è un nodo min, Vp= min(Vp,Vx), altrimenti Vp=max(Vp,Vx). Rimuovi x da L e torna allo step 2.
4. Se ad x non è assegnato alcun valore ed è un nodo terminale, assegnagli o 1, -1, o 0. Lascia x in L perché si dovranno aggiornare gli antenati e ritorna al passo 2.
5. Se a x non è stato assegnato un valore e non è un nodo terminale, assegna a Vx = -infinito se X è un max e Vx = + infinito se è un min (vogliamo aggiornare con i valori dei figli). Aggiungi i figli di x a L in testa e ritorna allo step 2.

- complessità temporale comunque esponenziale
- dfs perchè usiamo uno stack

conclusione: in ogni caso bisogna potare l'albero



**La soluzione (Shannon, 1949)**: si guarda avanti solo per un po' e si valutano le mosse fino ad un nodo non terminale ritenuto di successo. In pratica si applica minimax fino ad una certa profondità.

Utilizzo una certa funzione di valutazione (**che sarà un euristica**) per stimare la bontà di un certo nodo.
- e(n) = -1 sicuramente vincente per min;
- e(n) = +1 sicuramente vincente per max;
- e(n) = 0 circa le stesse probabilità;
- Poi valori intermedi per e(n).

Trade-off fra ricerca e funzione di valutazione e(n)

- min-max fino ad una certa profondità






**ALGORITMO MIN-MAX RIVISTO 2**
Posso decidere di non esplorare non solamente quando raggiungo una soglia di profondità, l'algoritmo generale ha questa forma:

Per valutare un nodo n in un albero di gioco:
1. Metti in L = (n) i nodi non ancora espansi.
2. Sia x il primo nodo in L. Se x = n e c'è un valore assegnato a esso ritorna questo valore.
3. Altrimenti se x ha un valore assegnato Vx, sia p il padre di x e Vp il valore provvisorio a esso assegnato. Se p è un nodo min, Vp= min(Vp,Vx), altrimenti Vp=max(Vp,Vx). Rimuovi x da L e torna allo step 2.
4. Se ad x non è assegnato alcun valore ed è un nodo terminale, **oppure decidiamo di non espandere l'albero ulteriormente**, assegnagli il
valore utilizzando la funzione di valutazione e(x). Lascia x in L perché si dovranno aggiornare gli antenati e ritorna al passo 2.
5. Se a x non è stato assegnato un valore e non è un nodo terminale, assegna a Vx = - infinito se X è un max e Vx = + infinito se è un min. Aggiungi i figli di X a L e ritorna allo step 2.

**NB**: Quand'è che decidiamo di non espandere ulteriormente? Ci sarà un if con una condizione che sceglie se continuare in profondità o meno!
- in tablut si avrà un minuto di tempo per fare una mossa

sempre su tablut: scegliere il cutoff a 7 livelli di profondità basandosi sulla profondità media che vedo sul mio computer non è una buona mossa dato che su altri computer la profondità media varia.





### TAGLI ALFA-BETA
I computer che "giocano" semplicemente cercano in alberi secondo certe proprietà matematiche.
- Perciò considerano anche mosse e nodi che non si verificheranno mai.
- Conseguenza: si deve cercare di ridurre lo spazio di ricerca.
- La tecnica più conosciuta è quella del taglio alfabeta

**Idea**: se sono max, taglio via l'albero sottostante ad una mossa che min non farà mai dato che quel sottoalbero non verrà mai giocato
- più complicato di così, in realtà cerco di propagare il più possibile le informazioni note dai miei antenati in maniera da tagliare il più possibile e solo se non ho abbastanza informazioni vado ad esplorare


PRINCIPO GENERALE DEI TAGLI ALFA-BETA
Si consideri un nodo N nell’albero. Il giocatore si muoverà verso
quel nodo?
- Se il giocatore ha una scelta migliore M a livello del nodogenitore od in un qualunque punto di scelta precedente, N non sarà mai selezionato. Se raggiungiamo questa conclusione possiamo eliminare N.



**ESAME**: durante gli esercizi alfa-beta è importante chiedersi se qualcuno degli antenati sa qualcosa che mi aiuta
- in questa maniera si può anche risolvere gli esercizi ad intuito piuttosto che algoritmicamente

valore migliore trovato per max -> alpha
- all'inizio +inf
valore migliore trovato per min -> beta
- all'inizio -inf

Tagli Alpha-Beta
- Si genera l’albero depth-first, left-to-right. 
- Si propagano i valori stimati a partire dalle foglie
- I temporanei valori nei MIN-nodes sono BETA-values
- I temporanei valori nei MAX-nodes sono ALPHA-values

**Caratteristica interessante**: dobbiamo sempre esplorare almeno il ramo più a sinistra


### Efficacia dei tagli
All'inizio devo cercare qualcosa se no non ho alcuna valore di alfa beta. L'algoritmo funziona bene quindi se la prima esplorazione che faccio è una strada intelligente, dato che questo mi porterà ad avere molti tagli.
- chiaramente all'inizio non so quale strada è intelligente
- posso però utilizzare una funziona euristica di nuovo

**ESAME**: i nodi della frontiera sono già ordinati secondo un'euristica data