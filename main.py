from demographic_data_analyzer import calculate_demographic_data

def main():
    results = calculate_demographic_data()

    print("Race Count:\n", results['race_count'], "\n")
    print("Average age of men:", results['average_age_men'], "\n")
    print(f"Percentage with Bachelor's degrees: {results['percentage_bachelors']}%\n")
    print(f"Percentage with higher education earning >50K: {results['higher_education_rich']}%\n")
    print(f"Percentage without higher education earning >50K: {results['lower_education_rich']}%\n")
    print(f"Minimum work hours per week: {results['min_work_hours']}\n")
    print(f"Percentage of rich among those who work minimum hours: {results['rich_percentage_min_work_hours']}%\n")
    print(f"Highest earning country: {results['highest_earning_country']} with {results['highest_earning_country_percentage']}%\n")
    print(f"Top occupation in India for those earning >50K: {results['top_IN_occupation']}\n")

if __name__ == "__main__":
    main()

