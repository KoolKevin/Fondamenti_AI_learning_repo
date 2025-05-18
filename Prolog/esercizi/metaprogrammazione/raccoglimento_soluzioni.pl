% I predicati setof, bagof e findall funzionano anche se le proprietà che vanno a controllare non sono definite da fatti, ma da regole.
p(X,Y):- q(X),r(X),c(Y).
q(0).
q(1).
r(0).
r(2).
c(1).
c(2).


% - Esercizio: raccogliere le soluzioni X per la chiamata p(X,Y) (per qualsiasi Y)



% - Esercizio: raccogliere le soluzioni (X,Y) per la chiamata p(X,Y).