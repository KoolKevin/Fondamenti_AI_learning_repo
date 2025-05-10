% Si definisca un predicato prodotto_cartesiano(L1,L2,L3) che, date due liste qualsiasi L1 e L2 
% restituisca la lista L3 delle coppie ordinate che si possono formare con elementi di L1 e L2.
% 
% Per esempio:
% ?-prodotto_cartesiano([a,b,c],[a,d],L3)
%   L3=[(a,a),(a,d),(b,a),(b,d),(c,a),(c,d)]


prodotto_cartesiano(L1, L2, L3) :-
    findall((A, B), ( member(A, L1), member(B, L2) ), L3). % il trucco era usare una congiunzione nel findall 








