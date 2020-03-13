import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    

    
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    
    
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york, washington). HINT: Use a while loop to handle invalid inputs
    cities=['chicago','new york','washington']


    while True:
        city=input("Please enter a city (Chicago, New York, Washington): ").lower()
        if city in cities:
            print("You have chosen city: ", city)
            break
        else:
            print("Enter valid city.")
      
         
    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['january', 'february', 'march', 'april', 'may', 'june','all']
          
    while True:
        month=input("Enter month: ").lower()
        if month in months:
            print("You have selected the month of",month)
            break
        else:
            print("Enter a valid month.")
            
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days_of_week=['monday','tuesday','wednesday','thursday','friday','saturday','sunday','all']
              
    while True:
        day=input("Enter day of week: ").lower()
        if day in days_of_week:
            print("You chose day: ",day)
            break
        else: 
            print("Enter valid day of week.")
         
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
    #load data into dataframe
    df=pd.read_csv(CITY_DATA[city])
    
    #convert the Start Time to datetime format
    df['Start Time']=pd.to_datetime(df['Start Time']) 
    #convert the End Time to datetime format
    df['End Time']=pd.to_datetime(df['End Time']) 
    #extract the month number to create new column
    df['month']=df['Start Time'].dt.month 
    #extract the day name to create new column
    df['day']=df['Start Time'].dt.weekday_name
    #extract the hour as number to create new column
    df['hour']=df['Start Time'].dt.hour
    
    # filter by month if applicable
    if month !='all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month=months.index(month)+1
        
       # filter by month to create the new dataframe
        df = df[df['month'] == month]
    
    #filter by day of the week if applicable
    if day !='all':
        # filter by day of week to create the new dataframe
        df = df[df['day'] == day.title()]
     
       
          
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    months = ['january', 'february', 'march', 'april', 'may', 'june','all']
    #days_of_week=['monday','tuesday','wednesday','thursday','friday','saturday','sunday','all']
    
    
    # TO DO: display the most common month
    most_common_month=df['month'].mode()[0]
    print("Most common month is: ",months[most_common_month])                  

    # TO DO: display the most common day of week 
    df['day']=df['Start Time'].dt.weekday_name #extract Weekday name
    most_common_day=df['day'].mode()[0]
    print("Most common day is: ",most_common_day)                  



    # TO DO: display the most common start hour
    df['hour']=df['Start Time'].dt.hour #extract hour number
    most_common_hour=df['hour'].mode()[0]              
    print("Most common start hour: ",most_common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station=df['Start Station'].mode()[0]
    print("The most common Start Station: ", most_common_start_station)

    # TO DO: display most commonly used end station
    most_common_end_station=df['End Station'].mode()[0]
    print("The most common End Station: ", most_common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    
    #Create new column that combines "Start Station" and "End Station" columns
    df['combo_station']=df['Start Station'] + ' with ' + df['End Station']
    
    #Determine most common entry from 'combo_station'
    most_common_station_combo=df['combo_station'].mode()[0]
    print("The most frequent combination of start/end station trip: ",most_common_station_combo)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
       
    
    #Create column that shows subtracts converted End/Start time 
    df['travel_time']=df['End Time']-df['Start Time']
    
    # TO DO: display total travel time
    #Sum of new column
    total_travel=df['travel_time'].sum() 
    print("Total travel time: ",total_travel)

    # TO DO: display mean travel time
    mean_travel=df['travel_time'].mean() 
    print("Mean travel time: ",mean_travel)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    #Adding some more code to satisfy requirements...


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
 
    # TO DO: Display counts of user types
    user_types=df['User Type'].value_counts()
    print("Breakdown of User Types: ")
    print(user_types)
    print("")
            
    # TO DO: Display counts of gender
    gender_count=df['Gender'].value_counts()
    print("Breakdown of Genders: ")
    print(gender_count)
    print("")

    # TO DO: Display earliest, most recent, and most common year of birth
    print("")
    #Earliest birth year
    earliest_birth=df['Birth Year'].min()
    print("Earliest birth year: ",earliest_birth)

    #Most recent birth year
    recent_birth=df['Birth Year'].max()
    print("Most recent birth year: ",recent_birth)
    
    #Most common birth year
    common_birth=df['Birth Year'].mode()[0]
    print("Most common birth year: ",common_birth)
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    #Adding some comments to satisfy course requirements

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
