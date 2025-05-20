Questa è una parte difficile da classificare
- riguarda sia aspetti di rappresentazione della conoscenza
- sia aspetti di ricerca nella spazio degli stati

La pianificazione riguarda 

azioni che vengono messe in serie una dietro l'altra per raggiungere un determinato goal

ordine parziale




...


pianificazione classica

pianificazione reattiva





situation calculus:
- situation = insieme dei fluenti
- si assume implicitamente la CWA




frame problem:
devo scrivere anche tutto ciò che dietro (sfondo, frame) NOn viene modificato
- esplosione computazionale
- devo dire tutto ciò che l'azione fa e tutto ciò che l'azione non fa





Strips assumption per il frame problem
- hanno dovuto specificare gli effetti negativi ed effetti positivi
    - lista degli add e lista dei delete
    
In strips vale comunque la CWA


punto di non determinismo di STRIPS se ho a,b,c in che ordine rimetto dentro lo stack?
- regola di selezione
- problematico se i goal interagiscono

strips fa backtracking
- abbiamo un punto di scelta
- strips prova con un ordine e se non riesce fa backtracking



Anomalia di Sussman