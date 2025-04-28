le liste non sono predicati, sono un insieme di elementi (termini?) in un certo ordine, con o senza ripetizione.

Definizione ricorsiva della lista:
- ...
- il carattere . è un funtore che mangia testa e coda della lista

esempi:
...

in prolog non c'è nessun vincolo sulla forma e sull'omogeneità degli elementi della lista
- in prolog le liste sono ibride
- nota caso 5: lista con dentro un solo elemento che è la lista vuota
    - posso avere altre liste come elementi di una lista

**notazione semplificata**: [T | Lista]
- è zucchero sintattico, l'interprete prolog traduce nella notazione con cento elementi innestati
- liste con più elementi non le scrivo così: [a| [b| [c]]], ma così: [a, b, c]

unificazione: intuitiva
- variabile _ è una variabile speciale che unifica con qualsiasi cosa. Serve ad esprimere l'idea di un qualcosa di cui non ci interessa sapere il valore ma sappiamo che esiste (o ce ne vogliamo assicurare). 
    - nei linguaggi procedurali viene chiamata **variabile muta**
    - tutte le volte che si può utilizzare una variabile muta conviene farlo.
    - Perchè? Sono sorgente di bug
    - da cosa capisco che una variabile non mi serve?
    - se nella definizione di un predicato una variabile viene utilizzata sia in testa che nel body, allora quella variabile mi interessa. 
    - se una variabile compare solo nella testa di una clausola allora vuol dire che questa non mi interessa
        - peccato, viene comunque sottoposta ad unificazione
    - prolog fornisce un warning per variabili di questo tipo: singleton variables

...

[a|b] non è una lista dato che b non è una lista

...

### Varie operazioni

...


curioso notare il comportamento generativo di member() ed append(). Paradigma dichiarativo


...


**NB**: problema della mutua esclusione in delete()