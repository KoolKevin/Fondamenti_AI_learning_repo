ciclo ...
- output delle azioni non è necessariamente deterministico
- prima distinzione tra problemi che sono abbastanza deterministici e altri meno
    - nel caso di problemi non deterministici abbiamo un insieme di stati futuri caratterizzati da una distribuzione di probabilità
    - pensa alla borsa
- noi ci concentriamo sul caso facile; inoltre, lo stato di osservazione aiuta col non-determinismo (con completo determinismo si può anche evitare)

Algoritmo assolutamente generale
...
utili per categorizzare la maggior parte dei problemi di AI, non per risolverli

**Lo Spazio degli Stati è Caratterizzato da**:
-  Uno stato iniziale in cui l’agente sa di trovarsi (non noto a priori);
- Un insieme di azioni possibili che sono disponibili da parte dell’agente (insieme operatori che trasformano uno stato in un altro o più formalmente una funzione successore S(X) che riceve in ingresso uno stato e restituisce l’insieme degli stati raggiungibili).
    - mi permette di generare le prossime mosse disponibili dato uno stato
- Un cammino è una sequenza di azioni che conduce da uno statoa un altro


### Soluzione del problema come ricerca in uno spazio degli stati
definizione di funzione successore come operatore di base che mi fa passare da uno stato all'altro
- pensare è diverso dall'agire 

La formulazione più semplice di un problema è arrivare in un determinato stato

- trovare una soluzione ottima

**NB**: l'algoritmo non riesce a "pilotare la ricerca con un colpo d'occhio". Lui, dato uno stato, riesce a vedere solo dove riesce ad andare. Le prova tutte, anche quelle insensate 

...

modellazione con grafi che hanno degli anelli
- soluzioni infinite
- vado in loop??!
- no se mi tengo salvati i nodi in cui sono già passato


...

8 regine e sudoku condividono la caratteristica di avere dei vincoli

...

Problemi scomponibili (parallelizzabili) e problemi non scomponibili (interagenti) 