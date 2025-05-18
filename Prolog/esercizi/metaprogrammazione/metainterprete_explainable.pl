p(X) :- q(X).
q(1).
q(2).

solve(true):- !.
solve((A,B)):- !, solve(A), solve(B).
solve(A) :-
    write('Solving: '), write(A), nl,
    clause(A,B),
    write('Selected Rule: '), write(A), write(":-"), write(B), nl,
    solve(B),
    write('Solved: '), write(B), nl.

% ?- solve(p(X)).