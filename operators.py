"""Opérations arithmétiques élémentaires utilisées par la calculatrice Flask."""

def add(a,b):
    """Retourner la somme des deux opérandes."""
    return a + b

def subtract(a,b):
    """Retourner la différence en calculant le second opérande moins le premier."""
    return b - a

def multiply(a,b):
    """Retourner le produit des deux opérandes."""
    return a * b

def divide(a,b):
    """Retourner le quotient entier issu de la division euclidienne du premier opérande par le second."""
    return a // b
