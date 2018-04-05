"""Author: Stefan Strang - Uni Freiburg."""
import spot


def translate(inp):
    """Translate input to polish pred Logic.

    input: ltl in []<>p0 or p1 U (p2 & GFp3)
    output: ltl in polish notation U p1 & p2 G F p3
    """
    f = spot.formula(inp)
    lbt = f.to_str('lbt')

    return lbt
