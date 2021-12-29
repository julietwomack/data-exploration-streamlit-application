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

### Initial data preview
- Users will be presented the first 7 rows of data
- Users will be presented a breakdown of the features by data type (i.e., number of continuous and discrete numerical variables and number of character variables)
- Users will be able to see a list of the feature names by data type

### Data exploration options
- Users will choose whether they want to explore the numerical, character, or missing data.

### Numerical data
- Users can explore either descriptive statistics or visualizations with the numerical features.
- For either option, users can choose to stratify their analysis by a character variable or a discrete numerical variable. Users will receive an error message if they stratify by a variable that is chosen to be displayed on the main visualization.

#### Numerical data: Descriptive statistics
- Users will choose which numerical variable to explore and then will be presented with initial statistics (i.e., count, mean, standard deviation, and five number summary).

#### Numerical data: Visualizations
- Users have the option of seeing a scatterplot, histogram, boxplot, or heatmap.
- The visualization will dynamically change with the variable(s) the user picks to display.
- **Scatterplot:** (1) users will receive an error message if they choose the same variable to be visualized on the x and y-axis and (2) users can only select the continuous numerical variables to be displayed on the main scatterplot.
- **Histogram:** (1) users can choose how many bins they want to be displayed using a slider, (2) users can decide if they want a density curve to be overlayed on the histogram using radio buttons, and (3) users can only select a continuous numerical variable to be displayed on the main histogram.
- **Boxplot:** users can only select a continuous numerical variable to be displays on the main boxplot.
- **Heatmap:** users will see a heatmap of ALL numerical variables (discrete and continuous) and it is annotated with the correlation coefficients.

### Character data
### Missing data

## Implications & Limitations
