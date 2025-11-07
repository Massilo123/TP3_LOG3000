"""Tests de régression pour la calculatrice Flask."""

from pathlib import Path

import pytest
import re

from app import calculate


def test_addition():
    """Vérifie que 2 + 3 retourne 5."""
    assert calculate("2+3") == 5


def test_subtraction():
    """Contrôle que 5 - 2 retourne 3."""
    assert calculate("5-2") == 3


def test_multiplication():
    """S'assure que 2 * 3 retourne 6."""
    assert calculate("2*3") == 6


def test_division():
    """Confirme que 5 / 2 retourne 2.5."""
    assert calculate("5/2") == 2.5


def test_multiple_operators():
    """Valide que l'analyse rejette une expression avec plusieurs opérateurs."""
    with pytest.raises(ValueError):
        calculate("1+2-3")


def test_button_labels_match_values():
    """Vérifie que chaque bouton numérique affiche le même texte que la valeur transmise au script."""
    template = (Path("templates") / "index.html").read_text(encoding="utf-8")
    matches = re.findall(r'appendToDisplay\(\'([^\']+)\'\)">([^<]*)</button>', template)
    label_map = {value: label for value, label in matches}

    for digit in map(str, range(10)):
        assert digit in label_map, f"Bouton {digit} introuvable dans le gabarit"
        assert label_map[digit] == digit, f"Bouton {digit} affiche « {label_map[digit]} »"


def test_operator_buttons_have_labels():
    """S'assure que les boutons opérateurs possèdent un libellé visible."""
    template = (Path("templates") / "index.html").read_text(encoding="utf-8")
    matches = re.findall(r'appendToDisplay\(\'([^\']+)\'\)">([^<]*)</button>', template)
    label_map = {value: label for value, label in matches}

    for operator in ["+", "-", "*", "/"]:
        assert operator in label_map, f"Bouton {operator} non trouvé"
        assert label_map[operator].strip(), f"Bouton {operator} sans texte visible"

