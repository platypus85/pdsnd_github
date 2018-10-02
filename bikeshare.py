import time
import pandas as pd
import numpy as np
import calendar

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        try:
            city = input(
                "Please, enter one of the following cities: Chicago, New York City, or Washington. -> ").lower()
        except KeyboardInterrupt:
            print("\nSorry, an error occurred. Please, try again.\n")
            continue
        if city not in ('chicago', 'new york city', 'washington'):
            print("\nSorry, wrong choice. Please, try again.\n")
        else:
            break

    # get user input for month (all, january, february, ... , june)
    while True:
        try:
            month = input(
                "\nThanks! Please, enter one of the first six months of the year: January, February, March, April, May, June, OR 'all' to access data from all the six months. -> ").strip().lower()
        except KeyboardInterrupt:
            print("\nSorry, an error occurred. Please, try again.\n")
            continue
        if month not in ('all', 'january', 'february', 'march', 'april', 'may', 'june'):
            print("\nSorry, wrong choice. Remember to use this format: January, February, March, April, May, June, OR 'all' to access data from all the six months.\n")
        else:
            break

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day = input(
                "\nThanks! Please, enter a day of the week (Monday to Sunday), OR 'all' to access data from the whole week. -> ").strip().lower()
        except KeyboardInterrupt:
            print("\nSorry, an error occurred. Please, try again.\n")
            continue
        if day not in ('all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'):
            print("\nSorry, wrong choice. Remember to use the full name of the day, OR 'all' for the whole week.\n")
        else:
            break

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    month = month.title()
    day = day.title()

    #  Loading data file
    df = pd.read_csv(CITY_DATA[city])

    # Converting Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extracting month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'All':
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1

        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'All':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    most_common_month = df['month'].mode()[0]
    print("The most common month was: " +
          str(calendar.month_name[most_common_month]) + ".\n")

    # display the most common day of week
    most_common_day_week = df['day_of_week'].mode()[0]
    print("The most common day of the week was: " + most_common_day_week + ".\n")

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_start_hour = df['hour'].mode()[0]
    print("The most common start hour was: " +
          str(most_common_start_hour) + ".")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_commonly_used_start_station = df['Start Station'].mode()[0]
    print("The most commonly used START station was: " +
          most_commonly_used_start_station + ".\n")

    # display most commonly used end station
    most_commonly_used_end_station = df['End Station'].mode()[0]
    print("The most commonly used END station was: " +
          most_commonly_used_end_station + ".\n")

    # display most frequent combination of start station and end station trip
    df['Station Combination'] = df['Start Station'] + " ### " + df['End Station']
    most_frequent_combination = df['Station Combination'].mode()[0]
    print("The most frequent combination of start station and end station trip was: " +
          most_frequent_combination + ".")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("Total travel time: ", total_travel_time)

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("\nMean travel time: ", mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_type = df['User Type'].value_counts()
    print('Count of user types: ', user_type)

    # Display counts of gender
    if 'Gender' in df.columns:
        gender = df['Gender'].value_counts()
        print('\nCount of gender: ', gender)

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_birth= df['Birth Year'].max()
        print('\nEarliest year of birth:', int(earliest_birth))

        latest_birth= df['Birth Year'].min()
        print('\nMost recent year of birth:', int(latest_birth))

        common_birth_year= df['Birth Year'].mode()[0]
        print('\nThe most common year of birth:', int(common_birth_year))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
