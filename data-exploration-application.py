# Libraries
import time
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# Setting the layout to be wide (expand the entire screen for the user)
st.set_page_config(layout = "wide")

# Welcome message
st.header("Data Exploration Application")
st.markdown("By Juliet Womack / [LinkedIn](https://www.linkedin.com/in/juliet-womack/) / [GitHub](https://github.com/julietwomack) / [Email](mailto:julietmeiling@gmail.com)")
st.subheader("Welcome, start by uploading your datafile below:")

# File upload - user can upload their own CSV file to do initial data exploration
file = st.file_uploader(label = "Upload your CSV file", type = ['csv'], help="Currently, the application only supports comma-separated values (CSV) files.")

# If no file has been uploaded, user will receive ERROR message
if file is None:
    st.error("Please upload a file to proceed.")

# If a file is uploaded, the user will receive a SUCCESS message
if file is not None:
    # Success messgage for file upload
    time.sleep(3)
    st.success("File uploaded successfully!")

    # Write the CSV to a Pandas dataframe
    df = pd.read_csv(file)

    # Show user their dataset
    st.write("\n")
    st.subheader("Here is a preview of your data file:")
    st.write(df.head(7))

    # Obtain the numerical variables from data file
    numerics = ['float16', 'float32', 'float64']
    cont_num_df = df.select_dtypes(include = numerics)

    numerics_d = ['int16', 'int32', 'int64']
    discrete_num_df = df.select_dtypes(include = numerics_d)

    # Histogram definition
    def create_hist():
        var = st.selectbox("Choose a variable for the histogram", options = cont_num_df.columns)
        bin_num = st.slider("How many bins would you like for your histogram?", min_value=5, max_value=100)
        apply_kernel = st.radio("Apply a density curve?", options = [True, False])
        if len(character_df.columns) != 0:
            strat_check = st.checkbox("Check the box to stratify the histogram by a character variable or a discrete numeric variable")
            if strat_check:
                strat_var = st.selectbox("Pick a variable to stratify the histogram by:", options = char_list)
                st.write("\n")
                fig = plt.figure(figsize = (10,4))
                sns.histplot(data = df, x = var, hue = strat_var, bins=bin_num, kde = apply_kernel)
                plt.title("Histogram of {}".format(var), pad = 15)
                plt.xlabel("{}".format(var), labelpad = 15)
                plt.ylabel("Count", labelpad = 15)
                st.pyplot(fig)
            else:
                st.write("\n")
                fig = plt.figure(figsize = (10,4))
                sns.histplot(data = df, x = var, bins=bin_num, kde = apply_kernel)
                plt.title("Histogram of {}".format(var), pad = 15)
                plt.xlabel("{}".format(var), labelpad = 15)
                plt.ylabel("Count", labelpad = 15)
                st.pyplot(fig)
        else:
            st.write("\n")
            fig = plt.figure(figsize = (10,4))
            sns.histplot(data = df, x = var, bins=bin_num, kde = apply_kernel)
            plt.title("Histogram of {}".format(var), pad = 15)
            plt.xlabel("{}".format(var), labelpad = 15)
            plt.ylabel("Count", labelpad = 15)
            st.pyplot(fig)

    # boxplot definition
    def create_boxplot():
        # User can select the variable for the boxplot
        var = st.selectbox("Choose a variable for the boxplot", options = cont_num_df.columns)
        # if there are character variable(s), the user can choose to create a side-by-side boxplot or not
        if len(character_df.columns) != 0:
            strat_check = st.checkbox("Check the box to create a side-by-side boxplot by a character variable or a discrete numeric variable")
            if strat_check:
                strat_var = st.selectbox("Pick a variable to stratify the boxplot by:", options = char_list)
                fig = plt.figure(figsize = (10,4))
                sns.boxplot(data = df, x = var, y = strat_var)
                plt.title("Boxplot of {} by {}".format(var, strat_var), pad = 15)
                plt.xlabel("{}".format(var), labelpad = 15)
                st.pyplot(fig)
            else:
                fig = plt.figure(figsize = (10,4))
                sns.boxplot(data = df, x = var)
                plt.title("Boxplot of {}".format(var), pad = 15)
                plt.xlabel("{}".format(var), labelpad = 15)
                st.pyplot(fig)
        # If there are no character variables, the user will just get a regular, single boxplot
        else:
            fig = plt.figure(figsize = (10,4))
            sns.boxplot(data = df, x = var)
            plt.title("Boxplot of {}".format(var), pad = 15)
            plt.xlabel("{}".format(var), labelpad = 15)
            st.pyplot(fig)

    # Obtain the character variables from data file
    numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
    character_df = df.select_dtypes(exclude = numerics)

    # obtain the character variables and discrete numeric variables so numeric variables can be stratified
    char_list = character_df.columns.tolist() + discrete_num_df.columns.tolist()
    num_list = discrete_num_df.columns.tolist() + cont_num_df.columns.tolist()

    # Provide user the number of numerical and character variables
    st.write("\n")
    st.subheader("Number of Features by Type:")
    col1, col2, col3 = st.columns(3)
    with col1:
        cont_num_var = st.metric("Continuous Numerical Variables", len(cont_num_df.columns))
        with st.expander("Click to view Continuous Numerical Variables"):
            st.write("\n")
            for i in range(0, len(cont_num_df.columns)):
                st.write(cont_num_df.columns[i])
    with col2:
        dis_var = st.metric("Discrete Numerical Variables", len(discrete_num_df.columns))
        with st.expander("Click to view the Discrete Numerical Variables"):
            st.write("\n")
            for i in range(0, len(discrete_num_df.columns)):
                st.write(discrete_num_df.columns[i])
    with col3:
        char_var = st.metric("Character Variables", len(character_df.columns))
        with st.expander("Click to view the Character Variables"):
            st.write("\n")
            for i in range(0, len(character_df.columns)):
                st.write(character_df.columns[i])

    # User selects if they would like to explore the numerical or character features
    st.write("-----")
    st.subheader("What would you like to explore?")

    # If there are both numerical and character features, the user can look at all data exploration options
    if len(cont_num_df.columns) > 0 and len(character_df.columns) > 0:
        explore = st.radio("Select an option", options = [None, "Numerical Data","Character Data", "Missing Data"], key = 0)
    # If there are NO numerical features, the user can only see character and missing data exploration features
    elif len(cont_num_df.columns) == 0 and len(character_df.columns) > 0:
        explore = st.radio("Select an option", options = ["Character Data", "Missing Data"], key = 1)
    # If there are NO character features, the user can only see numerical and missing data exploration features
    elif len(cont_num_df.columns) > 0 and len(character_df.columns) == 0:
        explore = st.radio("Select an option", options = ["Numerical Data", "Missing Data"], key = 2)
    # If there are NO numerical and character features, the user will receive a warning
    else:
        st.error("The data cannot be explored. Please upload a different file.")
    st.write("-----")
    # If user selects that they want to explore numerical data, they have a choice between exploring the descriptive statistics or visualizations
    if explore == "Numerical Data":
        st.subheader("You have selected to explore {}. What would you like to see?".format(explore))
        num_explore = st.radio("Select an option", options = [None, 'Descriptive Statistics', 'Visualizations'])
        st.write("-----")
        # By default, the application will default to NONE, so they will get an error message.
        if num_explore == None:
            st.subheader("")
        # If the user selects an option other than None, they can see descriptive statistics or visualizations for numerical variables
        else:
            st.subheader("Ok, let's look at the {}.".format(num_explore))
        # START Explore DESCRIPTIVE STATISTICS for Numerical Data
        if num_explore == "Descriptive Statistics":
            # User selects the numerical variable they would like to explore
            var = st.selectbox("Select a numerical variable", options = num_list)
            # User can (optionally) select a character variable to group the descriptive statistics by IF the data set contains character variables.
            if len(character_df.columns) != 0:
                # User checkbox to choose whether or not to stratify the descriptive statistics by a character variable
                groupby = st.checkbox("Optional: Check the box to group by a character or a discrete numeric variable")
                if groupby: # if user chooses to stratify the descriptive statistics by a character variable
                    # variable the user wants to stratify by
                    group_var = st.selectbox("Select a character or a discrete numeric variable", options = char_list)
                    if var != group_var:
                        # produces the descriptive statistics stratified by the character variable, the .T transposes the dataframe
                        st.write(df.groupby(group_var)[var].describe().T)
                    else:
                        st.error("Cannot use the same variable to stratify by, please pick a different variable to stratify by.")
                else: # if user does not check the box, then descriptive statistics will be run on the single numerical variable
                    st.write(df[var].describe())
            else: # if there are no character variables in the dataset, then just descriptive statistics on the single numerical variable will be produced
                st.write(df[var].describe())
        #END Explore Descriptive Statistics for Numerical Data

        # Start Explore VISUALIZATIONS for Numerical Data
        elif num_explore == "Visualizations":
            explore_viz = st.radio("Select an option",  [None, 'Scatterplot', 'Histogram', "Boxplot", "Heatmap"])

            # Scatterplots for numerical variables
            if explore_viz == "Scatterplot":
                st.subheader("You have chosen to look at a {}. Please select your variables.".format(explore_viz))
                st.write("\n")

                # User can select the variable on the x-axis
                x_var = st.selectbox("Select variable for the x-axis:", options = cont_num_df.columns)

                # User can select the variable on the y-axis
                y_var = st.selectbox("Select variable for the y-axis:", options = cont_num_df.columns)
                # If there are character features and the x-variable and y-variable are different, then the user can select a character variable or discrete numeric variable to stratify by or they can opt not to.
                if len(character_df.columns) != 0 and x_var != y_var:
                    strat_check = st.checkbox("Optional: Check the box to stratify the scatterplot by a character variable or a discrete numeric variable.")
                    if strat_check: # If the user wants to stratify, a scatterplot will be generated with the stratified variable colored differently
                        st.write("\n")
                        strat_var = st.selectbox("Select the variable to stratify the scatterplot by:", options = char_list)
                        st.write("\n\n")
                        fig = plt.figure(figsize = (10,4))
                        sns.scatterplot(data = df, x = x_var, y = y_var, hue = strat_var)
                        plt.title("Scatterplot of {} and {} Stratified by {}".format(x_var, y_var, strat_var), pad = 15)
                        plt.xlabel("{}".format(x_var), labelpad = 15)
                        plt.ylabel("{}".format(y_var), labelpad = 15)
                        st.pyplot(fig)
                    else: # If the user does not want to stratify
                        st.write("\n\n")
                        fig = plt.figure(figsize = (10,4))
                        sns.scatterplot(data = df, x = x_var, y = y_var)
                        plt.title("Scatterplot of {} and {}".format(x_var, y_var), pad = 15)
                        plt.xlabel("{}".format(x_var), labelpad = 15)
                        plt.ylabel("{}".format(y_var), labelpad = 15)
                        st.pyplot(fig)
                # If the user selects the same variables for the x-axis and y-axis for the scatterplot
                elif len(character_df.columns) != 0 and x_var == y_var:
                    st.error("Please select two different variables for the scatterplot.")
                elif len(character_df.columns) == 0 and x_var == y_var:
                    st.error("Please select two different variables for the scatterplot.")
                # If the user does not want to stratify, a single scatterplot will be generated with the two variables of choice.
                elif len(character_df.columns) == 0:
                    st.write("\n\n")
                    fig = plt.figure(figsize = (10,4))
                    sns.scatterplot(data = df, x = x_var, y = y_var)
                    plt.title("Scatterplot of {} and {}".format(x_var, y_var), pad = 15)
                    plt.xlabel("{}".format(x_var), labelpad = 15)
                    plt.ylabel("{}".format(y_var), labelpad = 15)
                    st.pyplot(fig)

            # If user wants to generate a histogram for their numerical variable(s) - will allow the user to generate a single histogram, stratified histogram, and a histogram with the density plot overlayed
            elif explore_viz == "Histogram":
                st.subheader("You have chosen to look at a {}. Please select your variables.".format(explore_viz))
                st.write("\n")
                create_hist()

            # If the user wants to generate a boxplot - will also allow the user to produce side-by-side boxplot based on a character variable (if they are in the dataset)
            elif explore_viz == "Boxplot":
                st.subheader("You have chosen to look at a {}. Please select your variables.".format(explore_viz))
                st.write("\n")
                create_boxplot()

            # If the user wants to generate a heatmap for numerical variables
            elif explore_viz == "Heatmap":
                st.header("You have chosen to look at a {}".format(explore_viz))
                st.write("\n")
                fig = plt.figure(figsize = (10,10))
                sns.heatmap(df.corr(), annot = True)
                plt.title("Heatmap for Numerical Variables", pad = 15)
                st.pyplot(fig)
            else:
                st.error("Please select an option to continue.")
        else:
            st.error("Please select an option to continue.")
        # END Explore VISUALIZATIONS for Numerical Data

    # START EDA for Character Variables
    elif explore == "Character Data":
        st.subheader("You have selected to explore {}. What would you like to see?".format(explore))
        # Allows user to select to explore character variables using descriptive statistics or visualizations
        char_explore = st.radio("Select an option", options = ['Descriptive Statistics', 'Visualizations'])
        # Descriptive statistics for character variables and will display different metrics for that character variable
        if char_explore == 'Descriptive Statistics':
            st.write("\n")
            char_var = st.selectbox("Pick a character variable to further explore:", options = character_df.columns)
            col1, col2, col3, col4 = st.columns(4)
            col1.metric("Count", len(df[char_var]))
            col2.metric("Unique Values", len(df[char_var].value_counts()))
            col3.metric("Most Frequent Value", df[char_var].mode()[0])
            col4.metric("Most Frequent Value Count", df[char_var].value_counts().head(1)[0].astype('str'))
        # Generates count plots for character or discrete numeric variables
        elif char_explore == 'Visualizations':
            # Character or discrete numeric variable to create the count plot from
            char_var = st.selectbox("Pick a character variable or discrete numeric variable to further explore:", options = char_list)
            # Checkbox for user to choose whether to stratify the countplot by another variable or not
            strat_check = st.checkbox("Check the box to stratify the countplot by another character variable or discrete numeric variable")
            if strat_check:
                # The variable the user selects to stratify the count plot by
                strat_var = st.selectbox("Pick a character variable or a discrete numeric variable to stratify by", options = char_list)
                # User will receive an error message if the character/discrete numeric variable is the same as the variable the user wants to stratify by
                if strat_var == char_var:
                    st.error("Please select a different character variable or discrete numeric variable to stratify by.")
                # if the user selects two different variables, the count plot will be generated
                else:
                    fig = plt.figure(figsize = (10,4))
                    sns.countplot(data = df, x = char_var, hue = strat_var)
                    plt.title("Count Plot for {} Stratifed by {}".format(char_var, strat_var), size = 12, pad = 15)
                    plt.xlabel("{}".format(char_var), labelpad = 15)
                    plt.ylabel("Count", labelpad = 15)
                    st.pyplot(fig)
            # If the user does not want to stratify, they will get a single count plot
            else:
                fig = plt.figure(figsize = (10,4))
                sns.countplot(data = df, x = char_var, order = df[char_var].value_counts().index)
                plt.title("Count Plot for {}".format(char_var), size = 12, pad = 15)
                plt.xlabel("{}".format(char_var), labelpad = 15)
                plt.ylabel("Count", labelpad = 15)
                st.pyplot(fig)

    # Exploring missing data through descriptive statistics and visualizations
    elif explore == "Missing Data":
        st.subheader("You have selected to explore {}.".format(explore))

        # create dataframe for missing data
        column_names = df.columns # names of all the features
        missing_count = df.isnull().sum() # discrete count of missing values by features
        missing_pct = ((df.isnull().sum()/len(df))*100.00).astype('float16') # percent of missing values by feature

        missing_data = pd.DataFrame([column_names, missing_count, missing_pct], index = ["Features", "Count Missing", "Percent Missing"])
        missing_data_transposed = missing_data.transpose().sort_values(by = ['Percent Missing'], axis = 0, ascending = False)

        st.table(missing_data_transposed)
        # User will receive a message if there is no missing data in the dataset
        if sum(missing_count) == 0:
            st.success("Congrats! There is no missing data.")
        # User will receive the option to view missing dataset in a barplot if there are truly missing data in the dataset
        else:
            missing_check = st.checkbox(label = 'Check the box to display the missing data visually.')
            if missing_check:
                # Allows users to select a specific way to display the missing data visually
                st.write("\n")
                st.subheader('Select the plot you would like to see\n\n')
                missing_viz = st.radio('Select an option', options = ['Bar Plot by Count', 'Bar Plot by Percent', 'Heatmap'])

                # Font size and label padding size for the bar plots to display either count or percent of missing data
                font_size = 14
                pad_size = 15

                # Bar plot displaying count of missing data by feature
                if missing_viz == 'Bar Plot by Count':
                    plot = plt.figure(figsize = (15,4))
                    sns.barplot(data = missing_data_transposed, x = 'Features', y = 'Count Missing')
                    plt.title('\nBar Plot of Missing Data', pad = pad_size, size = font_size)
                    plt.xlabel('Features', labelpad = pad_size, size = font_size)
                    plt.ylabel('Count of Missing Data', labelpad = pad_size, size = font_size)
                    plt.tight_layout()
                    st.pyplot(plot)
                # Bar plot displaying the percent of missing data by feature
                elif missing_viz == 'Bar Plot by Percent':
                    plot = plt.figure(figsize = (15,4))
                    sns.barplot(data = missing_data_transposed, x = 'Features', y = 'Percent Missing')
                    plt.title('\nBar Plot of Missing Data', pad = pad_size, size = font_size)
                    plt.xlabel('Features', labelpad = pad_size, size = font_size)
                    plt.ylabel('Percent of Missing Data', labelpad = pad_size, size = font_size)
                    plt.tight_layout()
                    st.pyplot(plot)
                # Displays a heatmap of missing data by feature.
                elif missing_viz == 'Heatmap':
                    plot = plt.figure(figsize = (10,10))
                    plt.title("\nHeatmap of Missing Data")
                    sns.heatmap(df.isna().transpose(), cmap = "rocket", cbar_kws={'label':'Missing Data'})
                    st.pyplot(plot)
    # If NONE is selected, user will receive this error message.
    else:
        st.error("Select an option to explore the data")
