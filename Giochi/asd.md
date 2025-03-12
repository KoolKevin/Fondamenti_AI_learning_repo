conoscenza completa: tutti i giocatori conoscono tutte le informazioni riguardanti lo stato del gioco
- poker -> conoscenza incompleta

agenti sono razionali? Cioè, fanno sempre la scelta migliore?
- non è detto


Abbiamo sempre una ricerca nello spazio degli stati, la differenza sta nel fatto che le mosse si alternano tra min e max
- a volte si parte da max, a volte di min
- NB: quando sono al 2^ livello non divento min/max! Sono sempre chi ero prima ma ragiono su quale sia la mossa migliore per min

**NB**: caratteristica dei giochi particolare tenere conto delle simmetrie! Nel gioco del tris il fattore di ramificazione è 4 e non 9 dato che le altre mosse sono speculari alle altre e quindi esplorarle porta allo stesso risultato



### ALGORITMO MIN-MAX
partiamo dai nodi foglia e ci propaghiamo verso l'alto


min-max fino ad una certa profondità

slide 14, **decidiamo** è una parola pericolosa! Ci sarà un if con una condizione che sceglie se continuare in profondità o meno!
- in tablut si avrà un minuto di tempo per fare una mossa

sempre su tablut: scegliere il cutoff a 7 basandosi sulla profondità media che vedo sul mio computer non è una buona mossa dato che su altri computer la profondità media varia.


### TAGLI ALFA-BETA
idea: se sono max, taglio via l'albero sottostante ad una mossa che min non farà mai
- più complicato di così, in realtà cerco di propagare il più possibile le informazioni note dai miei antenati in maniera da tagliare il più possibile e solo se non ho abbastanza informazioni vado ad esplorare
- durante gli esercizi alfa-beta è importante chiedersi se qualcuno degli antenati sa qualcosa che mi aiuta
    - in questa maniera si può anche risolvere gli esercizi ad intuito piuttosto che algoritmicamente

valore migliore trovato per max -> alpha
- all'inizio +inf
valore migliore trovato per min -> beta
- all'inizio -inf
