from PyReport.Symbols import SymbolInterface
from PyReport._utils import Switch, classproperty


DEFAULT_VAREPSILON = Switch('DEFAULT_VAREPSILON', False, True)
"""Switch out the default LaTeX command for epsilon with the alternate one (varepsilon)."""

DEFAULT_VARTHETA = Switch('DEFAULT_VARTHETA',True, False)
"""Switch out the default LaTeX command for theta with the alternate one (vartheta)."""

DEFAULT_VARPI = Switch('DEFAULT_VARPI',True, False)
"""Switch out the default LaTeX command for pi with the alternate one (varpi)."""

DEFAULT_VARRHO = Switch('DEFAULT_VARRHO',True, False)
"""Switch out the default LaTeX command for rho with the alternate one (varrho)."""

DEFAULT_VARPHI = Switch('DEFAULT_VARPHI',False, True)
"""Switch out the default LaTeX command for phi with the alternate one (varphi)."""


##################### SMALL LETTERS #####################


class alpha(SymbolInterface):
    _name = "alpha"
    _default_latex = r"\alpha"
    
    @classproperty
    def __doc__(cls):
        return super(alpha, cls).__doc__


class beta(SymbolInterface):
    _name = "beta"
    _default_latex = r"\beta"
    
    @classproperty
    def __doc__(cls):
        return super(beta, cls).__doc__
    

class gamma(SymbolInterface):
    _name = "gamma"
    _default_latex = r"\gamma"
    
    @classproperty
    def __doc__(cls):
        return super(gamma, cls).__doc__
    

class delta(SymbolInterface):
    _name = "delta"
    _default_latex = r"\delta"
    
    @classproperty
    def __doc__(cls):
        return super(delta, cls).__doc__
    

class epsilon(SymbolInterface):
    _name = "epsilon"
    _default_latex = r"\epsilon"
    _alternate_latex = r"\varepsilon"
    _switch = DEFAULT_VAREPSILON
    
    @classproperty
    def __doc__(cls):
        return super(epsilon, cls).__doc__
    

class varepsilon(SymbolInterface):
    _name = "varepsilon"
    _default_latex = r"\varepsilon"
    _alternate_latex = r"\epsilon"
    _switch = DEFAULT_VAREPSILON

    @classproperty
    def __doc__(cls):
        return super(varepsilon, cls).__doc__
    

class zeta(SymbolInterface):
    _name = "zeta"
    _default_latex = r"\zeta"
    
    @classproperty
    def __doc__(cls):
        return super(zeta, cls).__doc__
    

class eta(SymbolInterface):
    _name = "eta"
    _default_latex = r"\eta"
    
    @classproperty
    def __doc__(cls):
        return super(eta, cls).__doc__
    

class theta(SymbolInterface):
    _name = "theta"
    _default_latex = r"\theta"
    _alternate_latex = r"\vartheta"
    _switch = DEFAULT_VARTHETA
    
    @classproperty
    def __doc__(cls):
        return super(theta, cls).__doc__
    

class vartheta(SymbolInterface):
    _name = "vartheta"
    _default_latex = r"\vartheta"
    _alternate_latex = r"\theta"
    _switch = DEFAULT_VARTHETA
    
    @classproperty
    def __doc__(cls):
        return super(vartheta, cls).__doc__
    

class iota(SymbolInterface):
    _name = "iota"
    _default_latex = r"\iota"
    
    @classproperty
    def __doc__(cls):
        return super(iota, cls).__doc__
    

class kappa(SymbolInterface):
    _name = "kappa"
    _default_latex = r"\kappa"
    
    @classproperty
    def __doc__(cls):
        return super(kappa, cls).__doc__
    

class lambda_(SymbolInterface):
    _name = "lambda"
    _default_latex = r"\lambda"
    
    @classproperty
    def __doc__(cls):
        return super(lambda_, cls).__doc__
    

class mu(SymbolInterface):
    _name = "mu"
    _default_latex = r"\mu"
    
    @classproperty
    def __doc__(cls):
        return super(mu, cls).__doc__
    

class nu(SymbolInterface):
    _name = "nu"
    _default_latex = r"\nu"
    
    @classproperty
    def __doc__(cls):
        return super(nu, cls).__doc__
    

class xi(SymbolInterface):
    _name = "xi"
    _default_latex = r"\xi"
    
    @classproperty
    def __doc__(cls):
        return super(xi, cls).__doc__


class pi(SymbolInterface):
    _name = "pi"
    _default_latex = r"\pi"
    _alternate_latex = r"\varpi"
    _switch = DEFAULT_VARPI
    
    @classproperty
    def __doc__(cls):
        return super(pi, cls).__doc__
    

