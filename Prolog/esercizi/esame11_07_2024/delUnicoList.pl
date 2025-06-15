% Si scriva in Prolog il predicato delUnicoLista(L1,L2), che data una lista L1 di numeri interi, inserisca nella lista L2
% solo gli elementi di L1 che sono seguiti (nel seguito, ovvero nel resto della sequenza) da almeno un altro elemento uguale.
%
% Se L1 è la lista vuota verrà restituita in uscita la lista vuota.
%
% Per verificare se un elemento appartiene a una sequenza (resto) si usi il predicato member/2, definendolo e riportandolo nella soluzione.
%
% Esempio:
%     ?- delUnicoLista([6,2,3,3,5,2,3,1,4] ,X).
%         X = [2, 3, 3]

% member(_, []) :- fail. % questa clausola è superflua, se non riesco ad unificare con niente allora fallisco automaticamente
member(E, [E|_]) :- !.
member(E, [_|T]) :-
    member(E, T).

delUnicoLista([], []).
delUnicoLista([H|T], [H|T2]) :-
    member(H, T),
    !,
    delUnicoLista(T, T2).
delUnicoLista([_|T], L2) :-
    delUnicoLista(T, L2).