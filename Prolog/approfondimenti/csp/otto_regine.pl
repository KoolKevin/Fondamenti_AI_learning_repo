solution(S) :-
    permutation([1,2,3,4,5,6,7,8], S),
    safe(S).

permutation([], []).
permutation([H|T], PermList) :-
    permutation(T, PermTail),
    delete1(H, PermList, PermTail). % delete1 usato al contrario: genero (generate & test) PermList fissando un PermTail e 
                                    % lasciando creare a prolog tutte le possibili permutazioni che mi creano PermTail. 
                                    % Prolog prova tutti i modi di inserire H in PermList per ottenere PermTail.

delete1(El, [El|T], T).
delete1(El, [H|T], [H|T1]) :-
    delete1(El, T, T1).

safe([]).
safe([Queen|Others]) :-
    safe(Others),
    noattack(Queen, Others, 1).

% siccome sto considerando una permutazione di [1...8] non devo considerare attacchi stessa riga / stessa colonna
noattack(_, [], _).
noattack(Y, [Y1|Ylist], Xdist) :-
    Y-Y1 =\= Xdist,   % se due regine sono su una diagonale, allora la distanza verticale (Y-Y1) 
    Y1-Y =\= Xdist,   % è uguale a quella orizzontale (Xdist). (controllo rigirando in quando non ho abs())
    Dist1 is Xdist +1,
    noattack(Y, Ylist, Dist1).