from pyreport.symbols import SymbolCollection, Symbol

__all__ = ['Hebrews']


class Hebrews(SymbolCollection):
    aleph  = Symbol('aleph', r"\aleph", "\u2135")
    beth   = Symbol('beth', r"\beth", "\u2136")
    daleth = Symbol('daleth', r"\daleth", "\u2138")
    gimel  = Symbol('gimel', r"\gimel", "\u2137")

    @classmethod
    def get_symbols(cls):
        return super(Hebrews, cls).get_symbols()
    
    @classmethod
    def list_symbols(cls):
        super(Hebrews, cls).list_symbols()
