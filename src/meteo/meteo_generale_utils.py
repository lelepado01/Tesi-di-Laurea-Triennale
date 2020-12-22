
# Le funzioni restituiscono un dataframe in cui vengono filtrati i campi 
# che non corrispondono all'anno / mese / giorno

import pandas as pd

def get_weather_by_year(meteo : pd.DataFrame, year : int) -> pd.DataFrame: 
    return meteo[meteo['Date_Time'].map(lambda x : int(x.split(' ')[0].split('/')[2]) == year)]

def get_weather_by_month(meteo : pd.DataFrame, month : int) -> pd.DataFrame: 
    return meteo[meteo['Date_Time'].map(lambda x : int(x.split(' ')[0].split('/')[0]) == month)]

def get_weather_by_day(meteo : pd.DataFrame, day : int) -> pd.DataFrame: 
    return meteo[meteo['Date_Time'].map(lambda x : int(x.split(' ')[0].split('/')[1]) == day)]

def get_hour(meteo : pd.Series) -> pd.Series: 
    return meteo['Date_Time'].map(lambda x : x.split(' ')[1])

def get_less_hours(hours : pd.Series, jump : int) -> pd.Series: 
    for index in range(0, len(hours)):
        if index % jump != 0: 
            hours = hours.replace(hours.iloc[index], '')

    return hours