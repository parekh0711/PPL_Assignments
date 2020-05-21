/*Flight Management System */


path(toronto,london,air_canada,500,360).
path(toronto,london,united,650,420).
path(toronto,madrid,air_canada,900,480).
path(toronto,madrid,united,950,540).
path(toronto,madrid,iberia,800,480).
path(madrid,toronto,air_canada,900,480).
path(madrid,toronto,united,950,540).
path(madrid,toronto,iberia,800,480).
path(madrid,barcelona,air_canada,100,60).
path(madrid,barcelona,iberia,120,65).
path(madrid,valencia,iberia,40,20).
path(madrid,malaga,iberia,50,60).
path(malaga,madrid,iberia,50,60).
path(malaga,valencia,iberia,80,120).
path(barcelona,madrid,air_canada,100,60).
path(barcelona,madrid,iberia,120,65).
path(barcelona,valencia,iberia,110,75).
path(barcelona,london,iberia,220,240).
path(valencia,madrid,iberia,40,20).
path(valencia,barcelona,iberia,110,75).
path(valencia,malaga,iberia,80,120).
path(london,barcelona,iberia,220,240).
path(london,toronto,air_canada,500,360).
path(london,toronto,united,650,420).
path(paris,toulouse,united,35,120).
path(toulouse,paris,united,35,120).


taxsec(toronto,50,60).
taxsec(madrid,75,45).
taxsec(malaga,50,30).
taxsec(barcelona,40,30).
taxsec(valencia,40,20).
taxsec(london,75,80).
taxsec(paris,50,60).
taxsec(toulouse,40,30).

:- initialization(main).
main :- write('                      *******Airline System*******').

printDetails(A, B, Airline, Duration,Price):-
   nl,write('Departure city: '),
   nl,write(A),
   nl,write('Arrival city: '),
   nl,write(B),
   nl,write('Airline:'),
   nl,write(Airline),
   nl,write('Duration in minutes:'),
   nl,write(Duration),
   nl,write('Price in dollars:'),
   nl,write(Price).

%Prints All flights from A to B
flights(A,B):-
  checkPath(A,B),
  checkPath(B,A).

checkPath(From,To):-
  nl,write('Checking flight availability......'),
  path(From,To,Airline,Duration,Price),
  printDetails(From,To,Airline,Duration,Price).

%Prints Yes if it finds flight
isFlight(A,B) :-
  path(A,B,C,D,E);
  path(B,A,C,D,E).

%Prints Airport details
airport(A):-
  taxsec(A,Tax,Delay),
  nl,write('Airport :'),
  nl,write(A),
  nl,write('Tax :'),
  nl,write(Tax),
  nl,write('Delay :'),
  nl,write(Delay).

%Checks Indirect flights upto 2 times
checkIndirect(A,B):-
  path(A,B,D,E,F);
  path(A,C,G,H,I),
  path(C,B,J,K,L).

%checks for cheap flight
cheap(A,B):-
  path(A,B,C,D,E),(D<400).
  
%Checks for cheap flight or Airline W
cheaporconditional(A,B,W) :-
  path(A,B,C,D,E),(D<400);
  path(A,B,W,F,G).

%Checks if path exists between A and B for both C and D
checkExist(A,B,C,D):-
  path(A,B,C,E,F),
  path(B,A,D,G,H).
