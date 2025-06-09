% Si scriva un predicato Prolog split(L1, N, L2) che data in ingresso la lista L1 e l'intero N,
% restituisce la lista L2 contenente i primi N elementi di L1 .
%
% Esempi:
% ?- split([a,b,c,d,e,f,g,h,i,k], 3, L).
%    Yes L = [a,b,c]
%
% Se N è maggiore della lunghezza della lista L1 (si veda secondo esempio sotto), il predicato fallisce.
% ?- split([i,k], 3, L).
%   No

split(_, 0, []) :- !.

split([T|C], N, [T|C2]) :-
    N > 0,
    N1 is N-1,
    split(C, N1, C2).

