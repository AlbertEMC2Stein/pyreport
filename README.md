# pyreport: Automate Your LaTeX Reports with Python 📝
<p align="center">
  <img src="https://raw.githubusercontent.com/AlbertEMC2Stein/pyreport/main/docs/images/pyreport.png" width=250 style="border-radius:20px"/>
</p>


Create elegant LaTeX reports effortlessly from your code with pyreport. Generate and populate reports with plots, tables, custom environments, commands, and structure, all within your Python environment. Say goodbye to LaTeX headaches and focus on your work while pyreport handles the document creation for you.

- Automate LaTeX Reporting: Generate LaTeX reports seamlessly during your computations.
- Dynamic Content: Add plots, tables, variable logs, and custom LaTeX elements effortlessly.
- Structure Your Report: Define sections, chapters, and more for a well-organized document.
- Focus on Your Work: Stop worrying about LaTeX intricacies and focus on your data and analysis.

Simplify your report creation process with pyreport. No LaTeX expertise required.

**Main Contributors:**
- [Tim Prokosch](mailto:prokosch@rhrk.uni-kl.de)
- [Saif Khan](mailto:saif.khan@edu.rptu.de)

## Table of Contents
- [Introduction](#pyreport-automate-your-latex-reports-with-python-)
- [Roadmap](#roadmap)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## Roadmap
Our development roadmap is structured to follow a bottom-up approach, starting with fundamental features and gradually adding more advanced capabilities.

### Basic Functionality
- [x] Create LaTeX documents with text content.
- [x] Define sections and chapters for structuring your report.
- [ ] Add custom environments and commands.
- [ ] Add remaining symbols/math-operators 
- [x] Populate your report with plaintext.
- [x] Automate report generation with the `Reporter` class.

### Data Representation
- [ ] Add more environments for formatting text and data, e.g. center, figure, table, etc.
    - [ ] Add support for matplotlib figures and plots, e.g. with an Environment that can take a figure object, save it to a temporary file and then include it in the report.
    - [ ] Add support for custom data-viz via TikZ, e.g. Environment that can take various types of data and then creates an appropriate visualization given some settings.
    - [ ] Add support for .csv files to automatically create tables.
- [ ] Add environment that automatically displays source code via `inspect.getsource()` and listings.

### Mathematical Expressions
- [ ] Add support for mathematics with math environments like `align`, `equation`, etc.
- [ ] Add support for variables that can either be displayed as symbol or the value they hold.
- [ ] Support for variable tracking to see how variables change over time.
    - [ ] Add `x.watch` to automatically log the variable `x` whenever it changes. 
    - [ ] Make it possible to specify a list of variables to only log interactions with them, e.g. `x.watch([y, z])` only logs interactions of `x` with `y` and `z`.
- [ ] Builing formulas via python operations, e.g. `Variable(alpha, 0.5) + Variable(beta, 0.5)` either renders to $\alpha + \beta$ or returns the value 1.0.
- [ ] Add support for function evaluations and Variable assignments via `Function(f, lambda x: x**2)` and `Variable(x, 2)` such that `f(x)` renders to $f(x) = x^2$ and `f(x).value` returns 4.
- [ ] Add variable logging to see how the variable changes over time (maybe even own Logging environment?).
 
### Advanced Mathematical Concepts
- [ ] Support for vectors, matrices, and non-scalar functions.
- [ ] Handle custom function evaluations and variable assignments.
- [ ] Implement a variable glossary for variable documentation.

### Integration and References
- [ ] Add label-referencing support.
- [ ] Implement bibliography and sources, including automatic citation generation via classes like Article, Book, Report, etc.
- [ ] Automatically generate a glossary from provided variables with descriptions.

### High-level Convenience
- [ ] Provide a context manager with `with Reporter(...) as report` for streamlined report creation.
- [ ] Create custom style files to customize the report's appearance.

## Getting Started
1. Clone the repository:

    ```bash
    git clone https://github.com/AlbertEMC2Stein/pyreport.git
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Install pyreport:

    ```bash
    pip install .
    ```

4. Use the provided examples and documentation to start automating your reports with pyreport.

## Usage
To start generating reports, follow these basic steps:

1. Import the necessary modules:

    ```python
    from pyreport.math import *
    from pyreport.report import *
    ```

2. Create a `Reporter` instance:

    ```python
    report = Reporter('Your_Report_Name')
    ```

3. Add content to your report using the available functions and classes.

4. Save or export your report to the desired format, such as LaTeX or PDF.

## Examples
Here's an example of how to create a simple report with pyreport:

```python
from pyreport.math import *
from pyreport.report import *

report = Reporter('My_Report')

# Define a mathematical function
f = Function(f, lambda x: x**2)

# Create a variable and log its changes
x = Variable(x, 0, watch=True)
for i in range(100):
    x = x + i

print(x)  # -> 5050 or x = 5050
print(f(x, eval=True))  # -> 25502500

# Add equations and variable trace to the report
report.add(Equation(f, x, symbols=True))  # f(x) = x^2
report.add(Equation(f, x, symbols=False))  # -> f(x) = 25502500 
report.add(x.create_trace())  # -> 1:   x = 0     2:   x = 1     3: x = 3 ...
```

## Contributing
We welcome contributions! If you'd like to contribute to the development of pyreport, please see our [contribution guidelines](CONTRIBUTING.md) for more information.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

Feel free to customize and expand the sections as needed. Your README provides a comprehensive overview of your project's capabilities and how to get started with it.