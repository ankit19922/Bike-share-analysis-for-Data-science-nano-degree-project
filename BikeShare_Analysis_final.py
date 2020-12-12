import pandas as pd
import numpy as np
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

def validate_city(name):
    if name.lower() == 'chicago' or name.lower() == 'newyork' or name.lower() == 'washington':
        # data = pd.read_csv(data[name.lower()])
        print('City name is :', name)



    else:
        print('Enter valid city name\n ')
        city_names()

def data_read(name):
    data = {'chicago': 'F:/chicago.csv', 'newyork': 'F:/new_york_city.csv', 'washington': 'F:/washington.csv'}
    if name.lower() == 'chicago' or name.lower() == 'newyork' or name.lower() == 'washington':
        data = pd.read_csv(data[name.lower()])
    return data

def city_names():
    global city
    city = input('Please enter the city for which you want to see details of Chicago,Washington & Newyork ?\n')
    validate_city(city)


def validate_filter(option):
    global selected_month
    global selected_week
    if option.lower() == 'month':
        print('Analysis will be performed by :', option)
        selected_month = input('Enter the first 3 initials of the month name for which you want to perform analysis\n')
        if selected_month.lower() == 'jan' or selected_month.lower() == 'feb' or selected_month.lower() == 'mar' or selected_month.lower() == 'apr' or selected_month.lower() == 'may' or selected_month.lower() == 'jun' or selected_month.lower() == 'jul' or selected_month.lower() == 'aug' or selected_month.lower() == 'sep' or selected_month.lower() == 'oct' or selected_month.lower() == 'nov' or selected_month.lower() == 'dec':
            print('Analysis will be performed for the month \n', selected_month)
        else:
            print('Enter valid month name \n')
            filter_type()

    elif option.lower() == 'week':
        print('Analysis will be performed by :', option)
        selected_week = input('Enter the first 3 initials of the week names for which you want to perform analysis\n')
        if selected_week.lower() == 'mon' or selected_week.lower() == 'tue' or selected_week.lower() == 'wed' or selected_week.lower() == 'thu' or selected_week.lower() == 'fri' or selected_week.lower() == 'sat' or selected_week.lower() == 'sun':
            print('Analysis will be performed for the week \n', selected_week)
        else:
            print('Enter valid week name')
            filter_type()


    elif option.lower() == 'both':
        print('Analysis will be performed by :', option)
        selected_month = input('Enter the first 3 initials of the month name  for which you want to perform analysis\n')
        if selected_month.lower() == 'jan' or selected_month.lower() == 'feb' or selected_month.lower() == 'mar' or selected_month.lower() == 'apr' or selected_month.lower() == 'may' or selected_month.lower() == 'jun' or selected_month.lower() == 'jul' or selected_month.lower() == 'aug' or selected_month.lower() == 'sep' or selected_month.lower() == 'oct' or selected_month.lower() == 'nov' or selected_month.lower() == 'dec':
            print('Analysis will be performed for the month \n', selected_month)
        else:
            print('Enter valid month name')
            filter_type()
        selected_week = input('Enter the first 3 initials of the week names  for which you want to perform analysis\n')
        if selected_week.lower() == 'mon' or selected_week.lower() == 'tue' or selected_week.lower() == 'wed' or selected_week.lower() == 'thu' or selected_week.lower() == 'fri' or selected_week.lower() == 'sat' or selected_week.lower() == 'sun':
            print('Analysis will be performed for the week \n', selected_week)
        else:
            print('Enter valid week name')
            filter_type()
        print('Analysis will be performed for both month & week (i.e)', selected_month, selected_week)


    else:
        print('Enter valid value \n')
        filter_type()


def filter_type():
    global selection
    selection = input('How do you want to see the analysis by Month,Week or Both\n')
    validate_filter(selection)


