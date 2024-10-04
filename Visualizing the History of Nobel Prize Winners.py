import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pandas import DataFrame
import seaborn as sns
# Load the Dataset
nobel_prize_dirty = pd.read_csv('/Users/usamasuleiman/Downloads/workspace 3/data/nobel.csv')
# Dropping all rows with any missing values
nobel_prize_cleaned = nobel_prize_dirty.dropna().reset_index(drop=True)

# Resetting the index to start from 1 instead of 0
nobel_prize_cleaned.index = nobel_prize_cleaned.index + 1

# Alot of values are missing, but such it is a balancing act.
# Printing
print(nobel_prize_dirty.shape)  # Before cleaning
print(nobel_prize_cleaned.shape)  # After cleaning

# Question 1: What is the most commonly awarded gender?

# Grouping the relevant columns in our dataset
top_gender = nobel_prize_cleaned.groupby("sex")["prize"].count().reset_index()

# Fixing the index by making it start from = 1 instead of 0
top_gender = top_gender.sort_values(by="prize", ascending = False)

# Lets also make sure the index follows the amount of prizes,that way, the gender with most prizes is on top!
top_gender.reset_index(drop = True, inplace = True)

# Printing
print(top_gender) #Looks like Men are the most commonly awarded gender!

#Visualising the most commonly awarded gender
plt.figure(figsize=(6, 4))
sns.barplot(x=top_gender['sex'], y=top_gender['prize'], palette='muted')

plt.title('Most Commonly Awarded Gender in Nobel Prizes')
plt.xlabel('Gender')
plt.ylabel('Number of Prizes')
plt.show()


# Question 2. What is the most commonly awarded birth country? Lets start by grouping the relevant columns again
top_country = nobel_prize_cleaned.groupby("birth_country")["prize"].count().reset_index()

# Now lets make it so that the index follows the count of prizes
top_country = top_country.sort_values(by = "prize", ascending = False)
top_country.reset_index(drop= True, inplace = True)

# Printing
print("top country: USA", top_country) #Looks like the USA is the country is the most commonly awarded country! USA! USA! USA!

# Visualising the top 10 countries with the most Nobel Prize recipients
plt.figure(figsize=(10, 6))
sns.barplot(x=top_country['birth_country'].head(10),
            y=top_country['prize'].head(10),
            palette="muted")
plt.xticks(rotation=90)  # Rotating x-axis labels for better readability
plt.title('Top 10 Countries by Nobel Prize Count')
plt.xlabel('Country')
plt.ylabel('Number of Prizes')
plt.show()


# Question 3: Which decade had the highest ratio of US-born Nobel Prize winners to total winners in all categories?

