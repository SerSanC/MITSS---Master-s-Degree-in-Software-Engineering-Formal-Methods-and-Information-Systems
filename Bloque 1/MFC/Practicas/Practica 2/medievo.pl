rufian(bertoldo).
rufian(bartolo).
noble(bertoldo).
noble(romeo).
plebeyo(bartolo).
dama(julieta).
dama(gertrudis).
hermosa(julieta).
desea(A,B):- plebeyo(A), dama(B).
desea(A,B):- noble(A), dama(B), hermosa(B).
raptan(A,B):- rufian(A), desea(A,B).
