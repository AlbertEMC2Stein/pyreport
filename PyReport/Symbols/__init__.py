from typing import Any
from PyReport._utils import classproperty


class SymbolInterface:      
    _name = r"[Symbol_Name]"
    _default_latex = r"[Symbol\_Command]"
    _alternate_latex = None
    _switch = lambda: False

    @classproperty
    def __doc__(cls):
        addendum = f" or alternatively \\({cls._alternate_latex}\\) depending on {cls._switch.name}." \
            if cls._alternate_latex \
            else "."
        
        return f"This class represents the symbol \\({cls._default_latex}\\) ({cls._name}){addendum}"
    
    @classmethod
    def toTeX(cls):
        return cls._alternate_latex if (cls._alternate_latex and cls._switch()) else cls._default_latex
    

__all__ = ['SymbolInterface']