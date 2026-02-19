# EDA how to and why

## Objective

The exploratory data analysis provides immediate value to the clients, as it provides information about how various features are influencing the target variable (in this case the prices of houses). Furthermore the data visualization generated in this stage can be of use in presentations. A good EDA is the foundation step of further modeling stages and also has direct impact on the quality of models produced later on.

One of the famous sayings about working with data, is "garbage in, garbage out"; so the first thing you want to do before you analyse the data and draw conclusions, is to understand it and make sure your data is as clean as possible.

Data cleaning and data wrangling usually can account for up to 70% of the data scientist work. Your objective here would be to examine and preprocess the dataset. Your client wants to get a good understanding of the general housing condition in Seattle and surroundings and furthermore to have some recommendations tailored to their needs.

![](https://thumbor.forbes.com/thumbor/711x302/https://blogs-images.forbes.com/gilpress/files/2016/03/Time-1200x511.jpg?width=960)

## Why is this important?

"Garbage In Garbage Out" is not only relevant to the modeling step. But also to the step where one draws conclusions and insights from data. Insights derived from wrong data will not be trustworthy. And you want your analysis and your conclusion to be as **trustworthy** as possible.

# General methodology

- data science is an iterative process
- write rough draft/ todo list of plan with placeholders
  - do only simple plots, you should only invest more time in the plots you really want to keep in the end
  - main questions should already be answered -> POC (proof of concept)
  - iterate: go deeper, go prettier, go better
  - clean up .. feel free to delete things that are not useful anymore
  - optional: moving code to functions

The work is **time-boxed**, and with that in mind, you need to change how you approach the task. You will want to employ an iterative approach.

# Workflow

This is a recommended workflow, especially for people who are on their beginning journey with EDA.

### Understanding the Data

# Column Names and descriptions for King County Data Set

- **id** - unique identified for a house
- **dateDate** - house was sold
- **pricePrice** - is prediction target
- **bedroomsNumber** - # of bedrooms
- **bathroomsNumber** - # of bathrooms
- **sqft_livingsquare** - footage of the home
- **sqft_lotsquare** - footage of the lot
- **floorsTotal** - floors (levels) in house
- **waterfront** - House which has a view to a waterfront
- **view** - quality of view
- **condition** - How good the condition is ( Overall )
- **grade** - overall grade given to the housing unit, based on King County grading system
- **sqft_above** - square footage of house apart from basement
- **sqft_basement** - square footage of the basement
- **yr_built** - Built Year
- **yr_renovated** - Year when house was renovated
- **zipcode** - zip
- **lat** - Latitude coordinate
- **long** - Longitude coordinate
- **sqft_living15** - The square footage of interior housing living space for the nearest 15 neighbors
- **sqft_lot15** - The square footage of the land lots of the nearest 15 neighbors

### Research Questions and Hypothesis Generation

- *Research Questions* are questions that arise from a researcher guessing about reality (data). They are written in the form of a question.
- *Hypotheses* are assumptions or educated guesses we make about the data, using our domain knowledge. You can form a hypothesis in the form of *"if/then"* or *"the more the"*. A Hypothesis is formed as a measurable (operationisable) statement you can validate by looking at data.
- A research question can have multiple hypotheses attached to it.
```
+------------------------------------------------+-------------------------------------------------------------------+----------------------+
| Question                                       | Hypotheses                                                        | Indicators           |
+------------------------------------------------+-------------------------------------------------------------------+----------------------+
| Does the location of a house affect the price? | 1. The closer a house is to the city center, the higher the price| - geolocation        |
|                                                +-------------------------------------------------------------------+----------------------+
|                                                | 2. If a house is located to water, then the price is higher       | - waterfront(yes/no) |
+------------------------------------------------+-------------------------------------------------------------------+----------------------+
```
- The more concrete questions and related hypothesis you have, the easier and more focused your EDA can be. For more examples check this [article](https://www.analyticsvidhya.com/blog/2020/11/an-efficient-way-of-performing-eda-hypothesis-generation/).
- Ask yourself some questions about the data, the more the merrier. (e.g. Does the larger size of a house increase the price? Are houses in the South of the region more expensive?). In this step ask at least 3 questions.
- Thinking of the client, think of a couple of hypotheses that fit to their portion of the data. For some client not all the data will be relevant, e.g. the ones interested in houses in the city center might not care about the suburbs.

### Exploring the data

- Check distributions of the continuous variables, for example by producing histograms for each of them.
- Check the distributions for the categorical variables, by producing plots/tables of counts.
- Look at the histograms and check for clues or patterns: can you identify groups, are the distributions skewed, do you have extreme values or outliers, where is the data centered. Do you need to remove some data?

### Cleaning the data

- Dealing with missing values: remove (rows, or columns) or impute data
- Dealing with extreme values or outliers: remove data
- Transform data where necessary, e.g. to log or sqrt to try to get some feature closer to normal distribution, or binning
- How much data did you throw away? 😅

### Relationships in the data

- Compute the correlation matrix and plot it.
- Check the relationships between the values in your hypothesis and the targe (price)
- Are all the conclusions expected or unexpected?
- If helpful create new features by combining existing ones, e.g. if you have distance and time you could derive the speed.

### Presenting your work

- Do not forget to document your work, use markdown cells in the notebook to explain what you do, why you do it and interpret the results.
- For every plot you have, there should be at least a sentence saying what you see in it 🤓
- There is an expected format to your presentation following specific questions:
  - who are you, who is your client
  - what data are you working on (time span, location, size)
  - data overview
  - introducing your 3 main hypotheses
  - the results of the analysis of the hypotheses (visual/statistical)
  - insights and recommendations for client
  - Check this out for more tips on [how to make great data science presentations](https://www.dataknowsall.com/storytelling.html)

For more information regarding the image bellow check out the [EDA Checklist](https://github.com/neuefische/datascience-infographics/blob/main/EDA_Checklist.md) .

![EDA Checklist](https://raw.githubusercontent.com/neuefische/datascience-infographics/main/images/EDA_Checklist.png)
