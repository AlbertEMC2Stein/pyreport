from pyreport.symbols import symbol
from pyreport._utils import switch


__all__ = [
    'DEFAULT_VAREPSILON', 'DEFAULT_VARTHETA', 'DEFAULT_VARPI', 'DEFAULT_VARRHO', 'DEFAULT_VARPHI', 'alpha', 'beta', 'gamma', 'delta', 'epsilon', 'varepsilon', 'zeta', 'eta', 'theta', 'vartheta', 'iota', 'kappa', 'lambda_', 'mu', 'nu', 'xi', 'pi', 'varpi', 'rho', 'varrho', 'sigma', 'tau', 'upsilon', 'phi', 'varphi', 'chi', 'psi', 'omega', 'Gamma', 'Delta', 'Theta', 'Lambda', 'Xi', 'Pi', 'Sigma', 'Upsilon', 'Phi', 'Psi', 'Omega'
]


DEFAULT_VAREPSILON = switch('DEFAULT_VAREPSILON', False, True)
"""Switch out the default LaTeX command for epsilon with the alternate one (varepsilon)."""

DEFAULT_VARTHETA   = switch('DEFAULT_VARTHETA',True, False)
"""Switch out the default LaTeX command for theta with the alternate one (vartheta)."""

DEFAULT_VARPI      = switch('DEFAULT_VARPI',True, False)
"""Switch out the default LaTeX command for pi with the alternate one (varpi)."""

DEFAULT_VARRHO     = switch('DEFAULT_VARRHO',True, False)
"""Switch out the default LaTeX command for rho with the alternate one (varrho)."""

DEFAULT_VARPHI     = switch('DEFAULT_VARPHI',False, True)
"""Switch out the default LaTeX command for phi with the alternate one (varphi)."""

##################### SMALL LETTERS #####################

alpha      = symbol('alpha', r"\alpha")
beta       = symbol('beta', r"\beta")
gamma      = symbol('gamma', r"\gamma")
delta      = symbol('delta', r"\delta")
epsilon    = symbol('epsilon', r"\epsilon", r"\varepsilon", DEFAULT_VAREPSILON)
varepsilon = symbol('varepsilon', r"\varepsilon", r"\epsilon", DEFAULT_VAREPSILON)
zeta       = symbol('zeta', r"\zeta")
eta        = symbol('eta', r"\eta")
theta      = symbol('theta', r"\theta", r"\vartheta", DEFAULT_VARTHETA)
vartheta   = symbol('vartheta', r"\vartheta", r"\theta", DEFAULT_VARTHETA)
iota       = symbol('iota', r"\iota")
kappa      = symbol('kappa', r"\kappa")
lambda_    = symbol('lambda', r"\lambda")
mu         = symbol('mu', r"\mu")
nu         = symbol('nu', r"\nu")
xi         = symbol('xi', r"\xi")
pi         = symbol('pi', r"\pi", r"\varpi", DEFAULT_VARPI)
varpi      = symbol('varpi', r"\varpi", r"\pi", DEFAULT_VARPI)
rho        = symbol('rho', r"\rho", r"\varrho", DEFAULT_VARRHO)
varrho     = symbol('varrho', r"\varrho", r"\rho", DEFAULT_VARRHO)
sigma      = symbol('sigma', r"\sigma")
tau        = symbol('tau', r"\tau")
upsilon    = symbol('upsilon', r"\upsilon")
phi        = symbol('phi', r"\phi", r"\varphi", DEFAULT_VARPHI)
varphi     = symbol('varphi', r"\varphi", r"\phi", DEFAULT_VARPHI)
chi        = symbol('chi', r"\chi")
psi        = symbol('psi', r"\psi")
omega      = symbol('omega', r"\omega")

##################### CAPITAL LETTERS #####################

Gamma   = symbol('Gamma', r"\Gamma")
Delta   = symbol('Delta', r"\Delta")
Theta   = symbol('Theta', r"\Theta")
Lambda  = symbol('Lambda', r"\Lambda")
Xi      = symbol('Xi', r"\Xi")
Pi      = symbol('Pi', r"\Pi")
Sigma   = symbol('Sigma', r"\Sigma")
Upsilon = symbol('Upsilon', r"\Upsilon")
Phi     = symbol('Phi', r"\Phi")
Psi     = symbol('Psi', r"\Psi")
Omega   = symbol('Omega', r"\Omega")