class varpi(SymbolInterface):
    _name = "varpi"
    _default_latex = r"\varpi"
    _alternate_latex = r"\pi"
    _switch = DEFAULT_VARPI
    
    @classproperty
    def __doc__(cls):
        return super(varpi, cls).__doc__


class rho(SymbolInterface):
    _name = "rho"
    _default_latex = r"\rho"
    _alternate_latex = r"\varrho"
    _switch = DEFAULT_VARRHO
    
    @classproperty
    def __doc__(cls):
        return super(rho, cls).__doc__
    

class varrho(SymbolInterface):
    _name = "varrho"
    _default_latex = r"\varrho"
    _alternate_latex = r"\rho"
    _switch = DEFAULT_VARRHO
    
    @classproperty
    def __doc__(cls):
        return super(varrho, cls).__doc__


class sigma(SymbolInterface):
    _name = "sigma"
    _default_latex = r"\sigma"
    
    @classproperty
    def __doc__(cls):
        return super(sigma, cls).__doc__
    

class tau(SymbolInterface):
    _name = "tau"
    _default_latex = r"\tau"
    
    @classproperty
    def __doc__(cls):
        return super(tau, cls).__doc__
    

class upsilon(SymbolInterface):
    _name = "upsilon"
    _default_latex = r"\upsilon"
    
    @classproperty
    def __doc__(cls):
        return super(upsilon, cls).__doc__
    

class phi(SymbolInterface):
    _name = "phi"
    _default_latex = r"\phi"
    _alternate_latex = r"\varphi"
    _switch = DEFAULT_VARPHI
    
    @classproperty
    def __doc__(cls):
        return super(phi, cls).__doc__
    

class varphi(SymbolInterface):
    _name = "varphi"
    _default_latex = r"\varphi"
    _alternate_latex = r"\phi"
    _switch = DEFAULT_VARPHI
    
    @classproperty
    def __doc__(cls):
        return super(varphi, cls).__doc__
    

class chi(SymbolInterface):
    _name = "chi"
    _default_latex = r"\chi"
    
    @classproperty
    def __doc__(cls):
        return super(chi, cls).__doc__
    

class psi(SymbolInterface):
    _name = "psi"
    _default_latex = r"\psi"
    
    @classproperty
    def __doc__(cls):
        return super(psi, cls).__doc__
    

class omega(SymbolInterface):
    _name = "omega"
    _default_latex = r"\omega"
    
    @classproperty
    def __doc__(cls):
        return super(omega, cls).__doc__
    

##################### CAPITAL LETTERS #####################
    

class Gamma(SymbolInterface):
    _name = "Gamma"
    _default_latex = r"\Gamma"
    
    @classproperty
    def __doc__(cls):
        return super(Gamma, cls).__doc__


class Delta(SymbolInterface):
    _name = "Delta"
    _default_latex = r"\Delta"
    
    @classproperty
    def __doc__(cls):
        return super(Delta, cls).__doc__
    

class Theta(SymbolInterface):
    _name = "Theta"
    _default_latex = r"\Theta"
    
    @classproperty
    def __doc__(cls):
        return super(Theta, cls).__doc__


class Lambda(SymbolInterface):
    _name = "Lambda"
    _default_latex = r"\Lambda"
    
    @classproperty
    def __doc__(cls):
        return super(Lambda, cls).__doc__


class Xi(SymbolInterface):
    _name = "Xi"
    _default_latex = r"\Xi"
    
    @classproperty
    def __doc__(cls):
        return super(Xi, cls).__doc__


class Pi(SymbolInterface):
    _name = "Pi"
    _default_latex = r"\Pi"
    
    @classproperty
    def __doc__(cls):
        return super(Pi, cls).__doc__
    

class Sigma(SymbolInterface):
    _name = "Sigma"
    _default_latex = r"\Sigma"
    
    @classproperty
    def __doc__(cls):
        return super(Sigma, cls).__doc__
    

class Upsilon(SymbolInterface):
    _name = "Upsilon"
    _default_latex = r"\Upsilon"
    
    @classproperty
    def __doc__(cls):
        return super(Upsilon, cls).__doc__
    

class Phi(SymbolInterface):
    _name = "Phi"
    _default_latex = r"\Phi"
    
    @classproperty
    def __doc__(cls):
        return super(Phi, cls).__doc__
    

class Psi(SymbolInterface):
    _name = "Psi"
    _default_latex = r"\Psi"
    
    @classproperty
    def __doc__(cls):
        return super(Psi, cls).__doc__
    

class Omega(SymbolInterface):
    _name = "Omega"
    _default_latex = r"\Omega"
    
    @classproperty
    def __doc__(cls):
        return super(Omega, cls).__doc__