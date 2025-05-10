p(1).
q(X,a) :- p(X), r(a).
q(2,Y) :- d(Y).

% ?- clause(p(1),BODY).
%     yes BODY=true
% ?- clause(p(X),true).
%     yes X=1
% ?- clause(q(X,Y), BODY).
%     yes X=_1 Y=a BODY=p(_1),r(a);
%     X=2 Y=_2 BODY=d(_2);
%     no
% ?- clause(HEAD,true).
%     Error - invalid key to data-base