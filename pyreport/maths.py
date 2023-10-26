import time
from numpy.random import choice
import numpy as np


def timestamp():
    return time.strftime("%H:%M:%S", time.localtime())


def generate_tmp(value):
    if isinstance(value, Variable):
        return value

    hexcode = list("0123456789ABCDEF")
    tmp_name = "tmp_" + "".join([choice(hexcode) for _ in range(6)])

    return Variable(tmp_name, value)


def binarytrack(lhs, rhs, result_var_name, template):
    if not (isinstance(rhs, Variable) and isinstance(lhs, Variable)):
        return

    log_msg = f"{result_var_name} = {template.format(lhs.name, rhs.name)}, {rhs.name} = {rhs.value}, {lhs.name} = {lhs.value}"

    if lhs.is_watching(rhs):
        lhs.log(log_msg)

    if rhs.is_watching(lhs):
        rhs.log(log_msg)


def ternarytrack(var1, var2, var3, result_var_name, template):
    inst1 = isinstance(var1, Variable)
    inst2 = isinstance(var2, Variable)
    inst3 = isinstance(var3, Variable)
    if (inst1 + inst2 + inst3) < 2:
        return

    varss = [var for var in [var1, var2, var3] if isinstance(var, Variable)]
    names = [
        var.name if isinstance(var, Variable) else var for var in [var1, var2, var3]
    ]

    log_msg = f"{result_var_name} = {template.format(*names)}, " + ", ".join(
        [f"{var.name} = {var.value}" for var in varss]
    )

    if inst1 and (var1.is_watching(var2) or var1.is_watching(var3)):
        var1.log(log_msg)

    if inst2 and (var2.is_watching(var1) or var2.is_watching(var3)):
        var2.log(log_msg)

    if inst3 and (var3.is_watching(var1) or var3.is_watching(var2)):
        var3.log(log_msg)


