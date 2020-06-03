padrede(juan, maria).
padrede(pablo, juan).
padrede(pablo, marcela).
padrede(carlos, debora).
padrede(luisa, debora).
hijode(B, A) :- padrede(A, B).
hermanode(A, C) :- padrede(B, A), padrede(B, C), A\==C.
abuelode(A, C) :- padrede(A, B), padrede(B, C).
familiarde(A, B) :- padrede(A, B).
familiarde(A, B) :- hijode(A, B).
familiarde(A, B) :- hermanode(A, B).
familiarde(A,B) :- abuelode(A,B).
