specialPrint(1) :- write(1), nl.
specialPrint(N) :- N>1, write(N), nl, TheNext is N-1,specialPrint(TheNext). % nota, N>1 è solo un controllo dell'input; NON è il caso base 