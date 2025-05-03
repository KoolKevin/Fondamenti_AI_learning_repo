### Close World Assumption
Ricordiamo la CWA:
- è una **regola di inferenza** che afferma che se un atomo A **ground** (importante per dopo) non è conseguenza logica di un programma P, allora possiamo inferire che vale ~A
- in altre parole, stiamo ragionando come un DB, se qualcosa non è dentro alla base di conoscenza (fatti + predicati) allora deve essere per forza falsa
    - il DB è il mio mondo

**NB**: è un modo per inferire informazioni negative! 

La CWA è un esempio di regola di inferenza **NON MONOTONA** in quanto l’aggiunta di nuovi assiomi alla teoria (ossia nuove clausole in un programma) può modificare l’insieme di teoremi che valevano precedentemente.
- vedi: persona('Fido').

Siamo portati a pensare con la CWA 
- se qualcosa non è conseguenza logica dei dati nel DB, allora possiamo inferire che è falsa

Tuttavia, non è detto che questo ci porti a ragionare in modo corretto.
- se nel mio programma non c'è scritto "persona('Fido')." non è detto che non esista una persona che si chiama Fido
- (d'altronde la CWA non è monotona)

La CWA diventa problematica se si cerca di modellare un sistema dinamico che **evolve nel tempo**
- la CWA assume che quello che non è vero ora sia falso
- ma qualcosa può essere vero fino ad oggi ma non essere più vero domani, o viceversa
- non sempre quindi la possiamo usare 
- soluzioni? e.g. tre valori di verità: vero, falso, ignoto






**PROLOG SFRUTTA LO STESSO LA CWA**
- questo comportamento è integrato nel modo in cui Prolog gestisce il **fallimento delle query**
    - se non riesce a dimostrare qualcosa basandosi sulle clausole del programma, assume che non sia vero.

**PROBLEMA**:
A causa della sola **semi-decidibilità** della logica del primo ordine, non esiste alcun algoritmo in grado di stabilire in un tempo finito **se A non è conseguenza logica di P**
- Dal punto di vista operazionale, se A non è conseguenza logica di P, **la risoluzione SLD può non terminare**.

**NB**: la CWA si basa sul sapere se qualcosa non è conseguenza logica (P ~|= A \ ~A)

```L'applicazione della CWA deve necessariamente essere ristretta agli atomi la cui dimostrazione termina in TEMPO FINITO, cioè agli atomi per cui la risoluzione SLD non diverge```
- come si fà?





### Negazione per fallimento
L’uso della CWA viene sostituito con quello di una regola **meno potente**
- in grado di dedurre un insieme più piccolo di informazioni negative.

**Negazione per Fallimento ("Negation as Failure" – NF)**:
- si limita a derivare la negazione di atomi la cui dimostrazione termina con fallimento in tempo finito
- Dato un programma P, se l'insieme **FF(P) (insieme di fallimento finito) denota gli atomi A per cui la dimostrazione fallisce in tempo finito**, la regola NF si esprime come:
    - NF(P)={ ~A | A app. FF(P)}

In sostanza, stiamo dicendo la stessa cosa della CWA, se qualcosa non è conseguenza logica, allora è falso. Aggiriamo il problema della indecidibilità. Infatti:
- Se un atomo A appartiene a FF(P) allora A NON è conseguenza logica di P ...
- ... ma non è detto che tutti gli atomi che NON sono conseguenza logica del programma appartengano all'insieme di fallimento finito.
- ci sono anche quelli che NON falliscono in un tempo finito :(
- per questo la NF è meno potente della CWA


La domanda rimane aperta: ```come facciamo a limitarci agli atomi per cui la dimostrazione (fallimento per NF) termina in tempo finito?```
- (mi sembra di capire che non possiamo (siamo incompleti))






### Risoluzione SLDNF
Per risolvere goal generali, cioè che possono contenere letterali negativi, si introduce un'estensione della risoluzione SLD, nota come risoluzione SLDNF [Clark 78].
- Combina la risoluzione SLD con la negazione per fallimento (NAF, Negation As failure)


Sia :- L1, ..., Lm il goal (generale) corrente, in cui L1, ..., Lm sono letterali (atomi o negazioni di atomi). Un passo di risoluzione SLDNF si schematizza come segue:
- NON si seleziona alcun letterale negativo Li, se non è "ground" (capiamo meglio dopo il perchè);
- Se il letterale selezionato Li è positivo (siamo nel caso normale), si compie un passo ordinario di risoluzione SLD
- Se Li è del tipo ~A (con A "ground") ed A fallisce finitamente (cioè ha un albero SLD di fallimento finito), Li ha successo e si ottiene il nuovo risolvente
    - :- L1, ..., Li-1, Li+1, ..., Lm
 
In pratica, metto da parte il not e prima cerco di dimostrare il goal senza, poi lo recupero e lo applico al risultato ottenuto.
- Stiamo applicando CWA/NF: se A NON è conseguenza logica (derivabile) del mio programma, allora possiamo inferire ~A
    - viceversa, se A è conseguenza logica allora sappiamo che ~A è falso e quindi Li fallisce.  
- riciclo il codice SLD

```Tutto questo solo per robe ground? Come mai?```



Iniziamo col notare che, considerando solo letterali negativi ground, risolvere con successo un letterale negativo **non introduce alcun legame (unificazione)** per le variabili 
- :- L1, ..., Li-1, Li+1, ..., Lm -> non viene applicata alcuna sostituzione.

**Definizioni**:
- Una regola di calcolo (selezione) si dice **safe** se seleziona un letterale negativo solo quando è "ground“.
- La selezione di letterali negativi solo "ground" è necessaria per garantire **correttezza** e completezza della risoluzione SLDNF.




**In PROLOG**
Il linguaggio Prolog seleziona sempre il letterale più a sinistra, **senza controllare che sia "ground"** e quindi non adotta una regola di selezione safe
- Realizzazione **non corretta** della risoluzione SLDNF (già prolog non era completo...)

Si noti che, data la strategia di risoluzione utilizzata dal Prolog è possibile che la dimostrazione di A (per cercare di dimostrare ~A) non abbia termine ossia che il Prolog vada in loop in tale dimostrazione (incompletezza).


### SLDNF, variabili e quantificatori
```Cosa succede se si seleziona un letterale negativo non ground ?```
- vedi esempio slide 22
- in pratica non siamo corretti, vengono date risposte sbagliate alle query.

Il problema nasce dal fatto che non si interpreta correttamente la quantificazione nel caso di letterali negativi non "ground"
- la negazione in SLDNF mi porta a sostituire le variabili quantificate esistenzialmente del goal in variabili quantificate universalmente
- scorretto


Insomma, se nella valutazione di un goal ho delle variabili non ground il tutto non è più safe, dato che quest'ultime vengono quantificate in maniera opposta.

**NB**: spesso però **ordinando in maniera ben pensata i goal** di una clausola si riesce a rimanere nel caso ground grazie all'**unificazione**

**NB**: una conseguenza strana della negazione in prolog è quindi che scambiando l'ordine dei letterali, a volte il risultato potrebbe cambiare
- logicamente, scambiare l'ordine di due cose in and non dovrebbe fare alcuna differenza
- il meccanismo di risoluzione SLDNF abbiamo visto che non funzione per variabili non ground (che potrebbero presentarsi modificando l'ordine dei letterali)





**Riassumendo**:
- **Prolog non adotta una regola di selezione safe**
    - Questo fa perdere la correttezza del sistema di dimostrazione
    - Usando la regola di selezione di Prolog, si possono ottenere risultati diversi da quelli attesi a causa delle quantificazioni delle variabili.
- E’ buona regola di programmazione verificare che i goal negativi siano sempre ground al momento della selezione.
- **Questo controllo è a carico dell'utente programmatore !!**
    - (esistono predicati predefiniti var e nonvar)



**Altre considerazioni**:
La regola di selezione non è corretta ma è semplice correggerla con i **metainterpreti**
- posso riordinare i letterali delle mie clausole in maniera tale da ottenere solo variabili ground
- tuttavia, creo problemi da altre parti (riordinamento del programma)

C'è un motivo se la regola di selezione non è safe, **per chiarezza di comunicazione con il programmatore!**
- se l'interprete non eseguisse i goal nell'ordine definito dal programmatore, quest'ultimo vedrebbe l'esecuzione misteriosamente ricombinata (pensa alle stampe) 