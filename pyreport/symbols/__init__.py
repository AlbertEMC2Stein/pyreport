from abc import ABC, abstractmethod

__all__ = ["Symbol", "SymbolCollection"]


class Symbol:
    def __init__(self, plaintext, default_latex, default_unicode, alternate_latex=None, alternate_unicode=None, switch=lambda: False):
        self.__plaintext = plaintext
        self.__default_latex = default_latex
        self.__default_unicode = default_unicode
        self.__alternate_latex = alternate_latex
        self.__alternate_unicode = alternate_unicode
        self.__switch = switch

    # @property
    # def __doc__(self):
    #     addendum = (
    #         f" or alternatively \\({self.__alternate_latex}\\) \
    #         depending on {self.__switch.name}."
    #         if self.__alternate_latex
    #         else "."
    #     )

    #     return f"This class represents the symbol \\({self.__default_latex}\\) \
    #            ({self.__plaintext}){addendum}"

    def to_tex(self):
        return (
            self.__alternate_latex
            if (self.__alternate_latex and self.__switch())
            else self.__default_latex
        )

    def to_plain(self):
        return self.__plaintext
    
    def to_unicode(self):
        return (
            self.__alternate_unicode
            if (self.__alternate_unicode and self.__switch())
            else self.__default_unicode
        )
    
    def __str__(self):
        return f"Plaintext: {self.to_plain():<12} TeX: {self.to_tex():<13} Unicode: {self.to_unicode()}"


class SymbolCollection(ABC):
    @classmethod
    @abstractmethod
    def get_symbols(cls):
        all_attr = [(attr, getattr(cls, attr)) for attr in dir(cls)]
        return  {name: attr for (name, attr) in all_attr if isinstance(attr, Symbol)}

    @classmethod
    @abstractmethod
    def list_symbols(cls):
        symbols = cls.get_symbols()
        print(f"Symbols in {cls.__name__} [{len(symbols)}]:")
        for symbol in symbols.values():
            print(f"\t- {symbol.to_plain()}")