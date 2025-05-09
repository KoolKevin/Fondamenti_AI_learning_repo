p(1).
p(2).
q(1).
q(2).
r(1).
k(3).

if_then_else(Cond,Goal1,_):-
    call(Cond),
    !,
    call(Goal1).

if_then_else(_,_,Goal2):-
    call(Goal2).

% ?- if_then_else((q(X),p(X)),r(X),k(X)).