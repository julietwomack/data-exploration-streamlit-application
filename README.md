# Data Exploration Application
## Introduction

The **Data Exploration Application** was built using Python and the app framework, Streamlit. The application allows users to upload their own CSV file (up to 200 mb) and do initial exploratory data analysis on the numerical and character features. It also allows users to look at missing data to help prepare them for data cleaning prior to modeling or other data science tasks.

- [Click here to access the application](https://share.streamlit.io/julietwomack/data-exploration-streamlit-application/main/data-exploration-application.py)
- [Click here to access the code](https://github.com/julietwomack/data-exploration-streamlit-application/blob/main/data-exploration-application.py)

## Technologies
- [Atom](https://atom.io/)
- [Python](https://www.python.org/)

### Libraries
- [Time](https://docs.python.org/3/library/time.html)
- [Pandas](https://pandas.pydata.org/)
- [Streamlit](https://streamlit.io/)
- [Matplotlib](https://matplotlib.org/stable/index.html)
- [Seaborn](https://seaborn.pydata.org/)

## Functionality
- The following screenshots use the [training dataset of the Titanic dataset.](https://www.kaggle.com/c/titanic)

### Upload data
- Users can upload a CSV file (up to 200 mb) to the application.

<kbd> <img src="https://github.com/julietwomack/data-exploration-streamlit-application/blob/main/Screenshots/upload-image.png" /> </kbd>

### Initial data preview
- Users will be presented the first 7 rows of data
- Users will be presented a breakdown of the features by data type (i.e., number of continuous and discrete numerical variables and number of character variables)
- Users will be able to see a list of the feature names by data type

<kbd> <img src="https://github.com/julietwomack/data-exploration-streamlit-application/blob/main/Screenshots/preview-of-data.png" /> </kbd>

### Data exploration options
- Users will choose whether they want to explore the numerical, character, or missing data.

<kbd> <img src="https://github.com/julietwomack/data-exploration-streamlit-application/blob/main/Screenshots/exploration-options.png" /> </kbd>

### Numerical data
- Users can explore either descriptive statistics or visualizations with the numerical features.
- For either option, users can choose to stratify their analysis by a character variable or a discrete numerical variable. Users will receive an error message if they stratify by a variable that is chosen to be displayed on the main visualization.

<kbd> <img src="https://github.com/julietwomack/data-exploration-streamlit-application/blob/main/Screenshots/numerical-variable-options.png" /> </kbd>

#### Descriptive statistics
- Users will choose which numerical variable to explore and then will be presented with initial statistics (i.e., count, mean, standard deviation, and five number summary).

<kbd> <img src="https://github.com/julietwomack/data-exploration-streamlit-application/blob/main/Screenshots/numerical-descriptive-statistics-example.png" /> </kbd>

#### Visualizations
- Users have the option of seeing a scatterplot, histogram, boxplot, or heatmap.
- The visualization will dynamically change with the variable(s) the user picks to display.
- **Scatterplot:** (1) users will receive an error message if they choose the same variable to be visualized on the x and y-axis and (2) users can only select the continuous numerical variables to be displayed on the main scatterplot.
- **Histogram:** (1) users can choose how many bins they want to be displayed using a slider, (2) users can decide if they want a density curve to be overlayed on the histogram using radio buttons, and (3) users can only select a continuous numerical variable to be displayed on the main histogram.

<kbd> <img src="https://github.com/julietwomack/data-exploration-streamlit-application/blob/main/Screenshots/numerical-visualization-histogram-example.png" /> </kbd>

- **Boxplot:** users can only select a continuous numerical variable to be displays on the main boxplot.
- **Heatmap:** users will see a heatmap of ALL numerical variables (discrete and continuous) and it is annotated with the correlation coefficients.

### Character data
- Users can explore either descriptive statistics or visualizations with the character variables.

<kbd> <img src="https://github.com/julietwomack/data-exploration-streamlit-application/blob/main/Screenshots/character-data-options.png" /> </kbd>

#### Descriptive statistics
- Users will be presented the option to preview stats based on the selected character variable (i.e., count, number of unique values, most frequent value, and most frequent value count)

<kbd> <img src="https://github.com/julietwomack/data-exploration-streamlit-application/blob/main/Screenshots/character-data-ds-example.png" /> </kbd>

#### Visualizations
- Users will be presented count plots.
- Users will have the option to stratify the visualizations by another character variable or discrete numeric variable.

<kbd> <img src="https://github.com/julietwomack/data-exploration-streamlit-application/blob/main/Screenshots/character-data-viz-example.png" /> </kbd>

### Missing data
- Users will be presented a dataframe with the count and percent of missing data by feature.

<kbd> <img src="https://github.com/julietwomack/data-exploration-streamlit-application/blob/main/Screenshots/missing-data-options.png" /> </kbd>

- Users can opt to see the missing data visually (i.e., bar plot or heatmap).

<kbd> <img src="https://github.com/julietwomack/data-exploration-streamlit-application/blob/main/Screenshots/missing-data-viz-options-and-example.png" /> </kbd>

## Implications & Limitations
- Application can streamline the process of EDA for small data science projects.
- Application can help students new to data analysis and data science gain a "feeling" for their data quickly.
- Application works best with structured data.
- Application does not present any functionality with date variables.
- Application does not present all options for visualizations or descriptive statistics.
- Application may run slowly on large datasets or features with large cardinality.

## Future Additions
- Add functionality for date variables (i.e., descriptive statistics and visualization)
- Add functionality for resolving missing data (e.g., applying the median or mode value for missing data)
- Add functionality to download the visualizations as a JPG or PNG file
- Add functionality to change the appearance of the visualizations (i.e., color or palette)
