% Si definisca prima la versione ricorsiva e poi quella tail-ricorsiva di un predicato media che ritorni la media M
% di uno studente S data una lista di esami superati L.
%
% Ogni esame è rappresentato da un termine della lista L della forma: esame(ID, Studente, Voto)
%
% Ad esempio, la query:
%     ?- media(s1, [esame(e1,s1,27), esame(e1,s2,30), esame(e1,s3,25), esame(e2,f2,30)], M).
% restituirà:
%     yes, M = 28.5

media(S, E, M) :-
    totale(S, E, TOT, NUM),
    writeln(TOT), writeln(NUM),
    M is TOT/NUM.

totale(_, [], 0, 0) :- !.
totale(S, [esame(_, S, V)|T], TOT, NUM) :- 
    !,
    totale(S, T, TOT1, NUM1),
    TOT is TOT1 + V,
    NUM is NUM1+1.
totale(S, [_|T], TOT, NUM) :-
    totale(S, T, TOT, NUM).