# We'll start by creating a column whereby we group years by decade
nobel_prize_cleaned["decade"] = (nobel_prize_cleaned["year"] // 10) * 10

# Filtering for all nobel prize winners born in USA
us_born_w = nobel_prize_cleaned[nobel_prize_cleaned["birth_country"] == "United States of America"]

# Lets do the same with all nobel prize winners NOT born in the USA
non_us_born_w = nobel_prize_cleaned[nobel_prize_cleaned["birth_country"] != "United States of America"]

# Now lets group US winners by decade to count the total number of USA Nobel Prize winners in each decade
us_w_by_d = us_born_w.groupby("decade").size().sort_values(ascending = False)

# Doing the same for the prize winners from elsewhere
non_us_w_by_d = non_us_born_w.groupby("decade").size().sort_values(ascending = False)

# Calculating the highest ratio of US born prize winners versus total winners in all categories
ratio_w = (us_w_by_d/non_us_w_by_d) * 100

# Cleaning up the results i obtained by removing missing values, converting the floats to integers as well as sorting!
max_decade_usa = ratio_w.dropna().astype(int).sort_values(ascending=False)

# Printing
print(max_decade_usa) # It looks like the decade with the highest ratio of US born prize winners was the 1990's, 173%!

# Plotting (visualising) the ratio of US-born winners per decade
plt.figure(figsize=(10, 6))
sns.barplot(x=max_decade_usa.index, y=max_decade_usa.values, palette="coolwarm")
plt.title("Ratio of US-born Nobel Prize Winners by Decade")
plt.xlabel("Decade")
plt.ylabel("Ratio (%)")
plt.show()

# Question 4: Which decade and Nobel Prize category combination had the highest proportion of female laureates?

# Filtering for female Nobel prize recipients
fem_prize_rec = nobel_prize_cleaned[nobel_prize_cleaned["sex"] == "Female"].groupby(["decade", "category"]).size().reset_index(name = "female_count")

#Filtering for male Nobel prize recipients
mal_prize_rec = nobel_prize_cleaned[nobel_prize_cleaned["sex"] == "Male"].groupby(["decade", "category"]).size().reset_index(name = "male_count")

#Merging the two Df on the columns "decade" and "category, this allows for us to do our calculations within one "structure", using inner join
merged_counts = pd.merge(fem_prize_rec, mal_prize_rec, on=['decade', 'category'], how='inner')

# Printing
print(merged_counts)

#Calculating total winners
merged_counts["total_merged_counts"] = merged_counts["female_count"] + merged_counts["male_count"]

# Printing
print(merged_counts["total_merged_counts"])

# Calculating the proportion of female laureates
merged_counts['female_proportion'] = (merged_counts['female_count'] / merged_counts['total_merged_counts']) * 100

# Finding the decade and category combination with the highest proportion of female laureates
max_female_proportion = merged_counts.sort_values(by='female_proportion', ascending=False).head(1)

# Creating the dictionary with the decade as the key and category as the value
max_female_dict = {int(max_female_proportion["decade"].values[0]): max_female_proportion["category"].values[0]}

# Printing
print(max_female_dict) #The decade with the highest proportion of women was in the 2000's in the "Economics" category!

# Question 5: Who was the first woman to receive a Nobel Prize, and in what category?

# Filtering again for female recipients
fem_prize_rec = nobel_prize_cleaned[nobel_prize_cleaned["sex"] == "Female"]

# Finding the earliest year
earliest_year = fem_prize_rec['year'].min()

# Same operation on the DataFrame
first_fem_prize = fem_prize_rec[fem_prize_rec['year'] == earliest_year]

# Getting the first row in case there could be multiple laureates in that year
first_fem_laureate = first_fem_prize.iloc[0]

# Extracting the relevant information
first_fem_name = first_fem_laureate['full_name']
first_fem_category = first_fem_laureate['category']

# Printing
print("The first woman to receive a Nobel Prize was", first_fem_name, "in the category of", first_fem_category, "in the year", earliest_year)

# Question 6: Which individuals or organizations have won more than one Nobel Prize throughout the years?
# Store the full names in a list named repeat_list.


# Starting by counting the number of prizes for each individual and organization
multiple_winners_individuals = nobel_prize_cleaned.groupby('full_name').size().reset_index(name='count')
multiple_winners_organizations = nobel_prize_cleaned.groupby('organization_name').size().reset_index(name='count')

# Filtering for those with more than one prize
multiple_winners_individuals = multiple_winners_individuals[multiple_winners_individuals['count'] > 1]
multiple_winners_organizations = multiple_winners_organizations[multiple_winners_organizations['count'] > 1]

#Storing the names in a list
repeat_list = ("Individuals who have won more than one Nobel Prize:", multiple_winners_individuals), ("Organizations that have won more than one Nobel Prize:", multiple_winners_organizations)

# Printing
print(repeat_list)

#Visualising the final results

# Individuals with more than one Nobel Prize
plt.figure(figsize=(10, 6))
sns.barplot(x=multiple_winners_individuals['full_name'],
            y=multiple_winners_individuals['count'],
            palette='muted')

plt.xticks(rotation=90)  # Rotating x-axis labels for better readability
plt.title('Individuals with Multiple Nobel Prizes')
plt.xlabel('Full Name')
plt.ylabel('Number of Prizes')
plt.show()


# Organizations with more than one Nobel Prize
plt.figure(figsize=(10, 6))
sns.barplot(data=multiple_winners_organizations, x='organization_name', y='count')
plt.xticks(rotation=90)  # Rotating x-axis labels for better readability
plt.title('Organizations with More than One Nobel Prize')
plt.xlabel('Organizations')
plt.ylabel('Number of Prizes')
plt.show()