% Dato un insieme di studenti e i voti ottenuti negli esami, rappresentati come fatti del tipo:
%     studente(Nome, Voto).
% si definisca il predicato studMedia(Nome,Media) che dato il nome di uno studente (Nome) ne determina la media in Media.

studente(lucia,31).
studente(carlo,18).
studente(carlo,22).
studente(lucia,30).

studMedia(Stud, Media) :-
    findall(Voto, studente(Stud, Voto), ListaVoti),
    calcolaMedia(ListaVoti, Media).

calcolaMedia([], 0) :- !.
calcolaMedia(ListaVoti, Media) :-
    calcolaSomma(ListaVoti, Somma),
    length(ListaVoti, N),
    Media is Somma / N.

calcolaSomma([], 0).
calcolaSomma([Voto | Resto], Somma) :- 
    calcolaSomma(Resto, Somma1),
    Somma is Voto + Somma1.




% ?-studMedia(carlo,M).
%     M=20