"""Opérations arithmétiques élémentaires utilisées par la calculatrice Flask."""

def add(a,b):
    """Retourner la somme des deux opérandes."""
    return a + b

def subtract(a,b):
    """Retourner la différence en calculant le second opérande moins le premier."""
    return b - a

def multiply(a,b):
    """Retourner le résultat de l'élévation du premier opérande à la puissance du second."""
    return a ** b

def divide(a,b):
    """Retourner le quotient réel obtenu en divisant le premier opérande par le second."""
    return a / b
