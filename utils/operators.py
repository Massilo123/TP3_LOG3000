"""Opérations arithmétiques de base utilisées par l'application.

Ce module fournit des implémentations simples pour les opérations
basiques : addition, soustraction, multiplication et division.

Chaque fonction attend deux nombres (a, b) et retourne le résultat
numérique correspondant.

Remarque : les fonctions lèvent des exceptions Python standard lorsque
des cas d'erreur se produisent (par ex. ZeroDivisionError pour la
division par zéro).
"""

def add(a, b):
    """Retourner la somme de a et b.

        Args:
            a (float): Le premier nombre.
            b (float): Le deuxième nombre.

        Returns:
            float: La somme des deux nombres.
    """
    return a + b

def subtract(a,b):
    """
        Soustraire deux nombres.

        Args:
            a (float): Le premier nombre.
            b (float): Le deuxième nombre.

        Returns:
            float: La différence des deux nombres.
    """
    return b - a

def multiply(a,b):
    """
        Multiplier deux nombres.

        Args:
            a (float): Le premier nombre.
            b (float): Le deuxième nombre.

        Returns:
            float: Le produit des deux nombres.
    """
    return a * b

def divide(a,b):
    """
        Diviser deux nombres.

        Args:
            a (float): Le numérateur.
            b (float): Le dénominateur.

        Returns:
            float: Le résultat de la division.

        Raises:
            ZeroDivisionError: Si le dénominateur est zéro.
    """
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a / b
