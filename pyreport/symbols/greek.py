from pyreport.symbols import Symbol, SymbolCollection
from pyreport._utils import Switch

__all__ = [
    "DEFAULT_VAREPSILON",
    "DEFAULT_VARTHETA",
    "DEFAULT_VARPI",
    "DEFAULT_VARRHO",
    "DEFAULT_VARPHI",
    "Greeks",
]

DEFAULT_VAREPSILON = Switch("DEFAULT_VAREPSILON", True, False)
"""Switch out the default LaTeX command for epsilon with the alternate one (varepsilon)."""

DEFAULT_VARTHETA = Switch("DEFAULT_VARTHETA", False, True)
"""Switch out the default LaTeX command for theta with the alternate one (vartheta)."""

DEFAULT_VARPI = Switch("DEFAULT_VARPI", False, True)
"""Switch out the default LaTeX command for pi with the alternate one (varpi)."""

DEFAULT_VARRHO = Switch("DEFAULT_VARRHO", False, True)
"""Switch out the default LaTeX command for rho with the alternate one (varrho)."""

DEFAULT_VARPHI = Switch("DEFAULT_VARPHI", True, False)
"""Switch out the default LaTeX command for phi with the alternate one (varphi)."""


class Greeks(SymbolCollection):
    _members = {
        ##################### SMALL LETTERS #####################
        "alpha": Symbol("alpha", r"\alpha"),
        "beta": Symbol("beta", r"\beta"),
        "gamma": Symbol("gamma", r"\gamma"),
        "delta": Symbol("delta", r"\delta"),
        "epsilon": Symbol("epsilon", r"\epsilon", r"\varepsilon", DEFAULT_VAREPSILON),
        "varepsilon": Symbol(
            "varepsilon", r"\varepsilon", r"\epsilon", DEFAULT_VAREPSILON
        ),
        "zeta": Symbol("zeta", r"\zeta"),
        "eta": Symbol("eta", r"\eta"),
        "theta": Symbol("theta", r"\theta", r"\vartheta", DEFAULT_VARTHETA),
        "vartheta": Symbol("vartheta", r"\vartheta", r"\theta", DEFAULT_VARTHETA),
        "iota": Symbol("iota", r"\iota"),
        "kappa": Symbol("kappa", r"\kappa"),
        "lambda": Symbol("lambda", r"\lambda"),
        "mu": Symbol("mu", r"\mu"),
        "nu": Symbol("nu", r"\nu"),
        "xi": Symbol("xi", r"\xi"),
        "pi": Symbol("pi", r"\pi", r"\varpi", DEFAULT_VARPI),
        "varpi": Symbol("varpi", r"\varpi", r"\pi", DEFAULT_VARPI),
        "rho": Symbol("rho", r"\rho", r"\varrho", DEFAULT_VARRHO),
        "varrho": Symbol("varrho", r"\varrho", r"\rho", DEFAULT_VARRHO),
        "sigma": Symbol("sigma", r"\sigma"),
        "tau": Symbol("tau", r"\tau"),
        "upsilon": Symbol("upsilon", r"\upsilon"),
        "phi": Symbol("phi", r"\phi", r"\varphi", DEFAULT_VARPHI),
        "varphi": Symbol("varphi", r"\varphi", r"\phi", DEFAULT_VARPHI),
        "chi": Symbol("chi", r"\chi"),
        "psi": Symbol("psi", r"\psi"),
        "omega": Symbol("omega", r"\omega"),
        ##################### CAPITAL LETTERS #####################
        "Gamma": Symbol("Gamma", r"\Gamma"),
        "Delta": Symbol("Delta", r"\Delta"),
        "Theta": Symbol("Theta", r"\Theta"),
        "Lambda": Symbol("Lambda", r"\Lambda"),
        "Xi": Symbol("Xi", r"\Xi"),
        "Pi": Symbol("Pi", r"\Pi"),
        "Sigma": Symbol("Sigma", r"\Sigma"),
        "Upsilon": Symbol("Upsilon", r"\Upsilon"),
        "Phi": Symbol("Phi", r"\Phi"),
        "Psi": Symbol("Psi", r"\Psi"),
        "Omega": Symbol("Omega", r"\Omega"),
    }

    @classmethod
    def get_members(cls):
        return super(Greeks, cls).get_members()
    
    @classmethod
    def list_members(cls):
        super(Greeks, cls).list_members()
