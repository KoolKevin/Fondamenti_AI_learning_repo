isPrime(2).
isPrime(N) :- N>2, TheDiv is N-1, cannotBeDividedBy(N, TheDiv).

cannotBeDividedBy(N, 2) :-
    1 is N mod 2.
cannotBeDividedBy(N, TheDiv) :-
    TheDiv>2,
    Rest is N mod TheDiv,
    Rest > 0,
    TheNextDiv is TheDiv-1,
    cannotBeDividedBy(N, TheNextDiv).