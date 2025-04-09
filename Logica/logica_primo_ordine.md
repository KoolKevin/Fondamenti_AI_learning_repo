## Dimostrazioni in logica dei predicati del primo ordine
La logica dei predicati è un linguaggio più potente per esprimere KB
- (variabili e quantificatori)

Vedremo la dimostrazione di teoremi basata su:
- Risoluzione (corretta e completa per clausole generali)
- Forward chaining (corretta e completa per clausole Horn) Usata nei Database deduttivi (DATALOG)
- Backward chaining (corretta e completa per clausole Horn) **Usata nella Programmazione Logica (PROLOG)**.

### trasformazione clausole
Una qualunque fbf della logica dei predicati si può trasformare in un insieme di clausole generali.
- vanno fatte in questo ordine (dimostrato da Robinson)

1. le variabili non dichiarate si assume che sono quantificati universalmente
...

fino ad ora abbiamo solo riscritto applicando le regole degli operatori logici 

7. skolemizzazione
ogni variabile quantificata esistenzialmente viene sostituita da una funzione delle variabili quantificate universalmente che la precedono. Tale funzione è detta funzione di Skolem. 
- si sostituisce "esiste un ..." con il generico "tizio" 
- tizio: funzione delle variabili quantificate universalmente (il tizio che fa lezione a me è diverso del tizio che fa lezione ad uno della 5.6)

**NB**: Siamo sicuri di aver mantenuto il significato della formula originale? NO, abbiamo fatto una specializzazione! siamo partiti da un quantificatore esistenziale e siamo arrivati ad una funzione si Skolem

- non ci cambia troppo se l'obiettivo è dimostrare l'insoddisfacibilità 
- teorema: Vale comunque la proprietà che F è insoddisfacibile se e solo se F’ è insoddisfacibile

8. ...

**NB**: Qualunque teoria del primo ordine T può essere trasformata in una teoria T’ in forma a clausole.
- Anche se T non è logicamente equivalente a T’ (a causa dell'introduzione delle funzioni di Skolem), vale comunque la seguente proprietà 
- teorema: Sia T una teoria del primo ordine e T’ una sua trasformazione in clausole. Allora T è insoddisfacibile se e solo se T’ è insoddisfacibile.
- Ricorda: T è ottenuto come assiomi + una formula negata ~F, se la teoria è insoddisfacibile allora F è conseguenza logica degli assiomi