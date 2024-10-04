# Visualising the history of nobel prize winners

## Project Overview
The Nobel Prize has been among the most prestigious international awards since 1901. Each year, awards are bestowed in chemistry, literature, physics, physiology or medicine, economics, and peace. In addition to the honor, prestige, and substantial prize money, the recipient also receives a gold medal featuring an image of Alfred Nobel, the founder of the prize. 

This project utilizes a comprehensive dataset from the Nobel Prize API, recovered through DataCamp.com, documenting all prize winners from the inception of the awards in 1901 up until 2019. 

## Motivation
This analysis aims to explore the trends and insights regarding Nobel Prize winners over the years. By examining factors such as gender representation, nationalities, and the frequency of awards in different contexts, we can gain a deeper understanding of the impact and evolution of the Nobel Prize throughout its history.

## Challenges
Throughout the course of this project, I faced several challenges:

- **Missing Values:** A significant portion of the dataset contained missing values. I addressed this by dropping all rows with missing values to ensure the accuracy of the analysis. Although i admit, this isnt always the solution.
- **Data Visualization:** This was my first experience visualizing data with Seaborn. Initially, I found it challenging, but as I progressed, I became more comfortable with the library's capabilities and features.

## Technology Used
This project was developed using Python, along with several essential libraries:
- **Pandas** for data manipulation and analysis
- **NumPy** for numerical operations
- **Matplotlib** for basic plotting
- **Seaborn** for visualizations, it is built on top of Matplotlib

## Process
1. **Data Collection:** I sourced the dataset from DataCamp, which includes detailed information about the nobel prize winners.
2. **Data Cleaning:** I cleaned the data by addressing missing values, but i also through significantsorting, grouping and filtering throughout the process. 
4. **Data Visualization:** Using Matplotlib and Seaborn, I created various visual representations to highlight key insights, such as gender distribution, country representation, and decade-based trends.

## Conclusion
### Insights Gained from Nobel Prize Analysis
-  The analysis revealed that male laureates significantly outnumber female laureates, emphasizing the ongoing gender disparity in receiving Nobel Prizes.
-  The USA has a lionshare of all nobel prize recipients with the Highest Ratio of US winners up until they hit the peak a few decades ago.
- The insights gained could have looked different if the dataset had minimal or no missing values. As it stands, the dataset significantly compromised and any insight should be taken into consideration with caution.


## Credits
- **DataCamp:** For providing the dataset through the "Data Analyst with Python" career track, which made this project possible.
- **DataCamp:** For the seaborn course they offer on their platform, without that, i dont think i could have visualised with Seaborn for this project
