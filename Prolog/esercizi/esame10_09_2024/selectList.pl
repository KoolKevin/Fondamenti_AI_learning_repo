% Si scriva un predicato Prolog selectList(L1,M,L2,Result) che date due liste di interi L1 e L2 (quindi tutti gli elementi sono ground)
% e un numero intero M, crei una lista Result composta dagli elementi di L1 > M e che non appartengono a L2.

% Si può utilizzare , nella soluzione, il predicato member/2 come definito nel testo dell'esercizio che segue.

% Esempi:
%     ?-selectList([1,2,7,3,4,5],3,[1,2,3,5], [7,4]).
%     Yes
    
%     ?-selectList([1,2,7,3,4,5],3,[1,2,3,5], X).
%     Yes X= [7,4].

selectList([], _, _, []).

selectList([H|T], M, L2, [H|R]) :-
    H > M,
    \+ member(H, L2),	% H e L2 sono sicuramente ground, bisogna stare attenti con NF
    !,
    selectList(T, M, L2, R).

selectList([_|T], M, L2, R) :-
    selectList(T, M, L2, R).