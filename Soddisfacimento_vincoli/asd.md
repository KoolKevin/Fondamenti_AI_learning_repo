insieme finito di variabili

Un CSP è definito da tra 3 insiemi:
- ...

risolvere un CSP significa trovare una valore per tutte le variabili, ognuna che soddifi tutti i vincoli


CSP come esplorazione di un albero con DFS
- approccio naive
- ogni livello corrisponde all'assegnamento di un valore ad una variabile

Tre gradi di libertà
- i primi due riguardano le euristiche sulla strategia di ricerca
- **propagazione effettuata in ciascun nodo**... cosa significa?



Algoritmi generativi:
- check dei vincoli a posteriori

- generate & test
    - non necessariamente devo esplorare tutto l'albero in larghezza, ma almeno una soluzione la devo generare e quindi in profondità si
    - sembra stupido ma in realtà in alcune situazioni è una buona soluzione
- standard backtracking
    - ad ogni assegnamento verifico tutti i vincoli riguardanti la variabile appena istanziata rispetto a solo quelle già istanziate



Algoritmi di propagazione
- cosa significa propagare il vincolo? check dei vincoli a priori

- forward checking
    - con dominio vuoto fallisce e fa backtraking(a quanto pare lo fa me nella slide è ambiguo)
    - il forward checking sembra molto meglio rispetto a standard backtracking. Il problema è che ogni volta che assegno un valore ad una variabile vado a scorrere tutte le mie variabilil "adiacenti" e per ognuna di queste tutti i valore del suo dominio

- ESAME: a volte nell'esame ci sono i pasti gratis

- partial & full look-ahead
    - lookahead delle variabili che ho ancora assegnato (a{1,2,3}; b{3}; con a!=b)
    - partial ordina le variabili e controlla le variabili contro solo le successive; full controlla contro tutte le variabili
    - chiaramente, il full lookahead elimina più soluzioni sbagliate rispetto a partiale, e quindi possiamo quasi dire che ciò che rimane è una soluzione. Questo però a scapito di un costo computazionale maggiore