gioco asimmetrico
- il giocatore da implementare deve essere capace di coprire il ruolo sia del nero che del bianco

max 1 minuto per ogni mossa

variante di alfabeta -> negamax

un server fà da aribtro centrale e mantiene lo stato del gioco
- invia lo stato del gioco
- raccoglie le mosse dei giocatori
- invia i timeout
- i messaggio sono stringhe json
- le primitive read e send sono bloccanti
    - nel caso della send è superveloce
    - nel caso della read ci si blocco al massimo per un minuto (aspetto il turno dell'altro giocatore)

Abbiamo dei constraint hard e dei constraint soft
- il ruolo è case sensitive
- il timeout in secondi
    - non è sempre detto che siano 60 secondi spaccati, scrivere qualcosa d robusto
    - è intelligente avere un thread separato che calcola la mossa ed un thread che invia messaggi riguardanti il tempo mancante
- l'ip del server deve essere parametrico

**DEADLINE: 25 maggio!**

ci si può ritirare mandando una mail


ricorda di specificare nella mail di verbalizzazione dell'esame il fatto di avere fatto tablut per prendere il punto