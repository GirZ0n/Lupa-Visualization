# Python Call Expressions
This app will allow you to visualize the statistics of call expressions in Python that were gathered using [Lupa](https://github.com/JetBrains-Research/Lupa) framework.

## Glossary
- Call expression: `np.zeros()`;
- Fully qualified name of call expression (FQ name): `numpy.core._multiarray_umath.zeros`.

## Data
With [SEART GitHub Search](https://seart-ghs.si.usi.ch/), we've collected the top 10k Python repositories, sorted by stars. After filtering out duplicates, 9,645 repositories remain.

Using Lupa, 2,399,915 unique FQ names were collected. The names of built-in functions, classes, and decorators were then filtered out, along with the names related to the standard library. Then they were grouped by name, and in each group the number of projects in which that name was encountered was summed. Thus, we obtained usage statistics for 787,800 FQ names in 9,344 projects.

This statistic has also been divided by Python language version:

- `PYTHON_2` — only Python 2 is used in the project;
- `PYTHON_3` — only Python 3 is used in the project;
- `PYTHON_MIXED` — both Python 2 and Python 3 can be used in the project;
- `PYTHON_UNKNOWN` — the version of Python used in the project could not be determined.

The collected data can be found [here](https://github.com/GirZ0n/Lupa-Visualization/tree/main/resources/python_call_expressions/data).

## Pages
There are two pages in the visualization:

1. Statistics for all expressions: the statistics for all FQ names are visualized here.
2. Statistics without stdlib and builtins: the statistics for all FQ names, except for bultin and stdlib FQ names, are visualized here.

