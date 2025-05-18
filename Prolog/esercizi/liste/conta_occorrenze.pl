% conta(T,L,N) “N è il numero di occorrenze del termine T nella lista L”
% 
% Esempio:
% ?- conta(a, [b,a,a,b,c,a], N).
%   N = 3;
%   no
% ?- conta(a, [b,a,a,b,c,a], 3).
%   yes

% conta(_, [], 0).
% conta(El, [El|Coda], N) :- 
%     % !, questo cut mi garantisce la mutua esclusione tra le clausole
%     conta(El, Coda, N1),
%     N is N1+1.
% conta(El, [_|Coda], N) :-
%     conta(El, Coda, N).
% in alternativa al cut posso forzare la non unificazione... sono però ridondante
% conta(El, [T|Coda], N) :-
%     El \= T,
%     conta(El, Coda, N).


%%% versione tail-ricorsiva %%%
conta(El, Lista, N) :- conta(El, Lista, N, 0).

conta(_, [], Acc, Acc).
conta(El, [El|Coda], N, Acc) :- 
    !, % questo cut mi garantisce la mutua esclusione tra le clausole
    Acc1 is Acc+1,
    conta(El, Coda, N, Acc1).
conta(El, [_|Coda], N, Acc) :-
    conta(El, Coda, N, Acc).

