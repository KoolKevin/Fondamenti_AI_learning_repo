maggioriLista(_,[],[]).
maggioriLista(K,[H|T],[H|U]) :-
    H>=K,
    maggioriLista(K,T,U),
    !.
maggioriLista(K,[_|T],U) :-
    maggioriLista(K,T,U).

% maggioriLista(5,[4,6,3], X).