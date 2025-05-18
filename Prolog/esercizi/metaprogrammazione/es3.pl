% Data una matrice M (come lista di liste) si scriva un un predicato constant(M,C) che è vero se
% C è un numero che compare in ciascuna riga della matrice M.

% Esempio:
% ?- constant (
%   [[4, 9, 23, 55, 63, 107, 239],
%   [5, 9, 31, 55, 60, 73, 82, 99, 107],
%   [9, 23, 55, 107, 128, 512],
%   [6, 9, 13, 17, 22, 55, 63, 107 ]],
%   9).
% Yes
%
% ?- constant (
%   [[4, 9, 23, 55, 63, 107, 239],
%   [5, 9, 31, 55, 60, 73, 82, 99, 107],
%   [9, 23, 55, 107, 128, 512],
%   [6, 9, 13, 17, 22, 55, 63, 107 ]],
%   60).
% No

constant(Matrice, Const) :-
    findall(Riga, (member(Riga, Matrice), member(Const, Riga)), RigheValide),
    write(RigheValide), nl,
    RigheValide == Matrice.



% questa soluzione è invertibile ma sporca per il caso della matrice vuota
% constant([], _).
% constant([R|Rs], C) :-
%     member(C, R),
%     constant(Rs, C).