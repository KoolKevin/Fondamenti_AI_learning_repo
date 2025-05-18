% Dato il predicato constant/2, definire ora un predicato constant1(M,L) che data la matrice M
% restituisce la lista L dei numeri che compaiono in ciascuna riga della matrice.

% Esempio:
%     ?-constant1(
%     [[4, 9, 23, 55, 63, 107, 239],
%     [5, 9, 31, 55, 60, 73, 82, 99, 107],
%     [9, 23, 55, 107, 128, 512],
%     [6, 9, 13, 17, 22, 55, 63, 107 ]], CC).

%     Yes CC = [ 9, 55, 107 ]


constant([], _).
constant([R|Rs], C) :-
    member(C, R),
    constant(Rs, C).

constant1([], []).
constant1(Matrice, ListaConsts) :-
    findall(C, constant(Matrice, C), ListaConsts).