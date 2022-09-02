import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    
    while True:
        city = input('Please enter which city you want to explore : chicago, washington,  new york city? \n> ').lower()
        if city not in CITY_DATA:
          print('wrong choice, choose again') 
        else:
            break
    filter = input('would you like to filter by month, day, both or none?').lower()
    while filter not in (['month', 'day', 'both', 'none']):
        print("You provided an invalid selection")
    
    
    
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    month = ""
    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['january', 'february', 'march', 'april', 'may', 'june'] 
               
    if filter == 'month' or filter == 'both':
        month = input("Please select the month you would like to see results for: All, January, February, March, April, May, or June?").lower()
    while month not in months:
        print ('You provided and invalid choice')
        month= input("Please select the month you would like to see results for: All, January, February, March, April, May, or June?").lower()
    else:
        month = 'all'

    day = ""
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday'] 
    if filter == 'day' or filter == 'both':
       day = input("type the day you would like to see results: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday or Saturday?").lower() 
    while day not in days: 
       print('wrongh selection, try again')
       day = input("type the day you would like to see results: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday or Saturday?").lower() 
    else: 
        day = 'all'
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    
    df = pd.read_csv(CITY_DATA[city]) 
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month_name()
    df['day'] = df['Start Time'].dt.day_name()
    

    #Filter by month only
    if month != 'all' and day == 'all':
        mdf = df[(df['month']==month.lower())]
        return mdf

    #Filter by day only
    elif day != 'all' and month == 'all':
        ddf = df[(df['day']==day())]
        return ddf

    #Filter by month and day
    elif month != 'all' and day != 'all':
        mddf = df[(df['month']==month.lower()) & (df['day']==day())]
        return mddf
   #No filter
    else:
        return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    common_month = df['month'].value_counts().idxmax()
    
    print('The most common month is: {}.'.format(common_month))


    # TO DO: display the most common day of week
    days = ['monday','tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    day = df['day'].value_counts().idxmax()
    print('The most common day in this data set is {}.'.format(day))


    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
  
    print(f'Most common hour is:{popular_hour}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print(f'The most used start station is:{popular_start_station}')

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print(f'The most used end station is: {popular_end_station}')

    # TO DO: display most frequent combination of start station and end station trip
    popular_trip = df['Start Station'] + 'to' + df['End Station']
    print(f'The most popular trip is: from {popular_trip.mode()[0]}')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_duration = (pd.to_datetime(df['End Time']) - pd.to_datetime(df['Start Time'])).sum()
    days = total_travel_duration.days
    hours = total_travel_duration.seconds // (60*60)
    minutes = total_travel_duration.seconds % (60*60) // 60
    seconds = total_travel_duration.seconds % (60*60) % 60
    print(f'Total travel time: {days} days {hours} hours {minutes} minutes {seconds} seconds')

    # TO DO: display mean travel time
    average_travel_duration = (pd.to_datetime(df['End Time']) - pd.to_datetime(df['Start Time'])).mean()
    days = average_travel_duration.days
    hours = average_travel_duration.seconds // (60*60)
    minutes = average_travel_duration.seconds % (60*60) // 60
    seconds = average_travel_duration.seconds % (60*60) % 60
    print(f'The average travel time: {days} days {hours} hours {minutes} minutes {seconds} seconds')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print(df['User Type'].value_counts())
    print('\n\n')


    # TO DO: Display counts of gender
    if 'Gender' in (df.columns):
        print(df['Gender'].value_counts())
        print('\n\n')

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in (df.columns):
        year = df['Birth Year'].fillna(0).astype('int64')
        print(f'The earliest birth year is: {year.min()}\n most recent is: {year.max()}\n and most common birth year is:{year.mode()[0]}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    raw = input('\nWould you like to display the raw data?\n')
    if raw.lower() == 'yes':
        count = 0
        while True:
            print(df.iloc[count:count+5])
            count += 5
            ask = input('Next 5 rows?')
            if ask.lower() != 'yes':
                break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
