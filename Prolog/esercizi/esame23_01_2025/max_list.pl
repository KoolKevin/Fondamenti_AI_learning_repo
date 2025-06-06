% Si scriva un predicato Prolog max(L1, L2, L3) che, date in ingresso le liste L1 e L2 di interi della stessa lunghezza,
% restituisce nella lista L3 gli interi che sono il massimo tra gli elementi di L1 ed L2 di posizione corrispondente.
%
% Se le liste L1 e L2 sono di diversa lunghezza il predicato fallisce.
%
% Esempi:
% ?- max([4,7,9], [2,12,6], L).
%   Yes L = [4, 12, 9]
% ?-max([4,7,9], [2,12], L).
%   No

max([], [], []).

max([A|T1], [B|T2], [A|T3]) :- 
    A > B,
    !,
    max(T1, T2, T3).

max([_|T1], [B|T2], [B|T3]) :-
    max(T1, T2, T3).