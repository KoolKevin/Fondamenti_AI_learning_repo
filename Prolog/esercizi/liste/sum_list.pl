% sum_list(L,S) "S è la somma degli elementi della lista L data"
% % Esempi:
% ?- sum_list([1,2,3], 6).
%   Yes
% ?- sum_list([1,2,3], X).
%   Yes X=6

% sum_list([], 0).
% sum_list([Testa|Coda], Somma) :-
%     sum_list(Coda, SommaCoda),
%     Somma is SommaCoda + Testa.



%%% versione tail ricorsiva %%%


sum_list(List, Ris) :- sum_list(List, Ris, 0).

sum_list([], Acc, Acc).
sum_list([Testa|Coda], Ris, Acc) :-
    Acc1 is Acc + Testa,
    sum_list(Coda, Ris, Acc1).