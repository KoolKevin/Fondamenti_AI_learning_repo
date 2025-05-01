% Si scriva un programma Prolog no_dupl(Xs,Ys) che è vero se Ys è la lista senza duplicazioni degli elementi che compaiono nella lista Xs.
%
% Nella lista Ys gli elementi compaiono nello stesso ordine di Xs ed, in caso di elementi duplicati, si manterrà l'ultima occorrenza.
%
% Esempi:
% ?-no_dupl([a,b,a,d],[b,a,d]).
%    yes
% ?-no_dupl([a,b,a,c,d,b,e], L).
%   yes L=[a,c,d,b,e]

no_dupl([], []).

no_dupl([T | C], Ris) :-
    member(T, C),
    no_dupl(C, Ris).
    
% no_dupl([T | C], Ris) :-
%     \+ member(T, C),
%     append([T], Ris1, Ris), % questo mi produce Ris = [T|Ris1] e poi mi risolve Ris1 sotto 
%     no_dupl(C, Ris1).

% oppure senza append
no_dupl([T | C], [T | Ris]) :-
    \+ member(T, C),
    no_dupl(C, Ris).








%%% soluzione senza negazione %%%
% no_dupl([], []).

% no_dupl([X|Xs], Ys):-
%     member(X, Xs),
%     no_dupl(Xs, Ys).

% no_dupl([X|Xs], [X|Ys]):-
%     nonmember(X, Xs),
%     no_dupl(Xs, Ys).


% nonmember(_, []).

% nonmember(X, [Y|Ys]) :- X \== Y,
%     nonmember(X, Ys).