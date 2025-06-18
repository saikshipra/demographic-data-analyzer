import pandas as pd
def calculate_demographic_data():
    # Define column names as per dataset description
    column_names = [
        'age', 'workclass', 'fnlwgt', 'education', 'education-num',
        'marital-status', 'occupation', 'relationship', 'race', 'sex',
        'capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'salary'
    ]
    
    # Load the dataset
    df = pd.read_csv('adult.data.csv', header=None, names=column_names, na_values=' ?', skipinitialspace=True)
    
    # Drop rows with missing values
    df = df.dropna()

    # 1. How many people of each race are represented in this dataset?
    race_count = df['race'].value_counts()

    # 2. What is the average age of men?
    average_age_men = round(df.loc[df['sex'] == 'Male', 'age'].mean(), 1)

    # 3. What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round((df['education'] == 'Bachelors').mean() * 100, 1)

    # 4. What percentage of people with advanced education (Bachelors, Masters, Doctorate) make more than 50K?
    higher_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    higher_education_rich = round((df[higher_education]['salary'] == '>50K').mean() * 100, 1)

    # 5. What percentage of people without advanced education make more than 50K?
    lower_education = ~higher_education
    lower_education_rich = round((df[lower_education]['salary'] == '>50K').mean() * 100, 1)

    # 6. What is the minimum number of hours a person works per week?
    min_work_hours = df['hours-per-week'].min()

    # 7. What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
    min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage_min_work_hours = round((min_workers['salary'] == '>50K').mean() * 100, 1)

    # 8. What country has the highest percentage of people that earn >50K and what is that percentage?
    country_counts = df['native-country'].value_counts()
    rich_country_counts = df[df['salary'] == '>50K']['native-country'].value_counts()
    rich_country_percentage = (rich_country_counts / country_counts * 100).dropna()
    highest_earning_country = rich_country_percentage.idxmax()
    highest_earning_country_percentage = round(rich_country_percentage.max(), 1)

    # 9. Identify the most popular occupation for those who earn >50K in India.
    india_rich = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    top_IN_occupation = india_rich['occupation'].mode()[0]

    # Return all results in a dictionary
    results = {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage_min_work_hours': rich_percentage_min_work_hours,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }

    return results

