module Entrega1 where
    import Data.Char
    --Ejercicios a resolver sobre tipos básicos

    -- Ejercicio 1
    siguienteLetra::  Char -> Char
    siguienteLetra 'Z' = 'A'
    siguienteLetra 'z' = 'a'
    siguienteLetra c = chr(ord(c) + 1)
    -- Ejercicio 2
    sumatorio::  (Int, Int) -> Int
    sumatorio(x,y)
        | x < y = x + (sumatorio((x + 1), y))
        | x > y = y + (sumatorio(x, (y + 1)))
        | otherwise = x 
    -- Ejercicio 3
    producto::  (Int, Int) -> Int
    producto(x,y)
        | x < y = x * (producto((x + 1), y))
        | x > y = y * (producto(x, (y + 1)))
        | otherwise = x
    -- Ejercicio 4
    maximo::  (Int, Int) -> Int
    maximo(x,y)
        | x > y = x
        | x < y = y
        | otherwise = x
    -- Ejercicio 5
    fact::  Int -> Int
    fact 1 = 1
    fact x = x * fact(x-1)
    -- Ejercicio 6
    sumaFact::  (Int, Int) -> Int
    sumaFact(x,y)
        | x < y = fact(x) + sumaFact((x+1), y)
        | x > y = fact(y) + sumaFact(x, (y+1))
        | otherwise = fact(x)

    --Ejercicios a resolver sobre tipos listas

    -- Ejercicio 1
    sumarPares::  [(Int, Int)] -> [Int]
    sumarPares [] = []
    sumarPares ((x,y):xs) = (x + y):sumarPares(xs)
    
    -- Ejercicio 2
    primero::[a] -> a
    primero (x:xs) = x

    ultimo::  [a] -> a
    ultimo(x:[]) = x
    ultimo (x:xs) = ultimo(xs)
   
    -- Ejercicio 3
    divisoresDe::  Int -> [Int]
    divisoresDe n = [x | x <- [1..n], n `mod` x == 0]
   
    -- Ejercicio 4
    pertenece::  (Int, [Int]) -> Bool
    pertenece(x,[]) = False
    pertenece(x,(y:ys))
        | x == y = True
        | x /= y = pertenece(x,ys)

    -- Ejercicio 5
    reemplazar::  (Int, Int, [Int]) -> [Int]
    reemplazar(n,p,[]) = []
    reemplazar(n,p,(x:xs))
        | x == n = p:reemplazar(n,p,xs)
        | otherwise = x:reemplazar(n,p,xs)
  
    -- Ejercicio 6
    contar::  (Int,[Int]) -> Int
    contar(x,[]) = 0;
    contar(x,(y:ys))
        | x == y = 1 + contar(x,ys)
        | otherwise = contar(x,ys)

    -- Ejercicio 7
    multiple:: [Int]->[Int]
    multiple [] = [x*5 | x <- [1..10]]

    -- Ejercicio 8
    mayusculas::  [Char] -> [Char]
    mayusculas [] = [];
    mayusculas(x:xs)
        | ord(x) >= ord('A') && ord(x) <= ord('Z') = x:mayusculas(xs)
        | otherwise = mayusculas(xs)