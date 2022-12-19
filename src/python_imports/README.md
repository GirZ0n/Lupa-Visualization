# Python Imports
This app will allow you to visualize the statistics of import directives in Python that were gathered using [Lupa](https://github.com/nbirillo/Lupa) framework.

## Glossary
- Import directive: `from plotly.express import scatter`;
- Fully qualified name of import directive (FQ name): `plotly.express.scatter`.

## Data

With [SEART GitHub Search](https://seart-ghs.si.usi.ch/), we've collected the top 10k Python repositories, sorted by stars. 
After filtering out duplicates, 9,645 repositories remain.

Using Lupa, 853,611 unique FQ names were collected. Next, the private imports and the imports related to the standard library were filtered out. 
Then, they were grouped by package name and within each group the number of imports was summed. 
Thus, we obtained usage statistics for 496,744 FQ names, grouped into 62,972 packages.

This statistic has also been divided by Python language version:
- `PYTHON_2` — only Python 2 is used in the project;
- `PYTHON_3` — only Python 3 is used in the project;
- `PYTHON_MIXED` — both Python 2 and Python 3 can be used in the project;
- `PYTHON_UNKNOWN` — the version of Python used in the project could not be determined.

The collected data can be found [here](../../resources/python_imports/data).

## Pages
There are three pages in the visualization:

1. Statistics for all imports: the statistics for all FQ names, except for private FQ names, are visualized here.
2. Statistics without stdlib imports: the statistics for all FQ names, except for private ones and those included in the standard library, are visualized here.