def arranging_useful(data):
    data['Start Time'] = pd.to_datetime(data['Start Time'],infer_datetime_format=True).copy()
    data['End Time'] = pd.to_datetime(data['End Time'],infer_datetime_format=True).copy()
    data['Weekdays'] = data['Start Time'].dt.weekday.copy()
    data['Hours'] = data['Start Time'].dt.hour.copy()
    data['Months'] = data['Start Time'].dt.month.copy()
    data['Months'] = data['Months'] - 1
    data = data.dropna(axis=0).copy()

    weekdays = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
    weekdays_dict = {keys: weekdays[keys] for keys in range(7)}

    def day_of_weeks(idx):
        return weekdays_dict[idx]

    data['Weekdays'] = data['Weekdays'].apply(day_of_weeks)

    months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
    months_dict = {numbers: months[numbers] for numbers in range(12)}

    def Month_of_year(idx):
        return months_dict[idx]

    data['Months'] = data['Months'].apply(Month_of_year)

    return data


def data_calculation(filtered_data):
        print('Calculating first statistic............................!')
        popular_hour=filtered_data['Hours'].mode()[0]
        print('Most Popular hour is :',popular_hour)
        
        if selection.lower() == 'week':
            common_month=filtered_data['Months'].mode()[0]
            print('Most common Month is',common_month)
        elif selection.lower() == 'month':
            common_week=filtered_data['Weekdays'].mode()[0]
            print('Most common week is',common_week)
        
        print('Calculating Second statistic related to Stations.............!')
        popular_start_station=filtered_data['Start Station'].mode()[0]
        print('Most popular Start Station is : ', popular_start_station)

        popular_end_station=filtered_data['End Station'].mode()[0]
        print('Most popular End Station is : ', popular_end_station)
    
        print('Calculating Third statistic related to Trip Time.............!')
    
    
        total_time=filtered_data['Trip Duration'].sum()
        print('Total Duration is (seconds) : ',total_time )
    
        average_time=filtered_data['Trip Duration'].mean()
        print('Average time taken is (seconds) :',average_time)
        
        print('Calculating Forth an Last statistic related to User info.....!')
    
    
        user_type=filtered_data['User Type'].value_counts()
        print('What is breakdown of Users :',user_type)
        
        if city.lower()=='chicago' or city.lower()=='newyork':
            Gender_count=filtered_data['Gender'].value_counts()
            print('What is breakdown of Genders :',Gender_count)
            oldest_year=filtered_data['Birth Year'].min()
            youngest_year=filtered_data['Birth Year'].max()
            popular_year=filtered_data['Birth Year'].mode()[0]
            print('Oldest,Youngest and most Popular years are : ', youngest_year,oldest_year,popular_year)
        else:
            print('Thanks Have a nice day')
    


        
def main():
    while True:
        city_names()
        filter_type()
        data = arranging_useful(data_read(city))
        if selection.lower() == 'month':
            mnth=data['Months']
            mn=np.array(mnth)
            if selected_month.lower() in mn:
                filtered_data = data[(data['Months'] == selected_month.lower())]
                data_calculation(filtered_data)
            else:
                print('Entered  month input is not the part of dataset')

        elif selection.lower() == 'week':
            wekday=data['Weekdays']
            wd=np.array(wekday)
            if selected_week.lower() in wd:
                filtered_data = data[(data['Weekdays'] == selected_week.lower())]
                data_calculation(filtered_data)
            else:
                print('Entered  weekday input is not the part of dataset')
        
        elif selection.lower() == 'both':
            mnth=data['Months']
            mn=np.array(mnth)
            wekday=data['Weekdays']
            wd=np.array(wekday)
            if selected_month.lower() in mn and selected_week.lower() in wd:
                filtered_data = data[(data['Months'] == selected_month.lower()) & (data['Weekdays'] == selected_week.lower())]
                data_calculation(filtered_data)
            else:
                print('Either month or week input is not a part of dataset!')
                
                
                        
        
        restart=input('You want to restart the process again yes/no')
        
        if restart.lower()!='yes':
            break
    

    

    
    

main()