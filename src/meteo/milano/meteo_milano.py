
import pandas as pd
import matplotlib.pyplot as plt
import sys
sys.path.append("src")

import meteo.meteo_generale_utils as mgu

meteo = pd.read_csv("dataset/meteo/meteo_milano_generale_2008_2019.csv")

meteo_2010 = mgu.get_weather_by_year(meteo, 2010)

print(meteo_2010)