hombre(alfredo).
hombre(felipe).
hombre(francisco).
hombre(pepe).
mujer(sonia).
mujer(eva).
mujer(carmen).
mujer(elena).

bebe(alfredo, whisky).
bebe(alfredo, ron_cola).
bebe(felipe, cerveza).
bebe(felipe, gin_tonic).
bebe(felipe,ron_cola).
bebe(francisco, vino).
bebe(francisco, malibu).
bebe(sonia, gin_tonic).
bebe(sonia, malibu).
bebe(eva, vino).
bebe(eva, cerveza).
bebe(carmen, whisky).
bebe(carmen, ron_cola).


bebe(pepe,X) :- bebe(alfredo,X).
bebe(elena,X) :- bebe(felipe,X).
bebe(elena,X) :- bebe(sonia,X).

pareja(A,B) :- bebe(A, X), bebe(B,X), hombre(A) , mujer(B).
