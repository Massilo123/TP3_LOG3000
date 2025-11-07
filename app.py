from flask import Flask, request, render_template
from operators import add, subtract, multiply, divide

app = Flask(__name__)

OPS = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

def calculate(expr: str):
    """Calcule le résultat d'une expression binaire de type "<nombre><opérateur><nombre>".

    Paramètres
    ----------
    expr : str
        Chaîne provenant de l'utilisateur, censée contenir exactement un opérateur parmi OPS.

    Retour
    ------
    float
        Résultat numérique obtenu après conversion des opérandes et application de l'opérateur.

    Exceptions
    ----------
    ValueError
        Levée si l'expression est vide, mal placée, comporte plusieurs opérateurs
        ou si les opérandes ne sont pas convertibles en nombres flottants.
    """
    if not expr or not isinstance(expr, str):
        raise ValueError("empty expression")

    s = expr.replace(" ", "")

    op_pos = -1
    op_char = None

    # On mémorise la position de l'opérateur en s'assurant qu'il n'y en ait qu'un seul.
    for i, ch in enumerate(s):
        if ch in OPS:
            if op_pos != -1:
                raise ValueError("only one operator is allowed")
            op_pos = i
            op_char = ch

    if op_pos <= 0 or op_pos >= len(s) - 1:
        # operator at start/end or not found
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
    """Afficher l'interface de la calculatrice et traiter l'expression soumise."""
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