"""
Ce module constitue le point d'entrée de l'application web pour le
projet de calculatrice simple.

Il expose une petite application Flask qui rend un formulaire web et
évalue des expressions arithmétiques très simples de la forme "<num> <op> <num>".

Responsabilités :
- Définir l'instance Flask `app`.
- Analyser et évaluer une expression arithmétique binaire unique via `calculate`.
- Rendre la page principale et afficher les résultats.

Hypothèses :
- Les expressions contiennent exactement deux opérandes et un seul opérateur parmi
    l'ensemble {+ - * /}.
"""

from flask import Flask, request, render_template
from utils.operators import add, subtract, multiply, divide

app = Flask(__name__)

# Mapping des opérateurs aux fonctions correspondantes.
OPS = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide,
}

def calculate(expr: str):
    """
        Évaluer une expression mathématique simple sous la forme "a op b". En fonction de l'opérateur, on appelle la bonne fonction.
        Ne permet qu'un seul opérateur parmi +, -, *, /.
        

        Args:
            expr (str): L'expression mathématique à évaluer.

        Returns:
            float: Le résultat de l'évaluation.

        Raises:
            ValueError: Si l'expression est vide, mal formée, ou si les opérandes ne sont pas des nombres.
            ZeroDivisionError: Si une division par zéro est tentée.

        Examples:
            >>> calculate("3 + 5")
            8.0
            >>> calculate("10 / 2")
            5.0
    """
    if not expr or not isinstance(expr, str):
        raise ValueError("empty expression")

    # Supprimer les espaces pour simplifier l'analyse. On s'attend à une forme compacte comme "3+4" ou
    # une forme espacée comme "3 + 4"; la suppression des espaces garde la logique d'analyse simple.
    s = expr.replace(" ", "")

    op_pos = -1
    op_char = None

    # Trouver la position de l'opérateur dans la chaîne. Les expressions avec plusieurs opérateurs sont
    # considérées comme invalides pour cette calculatrice simple (pas de priorité des opérateurs).
    for i, ch in enumerate(s):
        if ch in OPS:
            if op_pos != -1:
                raise ValueError("only one operator is allowed")
            op_pos = i
            op_char = ch

    # L'opérateur ne doit pas être au début ou à la fin; les opérandes doivent exister des deux côtés.
    if op_pos <= 0 or op_pos >= len(s) - 1:
        raise ValueError("invalid expression format")

    left = s[:op_pos]
    right = s[op_pos+1:]

    try:
        a = float(left)
        b = float(right)
    except ValueError:
        raise ValueError("operands must be numbers")

    return OPS[op_char](a, b)

@app.route('/', methods=['GET', 'POST'])
def index():
    """
        Gérer la page principale de l'application web. Afficher le formulaire et traiter les soumissions.
        Args:
            None

        Returns:
            str: Le rendu HTML de la page principale avec le résultat de l'évaluation si applicable.    
    """
    result = ""
    if request.method == 'POST':
        expression = request.form.get('display', '')
        try:
            result = calculate(expression)
        except Exception as e:
            result = f"Error: {e}"
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)