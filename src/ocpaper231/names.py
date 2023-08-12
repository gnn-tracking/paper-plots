from __future__ import annotations

__all__ = [
    "Variable",
    "VariableManager",
    "variable_manager",
]


class Variable:
    def __init__(self, name: str, latex: str = ""):
        self.name = name
        self._latex = latex

    @property
    def latex(self):
        return self._latex or self.name

    def __str__(self):
        return self.name


class VariableManager:
    def __init__(self):
        self._variables: dict[str, Variable] = {}

    def __getitem__(self, name: str) -> Variable:
        try:
            return self._variables[name]
        except KeyError:
            return Variable(name)

    def add(self, other):
        if isinstance(other, list):
            for var in other:
                self.add(var)
        elif isinstance(other, Variable):
            self._variables[other.name] = other
        elif isinstance(other, tuple):
            self._variables[other[0]] = Variable(*other)
        else:
            msg = f"Cannot add {other} of type {type(other)}"
            raise TypeError(msg)


variable_manager = VariableManager()
variable_manager.add(
    [
        ("frac50", "50SF"),
        ("frac75", "75SF"),
        ("frac100", "100SF"),
        ("efficiency", "Efficiency"),
        ("purity", "Purity"),
        ("double_majority", "DM"),
        ("double_majority_pt0.9", r"DM ($p_T > 0.9\, \mathrm{GeV}$)"),
        ("lhc", "LHC"),
        ("lhc_pt0.9", r"LHC ($p_T > 0.9\, \mathrm{GeV}$)"),
        ("perfect", "Perfect"),
        ("perfect_pt0.9", r"Perfect ($p_T > 0.9\, \mathrm{GeV}$)"),
        ("pt", "$p_T$"),
        ("eta", r"$\eta$"),
    ]
)
for target in ["90", "93", "95", "97"]:
    variable_manager.add(
        (
            f"n_edges_frac_segment50_{target}",
            r"$N_\text{edges}^{50\mathrm{SF}\geq " + target + r"\%}$",
        )
    )
