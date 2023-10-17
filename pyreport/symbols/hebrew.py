"""A module providing the Hebrew alphabet as symbols."""

from pyreport.symbols import SymbolCollection, Symbol

__all__ = ['Hebrews']


class Hebrews(SymbolCollection):
    """A collection containing the Hebrew alphabet as symbols.

    Attributes
    ----------
    aleph : Symbol
        The symbol for the Hebrew letter aleph.
    beth : Symbol
        The symbol for the Hebrew letter beth.
    daleth : Symbol
        The symbol for the Hebrew letter daleth.
    gimel : Symbol
        The symbol for the Hebrew letter gimel.
    """

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
