In Prolog le liste sono dei termini costruiti a partire da uno speciale atomo ([], che denota la lista vuota) e utilizzando un particolare operatore funzionale (l'operatore “.”).

Definizione ricorsiva della lista:
- ...
- il carattere . è un funtore che mangia testa e coda della lista

esempi:
...

in prolog non c'è nessun vincolo sulla forma e sull'omogeneità degli elementi della lista
- in prolog le liste sono ibride
- nota caso 5: lista con dentro un solo elemento che è la lista vuota
    - posso avere altre liste come elementi di una lista



**notazione semplificata**:
- al posto di .(T, Lista) -> [T | Lista]
    -  .(f(g(X)), . (h(z), .(c, []))) diventa [f(g(X)) | [h(z) | [c | []]]]
- le quadre [ X | Y ] sostituiscono .(X, Y)...
- continua ad essere scomodo con più termini...
- liste con più elementi non le scrivo così: [a| [b| [c]]], ma così: [a, b, c]
    - [f(g(X)) | [h(z) | [c | []]]] diventa [f(g(x)), h(z), c] 
- è zucchero sintattico, l'interprete prolog traduce nella notazione con l'operatore .



### Unificazione delle liste:
intuitiva















- lavariabile **_** è una variabile speciale che unifica con qualsiasi cosa.
    - Serve ad esprimere l'idea di un qualcosa di cui non ci interessa sapere il valore ma sappiamo che esiste (o ce ne vogliamo assicurare). 
    - nei linguaggi procedurali viene chiamata **variabile muta**
    - tutte le volte che si può utilizzare una variabile muta conviene farlo.
    - Perchè? Sono sorgente di bug

Da cosa capisco che una variabile non mi serve?
- se nella definizione di un predicato una variabile viene utilizzata sia in testa che nel body, allora quella variabile mi interessa. 
- se una variabile compare solo nella testa di una clausola allora vuol dire che questa non mi interessa
    - la testa magari unifica con una query, ma dopo nel corpo non viene sostituito niente 
    - peccato, viene eseguita una unificazione che non serve a niente
- prolog fornisce un warning per variabili di questo tipo: singleton variables












### Operazioni sulle liste

- is_list(T)
    - [a|b] non è una lista dato che b non è una lista
- member(T, L)
    - curioso notare il comportamento generativo di member() ed append() -> Paradigma dichiarativo
- length(L, N)
- append(L1,L2,L3)
    - concatenazione di due liste
-  delete1(El,L,L1) e delete1(El,L,L1)
    - rispettivamente: elimina il primo termine unificabile con El, elimina tutti i termini unificabili con El, 
    - **NB**: attenzione alla mutua esclusione!
- reverse(L, Lr) 






**Operazioni sulle Liste – Osservazione**: 
Molte operazioni su lista seguono lo stesso pattern:
1. Caso base (lista vuota)
2. Caso ricorsivo (isolo Testa, e ripeto su Resto)

Esempi:
    length([],0).
    length([_|L],N) :-
        length(L,N1),
        N is N1 + 1.

    member(T, [T | _]).
    member(T, [_ | L]) :-
        member(T, L).


### Operazioni sugli insiemi
Gli insiemi possono essere rappresentati come liste di oggetti (senza ripetizioni).


- intersection(S1,S2,S3)
    - l’insieme S3 contiene gli elementi appartenenti all’intersezione di S1 e S2
- union(S1,S2,S3)
    - l’insieme S3 contiene gli elementi appartenenti all’unione di S1 e S2

NB: anche qua abbiamo problemi di mutua esclusione e quindi di risultati sbagliati dopo il primo 