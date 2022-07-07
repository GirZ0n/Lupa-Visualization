# Lupa-Visualization
This repository contains the source code of the statistics visualizations gathered with the [Lupa](https://github.com/JetBrains-Research/Lupa) framework. 

The collected data is located in the [`resources`](./resources) folder. You can use them for your own analysis and visualization.

## Available visualizations
The visualization of the following statistics is currently available:
- [Kotlin Imports](https://share.streamlit.io/girz0n/kotlin-analysis-visualization/main/src/kotlin_imports/app.py)
- [Kotlin Gradle Dependencies](https://share.streamlit.io/girz0n/kotlin-analysis-visualization/main/src/kotlin_gradle_dependencies/app.py)
- [Python Imports](https://share.streamlit.io/girz0n/kotlin-analysis-visualization/main/src/python_imports/app.py)
- [Python Call Expressions](https://share.streamlit.io/girz0n/kotlin-analysis-visualization/main/src/python_call_expressions/app.py)

You can also run the visualization locally:
```
streamlit run src/<visualization_name>/About.py
```
where `<visualization_name>` corresponds to the name of the visualization you want to run. For example, for Python Imports `<visualization_name>` will be equal to `python_imports`.
