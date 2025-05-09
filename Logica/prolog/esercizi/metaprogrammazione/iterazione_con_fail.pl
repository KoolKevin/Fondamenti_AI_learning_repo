itera :- call(p(X)),
    verifica(q(X)),
    write(X),nl,
    fail.
    itera.

verifica(q(X)):- call(q(X)), !. % qua il cut mi taglia eventuali punti di scelta di call(q(x))
    
p(1).
p(2).
p(3).
    
q(1).
q(3).