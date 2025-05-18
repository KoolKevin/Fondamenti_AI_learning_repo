p(1).
p(2).
p(0).
p(1).
q(2).
r(7).


% :- setof(X,p(X),S).
% :- bagof(X,p(X),S).

% NOTA: la variabile X alla fine della valutazione non è legata a nessun valore. Provate il goal:
% ?- bagof(X,p(X),S),write(X), nl.

% NOTA: Il primo argomento può essere un termine complesso (non solo una variabile)
% :- setof(f(X), p(X), S).
% :- bagof(p(X), p(X), S).
