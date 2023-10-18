# pyreport - A Python package for creating LaTeX reports from within your code!

## Roadmap
- [ ] Add all remaining symbols/math-operators 
- [ ] Add more environments for formatting text and data, e.g. center, figure, table, etc.
    - [ ] Add support for matplotlib figures and plots, e.g. with an Environment that can take a figure object, save it to a temporary file and then include it in the report
    - [ ] Add support for custom data-viz via TikZ, e.g. Environment that can take various types of data and then creates an appropriate visualization given some settings
    - [ ] Add support for .csv files to automatically create tables
- [ ] Add environment that automatically displays source code via inspect.getsource() and listings
- [ ] Add support for mathematics
    - [ ] Add math environments like align, equation, etc.
    - [ ] Add support for variables that can either be displayed as symbol or the value they hold
    - [ ] Add support for variable tracking such that variable objects can be used in computations and the result is automatically displayed
    - [ ] Add syntax for builing formulas via python operations, e.g. `Variable(alpha, 0.5) + Variable(beta, 0.5)` either renders to $\alpha + \beta$ or returns the value 1.0.
    - [ ] Add variable logging to see how the variable changes over time (maybe even own Logging environment?)
    - [ ] Add support for function evaluations and Variable assignments via `Function(f, lambda x: x**2)` and `Variable(x, 2)` such that `f(x)` renders to $f(x) = x^2$ and `f(x).value` returns 4.
    - [ ] Add support for vectors, matrices and non-scalar functions.
- [ ] Add support for custom environments
- [ ] Add support for custom commands
- [ ] Add support for label-referencing
- [ ] Add support for bibliography and sources, maybe even with automatic citation generation via classes like Article, Book, Report, etc.
- [ ] Add support for custom style files to customize the look of the report