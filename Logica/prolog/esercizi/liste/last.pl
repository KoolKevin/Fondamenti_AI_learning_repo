
% last(L,X) "X è l’ultimo elemento della lista L"
% 
% Esempi:
% ?- last([a,b,c],N).
%   X = c;
%   no
% ?- last([a,b,[c,d,e]],X).
%   X = [c,d,e];
%   no

last([X], X).
last([_ | Coda], X) :- last(Coda, X).