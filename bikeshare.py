import time
import pandas as pd
import numpy as np

# Load data files
chicago_df = pd.read_csv('chicago.csv')
new_york_df = pd.read_csv('new_york_city.csv')
washington_df = pd.read_csv('washington.csv')




CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

import ipywidgets as widgets
from IPython.display import display

def get_filters():
    print('Hello! Let\'s explore some US bikeshare data!')
    cities = ['chicago', 'new york city', 'washington']
    city=input("would you like to see data for chicago, new york city or washington?").lower()
    while city not in CITY_DATA:
        city = input('Invalid input. Enter city name (chicago, new york city, washington): ').lower()
    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    while True:
        month = input('Enter month name (all, january, february, march, april, may , june): ').lower()
        if month in months:
            break
        else:
            print('Invalid month name. Please try again.')
    day = input('Enter day of week (all, monday, tuesday, ..., sunday): ').lower()
    days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    while day not in days :
        day = input('Invalid day of week. Please try again.').lower()

    print('-'*40)
    return city, month, day





def display_raw_data(df):
    i = 0
    pd.set_option('display.max_columns', None)

    while True:
        show_data = input("\nWould you like to see 5 more rows of data? Enter yes or no: \n").lower()
        if show_data != 'yes':
            print("\nNo more data to show.\n")
            return False 
        print(df.iloc[i:i+5])
        i += 5
        if i >= len(df):
            print("\nNo more data to display.\n")
            return False  
   
   
        
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
   
    df = pd.read_csv(CITY_DATA[city])

    # Convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'].str.lower() == day.lower()]

    return df



def time_stats(df):
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    
    most_common_month = df['month'].mode()[0]
    most_common_day_of_week = df['day_of_week'].mode()[0]
    most_common_start_hour = df['Start Time'].dt.hour.mode()[0]

    print('Most Common Month:', most_common_month)
    print('Most Common Day of Week:', most_common_day_of_week)
    print('Most Common Start Hour:', most_common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)




def station_stats(df):
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    most_common_start_station = df['Start Station'].mode()[0]
    most_common_end_station = df['End Station'].mode()[0]

    print('Most Commonly Used Start Station:', most_common_start_station)
    print('Most Commonly Used End Station:', most_common_end_station)

    # Display most frequent combination of start station and end station trip
    
    df['Trip'] = df['Start Station'] + " to " + df['End Station']
    most_common_trip = df['Trip'].mode()[0]

    print('Most Common Trip:', most_common_trip)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)




def trip_duration_stats(df):
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    
    total_duration = df['Trip Duration'].sum()
    mean_duration = df['Trip Duration'].mean()

    print('Total Travel Time:', total_duration)
    print('Mean Travel Time:', mean_duration)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

   
    user_types = df['User Type'].value_counts()
    print('User Types:\n', user_types)

    # For Gender and Birth Year statistics (if available)
    if 'Gender' in df.columns:
       
        genders = df['Gender'].value_counts()
        print('Genders:\n', genders)


    if 'Birth Year' in df.columns:
        
        earliest_year = df['Birth Year'].min()
        most_recent_year = df['Birth Year'].max()
        most_common_year = df['Birth Year'].mode()[0]

        print('Earliest Year of Birth:', earliest_year)
        print('Most Recent Year of Birth:', most_recent_year)
        print('Most Common Year of Birth:', most_common_year)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        print('-'*40)

        print(f"Selected filters - City: {city.title()}, Month :{month.title()}, Day:{day.title()}")
        df = load_data(city, month, day)

        display_raw_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            print("\nThank you for using the Bikeshare Analysis! Goodbye")
            break



if __name__ == "__main__":
	main()
  