#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thur Feb  8 17:45:19 2019

@author: anthonypierrat
"""
import math
from StringIntegerBijection import StringIntegerBijection

"""
 Calcul l'exponentiation modulaire rapide
 params: x base, k exposant, n modulo
 return: integer
"""
def exponentiationModulaire(x, k, n):

    # transformer la puissance en binaire
    k = bin(k)[2:]
    # récupérer la longueur du string en binaire (enlever Ob)
    len_k = len(k)
    result = 1
    
    # parcourir l'écriture binaire
    for i in range(len_k - 1, -1, -1):
        result = (result * x ** int(k[i])) % n
        x = (x ** 2) % n
    return result
    
"""
 Calcul de l'euclide etendu
 params: a, b integer
 return: les coéfficients de Bézout
"""
def euclideEtendu(a, b):
    r, u, v = a, 1, 0
    r1, u1, v1 = b, 0, 1
    
    while r1 != 0:
        q = r//r1
        r, u, v, r1, u1, v1 = r1, u1, v1, (r - q*r1), (u - q*u1), (v - q*v1)
    
    return r, u, v

"""
 Permet de savoir si deux nombres sont premiers entre eux
 params: a integer, b integer
 return: boolean
"""
def premierEntreEux(a, b):
    return True if euclideEtendu(a, b)[0] == 1 else False

"""
 Calcul de l'inverse modulaire
 params: a integer, N integer
 return: integer
"""
def InverseModulaire(a, N):
    
    # vérifier s'ils sont premiers entre eux
    if not premierEntreEux(a, N):
        return '{a} et {N} ne sont pas premier entre eux !'
    # retourner le coefficient u d'euclide etendu avec Bézout
    else:
        return euclideEtendu(a, N)[1]
"""
 Génération des exposants p, q
 params: a integer, N integer
 return: clé chiffrement, clé déchiffrement array integer
"""      
def generationExposants(p, q):
    
    phi = (p-1)*(q-1)
    for i in range(100, phi//2):
        if (euclideEtendu(i, phi)[0] == 1):
            exposantChiffrement = i
            break
    
    exposantDechiffrement = InverseModulaire(exposantChiffrement, phi)
    
    return exposantChiffrement, exposantDechiffrement

"""
 Calcul du module de chiffrement
 params: p integer, q integer
 return: integer
"""
def moduleChiffrement(p, q):
    return p*q

"""
 Chiffrement d'un message
 params: m (message), n (module chiffrement), c (clé chiffrement)
 return: integer
"""
def chiffrement(m, n, c):
    # m2 = m1^c1 (mod n1)
    return exponentiationModulaire(m, c, n)

"""
 Déchiffrement d'un message
 params: m (message), n (module chiffrement), d (clé déchiffrement)
 return: integer
"""
def dechiffrement(m, n, d):
    # m1 = m2^d1 (mod n1)
    return exponentiationModulaire(m, d, n)

"""
 Calcul pour trouver (p,q)
 params: n integer
 return: array integer
"""
def listeDiviseurs(n):
    p = 0
    for i in range(2, int(math.sqrt(n))):
        if ((n % i) == 0):
            p = i
    q = int(n/p)
    return p,q
   
"""
 Decodage d'un message
 params: m string, n interger, c integer
 return: string (message décodé)
"""
def decodageMessage(m, n, c):
    util = StringIntegerBijection()
    
    # trouver p et q
    p, q = listeDiviseurs(n)
    # calcul du module de chiffrement
    moduleC = moduleChiffrement(p,q)
    
    # calcul clé de déchiffrement
    d = InverseModulaire(c, (p-1)*(q-1))
    # si clé négatif
    if (d < 0):
        d1 = d % ((p-1)*(q-1))
        # déchiffrement
        m = dechiffrement(util.StringToInteger(m), moduleC, d1)
    else:
        # déchiffrement
        m = dechiffrement(util.StringToInteger(m), moduleC, d)
    
    return util.IntegerToString(m)