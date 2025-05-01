% “Concepts” we would like to represent:
% • Male
% • Female

male('George').
male('Philip').
male('Charles').
male('Kydd').
male('Mark').
male('Andrew').
male('Edward').
female('Mum').
female('Spencer').
female('Elizabeth').
female('Margaret').
female('Diana').
female('Anne').
female('Sarah').
female('Sophie').

% • Parent
% • Father
% • Mother
genitore('George', 'Elizabeth').
genitore('George', 'Margaret').
genitore('Mum', 'Elizabeth').
genitore('Mum', 'Margaret').
genitore('Spencer', 'Diana').
genitore('Kydd', 'Diana').
genitore('Elizabeth', 'Charles').
genitore('Elizabeth', 'Anne').
genitore('Elizabeth', 'Andrew').
genitore('Elizabeth', 'Edward').
genitore('Philip', 'Charles').
genitore('Philip', 'Anne').
genitore('Philip', 'Andrew').
genitore('Philip', 'Edward').

padre(X, Y) :- male(X), genitore(X, Y). 
madre(X, Y) :- female(X), genitore(X, Y). 

% • Sibling
% • Brother
% • Sister

sibling(X, Y) :- genitore(Z, X), genitore(Z, Y), X\==Y. % nota: diverso mettere il controllo sulla diversità all'inizio o alla fine
fratello(X, Y) :- sibling(X, Y), male(X). % conta l'ordine per l'efficienza?
sorella(X, Y) :- sibling(X, Y), female(X).

% • Child
% • Daughter
% • Son



% • Spouse
% • Wife
% • Husband


% • Granparent
% • Grandchild
% • Cousin
% • Aunt
% • Uncle
% • Greatgrandparent
% • Ancestor
% • FirstCousin
% • BrotherInLaw
% • SisterInLaw