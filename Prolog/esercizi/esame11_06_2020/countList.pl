% countList(N, P, N1) data una lista P di interi e un intero N, da
% in uscita un numero N1 che rappresenta quante volte compare l’elemento N in P.
% 
% Ad esempio:
% ?-countList(3, [3,3,2,3,1], X).
%   X = 3
% ?-countList(9, [3,3,2,3,1], X).
%   X = 0

countList(_, [], 0) :-
    !. % prolog lascia aperto il punto di scelta anche se sotto non unifica niente (infatti restituisce false); taglio via

countList(El, [El|Coda], N) :-
    !,
    countList(El, Coda, N1),
    N is N1+1.

countList(El, [_|Coda], N) :-
    countList(El, Coda, N).