from PyReport.Symbols import SymbolInterface
from PyReport._utils import classproperty


class aleph(SymbolInterface):
    _name = "aleph"
    _default_latex = r"\aleph"
    
    @classproperty
    def __doc__(cls):
        return super(aleph, cls).__doc__


class beth(SymbolInterface):
    _name = "beth"
    _default_latex = r"\beth"
    
    @classproperty
    def __doc__(cls):
        return super(beth, cls).__doc__


class daleth(SymbolInterface):
    _name = "daleth"
    _default_latex = r"\daleth"
    
    @classproperty
    def __doc__(cls):
        return super(daleth, cls).__doc__


class gimel(SymbolInterface):
    _name = "gimel"
    _default_latex = r"\gimel"
    
    @classproperty
    def __doc__(cls):
        return super(gimel, cls).__doc__