# Lupa-Visualization
This repository contains the source code of the statistics visualizations gathered with the [Lupa](https://github.com/JetBrains-Research/Lupa) framework. 

The collected data is located in the [`resources`](./resources) folder. You can use them for your own analysis and visualization.

## Available visualizations
The visualization of the following statistics is currently available:
- [Kotlin Imports](https://jbr-lupa-visualization-kotlin-imports.streamlitapp.com)
- [Kotlin Gradle Dependencies](https://jbr-lupa-visualization-kotlin-gradle-dependencies.streamlitapp.com)
- [Python Imports](https://jbr-lupa-visualization-python-imports.streamlitapp.com)
- [Python Call Expressions](https://jbr-lupa-visualization-python-call-expressions.streamlitapp.com)

You can also run the visualization locally:
```
streamlit run src/<visualization_name>/About.py
```
where `<visualization_name>` corresponds to the name of the visualization you want to run. For example, for Python Imports `<visualization_name>` will be equal to `python_imports`.
