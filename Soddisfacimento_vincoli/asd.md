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

Il terzo grado di libertà è ciò che differenzia le diverse strategie:
- Algoritmi senza propagazione  (/generativi/con vincoli a posteriori):
    - Generate and Test
    - Standard Backtracking
    - genero una soluzione e solo dopo vedo se rispetta i vincoli (e quindi se è valida)
- Algoritmi di Propagazione (con vincoli a priori):
    - Forward Checking
    - (Partial and Full) Look Ahead
    - Ad ogni assegnamento(?) propago i vincoli il più possibile, se continuando così riesco ad arrivare ad una foglia (soluzione) allora sono sicura di aver trovato una soluzione valida


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




    ...




# CHIEDI AL PROF COME SI FA AD AVERE MIGLIAIA DI VARIABILI
# QUAND'é CHE MI CONVIENE MODELLARE UN PROBLEMA COME CSP
- problemi di scheduling con vincoli
# RELAZIONE CON SIMPLESSO DI RICERCA OPERATIVA





## Tecniche di consistenza
aiutano a buttare via dei valori. Non mi trova necessariamente delle soluzioni ma aiuta  le ricerche (FLA, ...) a trovare una soluzione con minor costo computazionale 

**NB**: nei grafi i vincoli sembrano ad essere orientati ma in realtà stabiliscono solo il verso del ragionamento quando si applica il vincolo. In realtà le frecce sono due, in ambo le direzioni (nota anche l'ordine delle eliminazini/aggiunte nell'algoritmo)



ERRORE TIPICO ALL'ESAME: eliminare un valore della variabile nella destinazinoe e non nella sorgente


### Procedimento iterativo e raggiungimento della quiescenza

...

l'ordine non conta




### CSP ed ottimizzazione

...

nel mondo reale, tipicamente avremo più funzioni obiettivo da ottimizzare, tipicamente in conflitto tra di loro.

Come fare
- somma pesata delle funzioni
- ...