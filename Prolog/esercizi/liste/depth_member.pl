% depth_member(T,L) "T appartiene alla lista L o, ricorsivamente, ad una lista che appartiene a L"
%
% Esempi:
% ?- depth_member(b, [a,b,[c,a],d]).
%   Yes
% ?- depth_member([c,a], [a,b,[c,a],d]).
%   Yes
% ?- depth_member(X, [a,b,[c,a],d]).
%   X=a ;
%   X=b ;
%   ...

depth_member(El, [El|_]).
depth_member(El, [Testa|_]) :-
    is_list(Testa),
    depth_member(El, Testa).
depth_member(El, [_|Coda]) :- 
    depth_member(El, Coda).



