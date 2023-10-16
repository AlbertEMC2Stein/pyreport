from abc import ABC, abstractmethod

__all__ = ["Symbol"]


class Symbol:
    def __init__(self, name, default_latex, alternate_latex=None, switch=lambda: False):
        self._name = name
        self._default_latex = default_latex
        self._alternate_latex = alternate_latex
        self._switch = switch

    @property
    def __doc__(self):
        addendum = (
            f" or alternatively \\({self._alternate_latex}\\) \
            depending on {self._switch.name}."
            if self._alternate_latex
            else "."
        )

        return f"This class represents the symbol \\({self._default_latex}\\) \
               ({self._name}){addendum}"

    def to_tex(self):
        return (
            self._alternate_latex
            if (self._alternate_latex and self._switch())
            else self._default_latex
        )

    def to_plain(self):
        return self._name


class SymbolCollection(ABC):
    _members = {}

    @classmethod
    @abstractmethod
    def get_members(cls):
        return cls._members

    @classmethod
    @abstractmethod
    def list_members(cls):
        print(f"Symbols in {cls.__name__} [{len(cls._members)}]:")
        for symbol in cls._members.values():
            print(f"\t- {symbol.to_plain()}")
