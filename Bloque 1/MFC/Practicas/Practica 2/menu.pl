primero(ensalada).
primero(sopa).
primero(revuelto).
segundo(chuleta).
segundo(lubina).
segundo(pollo).
postre(natillas).
postre(flan).
postre(cafe).
comida(X, Y, Z):- primero(X), segundo(Y), postre(Z).
