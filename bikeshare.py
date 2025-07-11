import time
import pandas as pd
import numpy as np


import time

CITY_DATA = {
    'chicago': 'chicago.csv',
    'new york city': 'new_york_city.csv',
    'washington': 'washington.csv'
}

def get_filters():
    """Prompt for city, month, and day with robust validation."""
    print("Hello! Let's explore some US bikeshare data!")

    # Validate city
    while True:
        city = input("Choose a city (Chicago, New York City, Washington): ").strip().lower()
        if city in CITY_DATA:
            break
        print("Invalid city. Please enter Chicago, New York City, or Washington.")

    # Validate month
    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    while True:
        month = input("Enter month (all or January–June): ").strip().lower()
        if month in months:
            break
        print("Invalid month. Please select from: all, January–June.")

    # Validate day
    days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday',
            'friday', 'saturday', 'sunday']
    while True:
        day = input("Enter day of week (all or Monday–Sunday): ").strip().lower()
        if day in days:
            break
        print("Invalid day. Please enter a full weekday name or 'all'.")

    print("-" * 40)
    return city, month, day

def load_data(city, month, day):
    """Load city data and apply filters."""
    try:
        df = pd.read_csv(CITY_DATA[city])
    except FileNotFoundError:
        raise FileNotFoundError(f"Data file for {city} not found.")

    df['Start Time'] = pd.to_datetime(df['Start Time'], errors='coerce')
    df = df.dropna(subset=['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name().str.lower()

    if month != 'all':
        df = df[df['month'] == ['january','february','march','april','may','june'].index(month) + 1]

    if day != 'all':
        df = df[df['day_of_week'] == day]

    return df

# (Other functions unchanged: display_raw_data, time_stats, etc.)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        display_raw_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        if input("\nRestart? Enter yes to continue: ").strip().lower() != 'yes':
            print("\nThank you for using the Bikeshare Analysis Tool. Goodbye!")
            break

if __name__ == "__main__":
    main()
  