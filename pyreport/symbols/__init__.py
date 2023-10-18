"""Provides the Symbol and SymbolCollection classes."""

from abc import ABC, abstractmethod

__all__ = ["Symbol", "SymbolCollection"]


class Symbol:
    """A class that represents a symbol in plaintext, TeX and Unicode."""

    def __init__(self, plaintext, default_latex, default_unicode, alternate_latex=None, alternate_unicode=None, switch=lambda: False):
        """Constructor for the Symbol class.

        Parameters
        ----------
        plaintext : str
            The plaintext representation of the symbol.
        default_latex : str
            The default TeX representation of the symbol.
        default_unicode : str
            The default Unicode representation of the symbol.
        alternate_latex : str, optional
            The alternate TeX representation of the symbol, by default None.
        alternate_unicode : str, optional
            The alternate Unicode representation of the symbol, by default None.
        switch : function, optional
            A function that returns a boolean value that determines whether to use the alternate representation, by default lambda: False.
        """

        self._plaintext = plaintext
        self._default_latex = default_latex
        self._default_unicode = default_unicode
        self._alternate_latex = alternate_latex
        self._alternate_unicode = alternate_unicode
        self._switch = switch

    def to_plain(self):
        """Get the plaintext representation of the symbol."""

        return self._plaintext

    def to_tex(self):
        """Get the TeX representation of the symbol."""

        return (
            self._alternate_latex
            if (self._alternate_latex and self._switch())
            else self._default_latex
        )

    def to_unicode(self):
        """Get the Unicode representation of the symbol."""

        return (
            self._alternate_unicode
            if (self._alternate_unicode and self._switch())
            else self._default_unicode
        )

    def __str__(self):
        return f"Plaintext: {self.to_plain():<12} TeX: {self.to_tex():<13} Unicode: {self.to_unicode()}"


class SymbolCollection(ABC):
    """A class that represents a collection of symbols."""

    @classmethod
    @abstractmethod
    def get_symbols(cls):
        """Get all symbols in the class."""

        all_attr = [(attr, getattr(cls, attr)) for attr in dir(cls)]
        return  {name: attr for (name, attr) in all_attr if isinstance(attr, Symbol)}

    @classmethod
    @abstractmethod
    def list_symbols(cls):
        """List all symbols in the class."""

        symbols = cls.get_symbols()
        print(f"Symbols in {cls.__name__} [{len(symbols)}]:")
        for symbol in symbols.values():
            print(f"\t- {symbol.to_plain()}")
