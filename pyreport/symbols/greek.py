"""A module providing the Greek alphabet as symbols."""

from pyreport.symbols import Symbol, SymbolCollection
from pyreport.utils import Switch

__all__ = [
    "DEFAULT_VAREPSILON",
    "DEFAULT_VARTHETA",
    "DEFAULT_VARPI",
    "DEFAULT_VARRHO",
    "DEFAULT_VARPHI",
    "Greeks",
]

DEFAULT_VAREPSILON = Switch("DEFAULT_VAREPSILON", True, False)
"""Switch out the default LaTeX command for epsilon with the alternate one (varepsilon). Default is True."""

DEFAULT_VARTHETA = Switch("DEFAULT_VARTHETA", False, True)
"""Switch out the default LaTeX command for theta with the alternate one (vartheta). Default is False."""

DEFAULT_VARPI = Switch("DEFAULT_VARPI", False, True)
"""Switch out the default LaTeX command for pi with the alternate one (varpi). Default is False."""

DEFAULT_VARRHO = Switch("DEFAULT_VARRHO", False, True)
"""Switch out the default LaTeX command for rho with the alternate one (varrho). Default is False."""

DEFAULT_VARPHI = Switch("DEFAULT_VARPHI", True, False)
"""Switch out the default LaTeX command for phi with the alternate one (varphi). Default is True."""


