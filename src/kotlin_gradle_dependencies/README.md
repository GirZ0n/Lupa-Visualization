# Kotlin Gradle Dependencies
This app will allow you to visualize the statistics of gradle dependencies in Kotlin that were gathered using [Lupa](https://github.com/nbirillo/Lupa) framework.

## Glossary
Gradle dependency — `implementation "org.jetbrains.kotlin:kotlin-reflect:1.5.10"` where:
- configuration: `implementation`;
- groupId: `org.jetbrains.kotlin`;
- artifactId: `kotlin-reflect`;
- version: `1.5.10`.

## Data
The collected data can be found [here](https://github.com/GirZ0n/Lupa-Visualization/tree/main/resources/kotlin_gradle_dependencies/data).

## Pages
There are three pages in the visualization:

1. Per module statistics for all projects: the statistics per module for all FQ names are visualized here.
2. Per module statistics without Android projects: the statistics per module for all FQ names, except those collected from Android projects, are visualized here.
3. Per project statistics: the statistics per project for all FQ names are visualized here.
