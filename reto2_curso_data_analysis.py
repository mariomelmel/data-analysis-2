import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the
    # index labels.
    races = df['race']
    obj_races = {}
    for race in races:
        if race in obj_races:
            obj_races[race] += 1
        else:
            obj_races[race] = 1

    race_count = pd.DataFrame({'race': obj_races.keys(), 'count': obj_races.values()})

    # What is the average age of men?    
    age_mean_men = df.loc[df['sex'] == 'Male', 'age']
    average_age_men = age_mean_men.mean()
    average_age_men = round(average_age_men, 1)

    # What is the percentage of people who have a Bachelor's degree?
    number_total = df.iloc[:, :1]
    num_total = len(number_total)

    number_bachelors = df.loc[df['education'] == 'Bachelors', ['education']]
    num_bachelors = len(number_bachelors)
    percentage_bachelors = num_bachelors / num_total * 100
    percentage_bachelors = round(percentage_bachelors, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = len(
        df.loc[
            (df['education'] == 'Bachelors') |
            (df['education'] == 'Masters') |
            (df['education'] == 'Doctorate'),
            'education'
        ]
    )
    lower_education = num_total - higher_education
    # percentage with salary >50K
    number_higher_edu_rich = len(
        df.loc[
            (df['education'] == 'Bachelors') |
            (df['education'] == 'Masters') |
            (df['education'] == 'Doctorate') &
            (df['fnlwgt'] > 50000),
            'education'
        ]
    )
    higher_education_rich = number_higher_edu_rich / higher_education * 100
    higher_education_rich = round(higher_education_rich, 1)

    number_lower_edu_rich = len(
        df.loc[
            (df['education'] != 'Bachelors') &
            (df['education'] != 'Masters') &
            (df['education'] != 'Doctorate') &
            (df['fnlwgt'] > 50000),
            'education'
        ]
    )
    lower_education_rich = number_lower_edu_rich / lower_education * 100
    lower_education_rich = round(lower_education_rich, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = len(
        df.loc[
            (df['hours-per-week'] == min_work_hours) &
            (df['fnlwgt'] > 50000),
            'hours-per-week'
        ]
    )

    rich_percentage = num_min_workers / num_total * 100
    rich_percentage = round(rich_percentage, 1)

    # What country has the highest percentage of people that earn >50K?

    countries = df.loc[(df['fnlwgt'] > 50000), 'native-country']
    obj_country = {}
    country_counter = 0
    for country in countries:
        if country in obj_country:
            obj_country[country] += 1
        else:
            obj_country[country] = 1
        country_counter += 1

    highest_earning_country = max(obj_country, key=obj_country.get)
    highest_earning_country_percentage = obj_country[highest_earning_country] / country_counter * 100
    highest_earning_country_percentage = round(highest_earning_country_percentage, 1)

    # Identify the most popular occupation for those who earn >50K in India.

    occupations = df.loc[(df['fnlwgt'] > 50000), 'occupation']
    obj_occupation = {}
    for occupation in occupations:
        if occupation in obj_occupation:
            obj_occupation[occupation] += 1
        else:
            obj_occupation[occupation] = 1

    top_IN_occupation = max(obj_occupation, key=obj_occupation.get)

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

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


calculate_demographic_data()