class Greeks(SymbolCollection):
    """A collection containing the Greek alphabet as symbols.

    Attributes
    ----------
    alpha : Symbol
        The symbol for the small greek letter alpha.
    beta : Symbol
        The symbol for the small greek letter beta.
    gamma : Symbol
        The symbol for the small greek letter gamma.
    delta : Symbol
        The symbol for the small greek letter delta.
    epsilon : Symbol
        The symbol for the small greek letter epsilon (depends on DEFAULT_VAREPSILON).
    varepsilon : Symbol
        The symbol for the small greek letter varepsilon (depends on DEFAULT_VAREPSILON).
    zeta : Symbol
        The symbol for the small greek letter zeta.
    eta : Symbol
        The symbol for the small greek letter eta.
    theta : Symbol
        The symbol for the small greek letter theta (depends on DEFAULT_VARTHETA).
    vartheta : Symbol
        The symbol for the small greek letter vartheta (depends on DEFAULT_VARTHETA).
    iota : Symbol
        The symbol for the small greek letter iota.
    kappa : Symbol
        The symbol for the small greek letter kappa.
    lambda_ : Symbol
        The symbol for the small greek letter lambda.
    mu : Symbol
        The symbol for the small greek letter mu.
    nu : Symbol
        The symbol for the small greek letter nu.
    xi : Symbol
        The symbol for the small greek letter xi.
    pi : Symbol
        The symbol for the small greek letter pi (depends on DEFAULT_VARPI).
    varpi : Symbol
        The symbol for the small greek letter varpi (depends on DEFAULT_VARPI).
    rho : Symbol
        The symbol for the small greek letter rho (depends on DEFAULT_VARRHO).
    varrho : Symbol
        The symbol for the small greek letter varrho (depends on DEFAULT_VARRHO).
    sigma : Symbol
        The symbol for the small greek letter sigma.
    tau : Symbol
        The symbol for the small greek letter tau.
    upsilon : Symbol
        The symbol for the small greek letter upsilon.
    phi : Symbol
        The symbol for the small greek letter phi (depends on DEFAULT_VARPHI).
    varphi : Symbol
        The symbol for the small greek letter varphi (depends on DEFAULT_VARPHI).
    chi : Symbol
        The symbol for the small greek letter chi.
    psi : Symbol
        The symbol for the small greek letter psi.
    omega : Symbol
        The symbol for the small greek letter omega.
    Gamma : Symbol
        The symbol for the capital greek letter Gamma.
    Delta : Symbol
        The symbol for the capital greek letter Delta.
    Theta : Symbol
        The symbol for the capital greek letter Theta.
    Lambda : Symbol
        The symbol for the capital greek letter Lambda.
    Xi : Symbol
        The symbol for the capital greek letter Xi.
    Pi : Symbol
        The symbol for the capital greek letter Pi.
    Sigma : Symbol
        The symbol for the capital greek letter Sigma.
    Upsilon : Symbol
        The symbol for the capital greek letter Upsilon.
    Phi : Symbol
        The symbol for the capital greek letter Phi.
    Psi : Symbol
        The symbol for the capital greek letter Psi.
    Omega : Symbol
        The symbol for the capital greek letter Omega.
    """

    ##################### SMALL LETTERS #####################
    alpha = Symbol("alpha", r"\alpha", "\u03B1")
    beta = Symbol("beta", r"\beta", "\u03B2")
    gamma = Symbol("gamma", r"\gamma", "\u03B3")
    delta = Symbol("delta", r"\delta", "\u03B4")
    epsilon = Symbol("epsilon", r"\epsilon", "\u03F5", r"\varepsilon", "\u03B5", DEFAULT_VAREPSILON)
    varepsilon = Symbol("varepsilon", r"\varepsilon", "\u03B5", r"\epsilon", "\u03F5", DEFAULT_VAREPSILON)
    zeta = Symbol("zeta", r"\zeta", "\u03B6")
    eta = Symbol("eta", r"\eta", "\u03B7")
    theta = Symbol("theta", r"\theta", "\u03B8", r"\vartheta", "\u03D1", DEFAULT_VARTHETA)
    vartheta = Symbol("vartheta", r"\vartheta", "\u03D1", r"\theta", "\u03B7", DEFAULT_VARTHETA)
    iota = Symbol("iota", r"\iota", "\u03B9")
    kappa = Symbol("kappa", r"\kappa", "\u03BA")
    lambda_ = Symbol("lambda", r"\lambda", "\u03BB")
    mu = Symbol("mu", r"\mu", "\u03BC")
    nu = Symbol("nu", r"\nu", "\u03BD")
    xi = Symbol("xi", r"\xi", "\u03BE")
    pi = Symbol("pi", r"\pi", "\u03C0", r"\varpi", "\u03D6", DEFAULT_VARPI)
    varpi = Symbol("varpi", r"\varpi", "\u03D6", r"\pi", "\u03C0", DEFAULT_VARPI)
    rho = Symbol("rho", r"\rho", "\u03C1", r"\varrho", "\u03F1", DEFAULT_VARRHO)
    varrho = Symbol("varrho", r"\varrho", "\u03F1", r"\rho", "\u03C1", DEFAULT_VARRHO)
    sigma = Symbol("sigma", r"\sigma", "\u03C3")
    tau = Symbol("tau", r"\tau", "\u03C4")
    upsilon = Symbol("upsilon", r"\upsilon", "\u03C5")
    phi = Symbol("phi", r"\phi", "\u03D0", r"\varphi", "\u03C6", DEFAULT_VARPHI)
    varphi = Symbol("varphi", r"\varphi", "\u03C6", r"\phi", "\u03D0", DEFAULT_VARPHI)
    chi = Symbol("chi", r"\chi", "\u03C7")
    psi = Symbol("psi", r"\psi", "\u03C8")
    omega = Symbol("omega", r"\omega", "\u03C9")
    ##################### CAPITAL LETTERS #####################
    Gamma = Symbol("Gamma", r"\Gamma", "\u0393")
    Delta = Symbol("Delta", r"\Delta", "\u0394")
    Theta = Symbol("Theta", r"\Theta", "\u0398")
    Lambda = Symbol("Lambda", r"\Lambda", "\u039B")
    Xi = Symbol("Xi", r"\Xi", "\u039E")
    Pi = Symbol("Pi", r"\Pi", "\u03A0")
    Sigma = Symbol("Sigma", r"\Sigma", "\u03A3")
    Upsilon = Symbol("Upsilon", r"\Upsilon", "\u03A5")
    Phi = Symbol("Phi", r"\Phi", "\u03A6")
    Psi = Symbol("Psi", r"\Psi", "\u03A8")
    Omega = Symbol("Omega", r"\Omega", "\u03A9")

    @classmethod
    def get_symbols(cls):
        return super(Greeks, cls).get_symbols()

    @classmethod
    def list_symbols(cls):
        super(Greeks, cls).list_symbols()