class Variable:
    def __init__(self, name, value):
        if type(value) not in [int, float, complex]:
            raise TypeError("Variable value must be int, float or complex")

        self._name = name
        self._value = value
        self._watch = None
        self._logs = Log() # collective log?
        self._logs(f"Start of log for variable {name} with initial value {value}")

    def assign(self, __value):
        value, from_ = (
            __value.identity if isinstance(__value, Variable) else (__value, None)
        )

        if type(value) not in [int, float, complex]:
            raise TypeError("Variable value must be int, float or complex")

        self._value = value

        if self._watch is not None:
            self._logs(
                f"{self._name} = {value}"
                + (f" from {from_}" if from_ is not None else "")
            )

    @property
    def name(self):
        return self._name

    @property
    def value(self):
        return self._value

    @name.setter
    def name(self, __name):
        raise AttributeError("Cannot set name of Variable")

    @value.setter
    def value(self, __value):
        raise AttributeError("Cannot set value of Variable")

    def log(self, message):
        self._logs(message)

    def watch(self, *__variables):
        if self._watch is None:
            self._watch = []

        for __variable in __variables:
            if __variable.name not in self._watch:
                self._watch.append(__variable.name)
            else:
                raise ValueError(f"Variable {__variable.name} is already being watched")

    def unwatch(self, *__variables):
        if self._watch is None:
            return

        for __variable in __variables:
            if __variable.name in self._watch:
                self._watch.remove(__variable.name)
            else:
                raise ValueError(f"Variable {__variable.name} is not being watched")

    def is_watching(self, __variable):
        if self._watch is None or not isinstance(__variable, Variable):
            return False

        return __variable.name in self._watch

    @property
    def identity(self):
        return self._value, self._name

    @property
    def real(self):
        return self._value.real

    @property
    def imag(self):
        return self._value.imag

    def conjugate(self):
        return self._value.conjugate()

    def __add__(self, __value):
        result = generate_tmp(self._value + __value)
        binarytrack(self, __value, result.name, "${0} + {1}$")
        return result

    def __sub__(self, __value):
        result = generate_tmp(self._value - __value)
        binarytrack(self, __value, result.name, "${0} - {1}$")
        return result

    def __mul__(self, __value):
        result = generate_tmp(self._value * __value)
        binarytrack(self, __value, result.name, "${0} \\cdot {1}$")
        return result

    def __floordiv__(self, __value):
        result = generate_tmp(self._value // __value)
        binarytrack(
            self,
            __value,
            result.name,
            "$\\left\\lfloor\\frac{{{0}}}{{{1}}}\\right\\rfloor$",
        )
        return result

    def __truediv__(self, __value):
        result = generate_tmp(self._value / __value)
        binarytrack(self, __value, result.name, "$\\frac{{{0}}}{{{1}}}$")
        return result

    def __mod__(self, __value):
        result = generate_tmp(self._value % __value)
        binarytrack(self, __value, result.name, "${0} \\pmod{{{1}}}$")
        return result

    def __pow__(self, __value, __mod=None):
        value = __value.value if isinstance(__value, Variable) else __value
        mod = __mod.value if isinstance(__mod, Variable) else __mod
        result = generate_tmp(pow(self._value, value, mod))

        if mod is not None:
            ternarytrack(self, __value, __mod, result.name, "${0}^{1} \\pmod{{{2}}}$")
        else:
            ternarytrack(self, __value, __mod, result.name, "${0}^{1}$")

        return result

    def __radd__(self, __value):
        result = generate_tmp(__value + self._value)
        binarytrack(__value, self, result.name, "${0} + {1}$")
        return result

    def __rsub__(self, __value):
        result = generate_tmp(__value - self._value)
        binarytrack(__value, self, result.name, "${0} - {1}$")
        return result

    def __rmul__(self, __value):
        result = generate_tmp(__value * self._value)
        binarytrack(__value, self, result.name, "${0} \\cdot {1}$")
        return result

    def __rfloordiv__(self, __value):
        result = generate_tmp(__value // self._value)
        binarytrack(
            __value,
            self,
            result.name,
            "$\\left\\lfloor\\frac{{{0}}}{{{1}}}\\right\\rfloor$",
        )
        return result

    def __rtruediv__(self, __value):
        result = generate_tmp(__value / self._value)
        binarytrack(__value, self, result.name, "$\\frac{{{0}}}{{{1}}}$")
        return result

    def __rmod__(self, __value):
        result = generate_tmp(__value % self._value)
        binarytrack(__value, self, result.name, "${0} \\pmod{{{1}}}$")
        return result

    def __rpow__(self, __value, __mod: None = None):
        result = generate_tmp(pow(__value, self._value, __mod))
        ternarytrack(__value, self, __mod, result.name, "${0}^{1} \\pmod{{{2}}}$")
        return result

    def __trunc__(self):
        return generate_tmp(self._value.__trunc__())

    def __ceil__(self):
        return generate_tmp(self._value.__ceil__())

    def __floor__(self):
        return generate_tmp(self._value.__floor__())

    def __round__(self, __ndigits=None):
        return generate_tmp(self._value.__round__(__ndigits))

    def __eq__(self, __value):
        binarytrack(self, __value, "_", "${0} \\overset{{?}}{{=}} {1}$")
        return self._value == __value

    def __ne__(self, __value):
        binarytrack(self, __value, "_", "${0} \\overset{{?}}{{\\neq}} {1}$")
        return self._value != __value

    def __lt__(self, __value):
        binarytrack(self, __value, "_", "${0} \\overset{{?}}{{<}} {1}$")
        return self._value < __value

    def __le__(self, __value):
        binarytrack(self, __value, "_", "${0} \\overset{{?}}{{\\leq}} {1}$")
        return self._value <= __value

    def __gt__(self, __value):
        binarytrack(self, __value, "_", "${0} \\overset{{?}}{{>}} {1}$")
        return self._value > __value

    def __ge__(self, __value):
        binarytrack(self, __value, "_", "${0} \\overset{{?}}{{\\geq}} {1}$")
        return self._value >= __value

    def __neg__(self):
        return generate_tmp(-self._value)

    def __pos__(self):
        return generate_tmp(+self._value)

    def __int__(self):
        return int(self._value)

    def __float__(self):
        return float(self._value)

    def __abs__(self):
        return generate_tmp(abs(self._value))

    def __hash__(self):
        return hash(self._value)

    def __bool__(self):
        return bool(self._value)

    def __str__(self):
        return f"{self._name} = {self._value}"


class Log:
    def __init__(self):
        self._collected = ""
        self._counter = 1

    def __call__(self, log):
        self._collected += f"[{timestamp()}]\t{self._counter}: {log}\n"
        self._counter += 1

    def __str__(self):
        return self._collected


if __name__ == "__main__":
    x = Variable("x", 0)
    y = Variable("y", 1)

    x.watch(y)
    y.watch(x)

    for i in range(10):
        tmp = x + y
        x.assign(y)
        y.assign(tmp)

    print(x._logs)
    print(y._logs)
