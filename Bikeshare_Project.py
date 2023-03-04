
import time
import datetime 
import pandas as pd
import numpy as np


CITY_DATA = {  'chicago': 'C:\\Users\\EOAghogho\\Documents\\UDACITY\\Intro_To_Python\\Bikeshare_Data\\chicago.csv',
    'new york city': 'C:\\Users\\EOAghogho\\Documents\\UDACITY\\Intro_To_Python\\Bikeshare_Data\\new_york_city.csv',
    'washington': 'C:\\Users\\EOAghogho\\Documents\\UDACITY\\Intro_To_Python\\Bikeshare_Data\\washington.csv'
 }

# lists for month and day to check user input validity
month_list = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
weekday_list = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

def get_filters():
    
    #print('Hello! Let\'s explore some US bikeshare data!')
    city =''
    # get user input for city (chicago, new york city, washington), and check user input validity
    while city not in CITY_DATA.keys():
        print("\nWelcome to US Bikeshare data program!")
        print("\n1. Chicago 2. New York City 3. Washington")
        print("\nPlease enter the name of your city from any of the above")
        city = input().lower()
        
        if city not in ['chicago', 'new york city', 'washington']:
            print("Invalid Input!, Please enter any of: Chicago, New York City or Washington")
            print("\nRestarting...")
            
    print(f"\nYou have entered {city.title()} as your city.")            
    
    
    # get user input for month (all, january, february, march, april, may, june), and check for user input validity
    month = ''
    while month not in month_list:
        print("\nPlease enter the month of your choice from January to June or 'all'for all months:")
        month = input().lower()
        
        if month not in month_list:
            print("Invalid Input!, Please enter any of: january, february, march, april, may, june or all")
            print("\nRestarting...")
        
    print(f"\nYou have entered {month.title()}.")
    
    # get user input for day of week (all, monday, tuesday, wednesday, thursday, friday, saturday, sunday), and check user input validity
    day = ''
    while day not in weekday_list:
        print("\nPlease enter any day of your choice or enter 'all' to view all days of the week")
        day = input().lower()
        
        if day not in weekday_list:
            print("Invalid Input!, Please enter any of: monday, tuesday, wednesday, thursday, friday, saturday, sunday or all")
            print("\nRestarting...")
            
    print(f"\nYou have entered {day.title()}.")
    
    print('-' * 40)
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
    
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # extract month, day of week and Hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name
    df['hour'] = df['Start Time'].dt.hour
  
    # extract month, day of week and Hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour
     

    return df
    

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    # display the most common month
    most_common_month = df['month'].mode()[0]
    print('Most common month is:', most_common_month)
    
    # display the common day of week
    most_common_day = df['day_of_week'].mode()[0]
    print('Most common day of week is: ', most_common_day)
    
    # display the most common start hour
    most_common_hour = df['hour'].mode()[0]
    print('Most common start hour of day is: ', most_common_hour)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)
    
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    
    # display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print('Most common start station is: ', most_common_start_station)
    
    # display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print('Most common end station is: ', most_common_end_station)
    
    # display most frequent combination of start station and end station trip
    # Result may not be sorted for the most frequent combination. The result to be in descending order
    combination_group = df.groupby(['Start Station', 'End Station'])
    most_frequent_combination_station = combination_group.size().sort_values(ascending = False).head(1)
    print('Most frequent combination of start station and end station trip is: ', most_frequent_combination_station)
    
    # top 5 most used stations
    top_five_start_station = df['Start Station'].value_counts(5)
    print('Top five most common start stations are: \n{}'.format(df['Start Station'].value_counts()))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)
    
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total Travel Time:', total_travel_time, ' seconds, or ', total_travel_time/3600, 'hours')
    
    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean travel time is:', mean_travel_time, ' seconds, or ', mean_travel_time/3600, 'hours') 
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def user_stats(df,city):
    """Displays statistics on bikeshare users."""
    
    print('\nCalculating users stats...\n')
    start_time = time.time()
    
    # display counts of user types
    print('User type in data are: \n{}'.format(df['User Type'].value_counts()))
    
    # ensure that city is not washington, since gender and birth year column are not in washington data
    if city != 'washington':
        # display counts of gender
        print('Counts of gender: \n{}'.format(df['Gender'].value_counts()))
        
        # display earliest, most recent, and most common year of birth
        earliest_year = df['Birth Year'].min()
        print("Earliest year is:%d" %(earliest_year))
        
        # youngest users
        most_recent_year = df['Birth Year'].max()
        print("Most recent year is:%d" %(most_recent_year))
        
        # most common birth year of users
        most_common_year = df['Birth Year'].mode()[0]
        print("Most common year is:%d" %(most_common_year))
        
        # number of users missing user type data
        number_missing_user_type_info = df['User Type'].isnull().sum()
        print("Number of missing user type data is:%s" % (number_missing_user_type_info))
        
        # number of users missing gender
        number_missing_gender_info = df['Gender'].isnull().sum()
        print("Number of missing gender data is:%s" % (number_missing_gender_info))
        
        # number of users missing birth year data
        number_missing_birth_year = df['Birth Year'].isnull().sum()
        print("Number of missing birth year data is:%s" % (number_missing_birth_year))
        
    print("\nThis took {} seconds.".format(time.time() - start_time))
    print('-' * 40)
    
# view raw data to user 
def show_row_data(df):
    row = 0
    while True:
        view_raw_data = input("Would you like to see more raw data? Please enter 'yes' or 'no':").lower()
        # row = 0
        if view_raw_data == "yes":
            
            print(df.iloc[row : row + 6])
            row += 6
        elif view_raw_data == "no":
            break
        else: # validate user input
            print("Sorry! You entered wrong input, Please try Again!")
        
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        show_row_data(df)
        
        restart = input('\nWould you like to restart? Please enter yes or no.\n').lower()
        if restart.lower() != 'yes':
            break
   
            
if __name__ == "__main__":
	main()