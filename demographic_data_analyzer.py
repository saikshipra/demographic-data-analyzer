import pandas as pd

def demographic_data_analysis(print_data=True):
    # Load data
    df = pd.read_csv("adult.data.csv")

    # How many people of each race are represented in this dataset?
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round((df['education'] == 'Bachelors').sum() / len(df) * 100, 1)

    # Advanced education: Bachelors, Masters, or Doctorate
    advanced_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    higher_education = df[advanced_education]
    lower_education = df[~advanced_education]

    # % with salary >50K
    higher_education_rich = round((higher_education['salary'] == '>50K').sum() / len(higher_education) * 100, 1)
    lower_education_rich = round((lower_education['salary'] == '>50K').sum() / len(lower_education) * 100, 1)

    # Minimum hours per week
    min_work_hours = df['hours-per-week'].min()

    # % earning >50K among those who work min hours
    min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round((min_workers['salary'] == '>50K').sum() / len(min_workers) * 100, 1)

    # Country with highest % of >50K earners
    country_salary_stats = df.groupby('native-country')['salary'].value_counts(normalize=True).unstack()
    country_salary_stats = country_salary_stats.fillna(0)
    highest_earning_country = country_salary_stats['>50K'].idxmax()
    highest_earning_country_percentage = round(country_salary_stats['>50K'].max() * 100, 1)

    # Most popular occupation for >50K earners in India
    top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].value_counts().idxmax()

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print("Percentage with Bachelors degrees:", percentage_bachelors)
        print("Percentage with higher education that earn >50K:", higher_education_rich)
        print("Percentage without higher education that earn >50K:", lower_education_rich)
        print("Min work time:", min_work_hours)
        print("% with salary >50K among those who work fewest hours:", rich_percentage)
        print("Country with highest % of rich:", highest_earning_country)
        print("Highest % of rich people in country:", highest_earning_country_percentage)
        print("Top occupations in India for those who earn >50K:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
