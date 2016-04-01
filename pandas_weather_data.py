#http://synesthesiam.com/posts/an-introduction-to-pandas.html#accessing-individual-rows

import pandas as pd
weather_data = pd.read_csv("/Users/shruti/Desktop/WorkMiscellaneous/OnlineCourses/Python/pandas/weather_year.csv")

print "head of dataframe: %s \n" % weather_data.head()
print "dimension of dataframe: %s \n" % (weather_data.shape,) #dim
print "number of rows of dataframe: %s \n" % len(weather_data) # nrows
print "column names of dataframe: %s \n" % weather_data.columns # colnames
print "row names of dataframe: %s \n" % weather_data.index # rownames
print "first 5 rows of column EDT of dataframe: \n %s \n" % weather_data[0:5]["EDT"]
print "first 5 rows of column EDT of dataframe: \n %s \n" % weather_data.EDT[0:5]
print "first 5 rows of column EDT and Mean TemperatureF of dataframe: \n %s \n" % weather_data[0:5][["EDT","Mean TemperatureF"]]
print "first 5 rows of column EDT and Mean TemperatureF of dataframe: \n %s \n" % weather_data[["EDT","Mean TemperatureF"]].head(5)

# rename the columns
weather_data.columns = ["date", "max_temp", "mean_temp", "min_temp", "max_dew",
                "mean_dew", "min_dew", "max_humidity", "mean_humidity",
                "min_humidity", "max_pressure", "mean_pressure",
                "min_pressure", "max_visibilty", "mean_visibility",
                "min_visibility", "max_wind", "mean_wind", "min_wind",
                "precipitation", "cloud_cover", "events", "wind_dir"]

print "summary report for each column: \n %s \n" % weather_data.describe()
print "standard deviation for each column: \n%s \n" % weather_data.std()
print "head of column - mean_temp: \n%s \n" % weather_data.mean_temp.head()
print "standard deviation of column - mean_temp. ignore missing values like NaN: \n%s \n" % weather_data.mean_temp.std()
#TODO: following not working
#  print "histogram of of column - mean_temp: \n%s \n" % weather_data.mean_temp.hist()

# bulk functions using apply
print weather_data.date.head()
# use the "values" property of the column to get a list of values for the column.
print weather_data.date.values[0]
print weather_data.date.values[0:4]

# convert date into string
from datetime import datetime
first_date = weather_data.date.values[0]
print datetime.strptime(first_date,"%Y-%m-%d")
data_date_asString = weather_data.date.apply(lambda d: datetime.strptime(d, "%Y-%m-%d"))
print data_date_asString.head()
# use dates instead of integers for rownames - index
weather_data.index = data_date_asString
print weather_data.head()
# look up a row by its date with the ix[] property.
print weather_data.ix[datetime(2012, 8, 19)]
# drop date column
weather_data = weather_data.drop(["date"], axis=1) # axis=1 in order to drop a column
print weather_data.columns

# handling missing values
print "head of events column - events \n %s" % weather_data.events.head()
print "head of events column - events without missing data \n %s" % weather_data.events.dropna().head()

print "dimension of events column - events: %s \n" %  weather_data.events.shape
print "dimension of events column - events without missing data %s \n " %  weather_data.events.dropna().shape

print "dimension of dataframe %s \n" % (weather_data.shape,)
print "dimension of dataframe without missing data %s \n" %  (weather_data.dropna().shape,)

print weather_data.events.head()
print weather_data.events.isnull().head()
empty = weather_data.apply(lambda col: pd.isnull(col))
print empty.events.head()
print empty.shape
print weather_data.dropna(subset=["events"]).shape
print weather_data.dropna(subset=["events"])

weather_data.events = weather_data.events.fillna("")
print weather_data.events.head(10)

# accessing rows
print weather_data.irow(0)
#print weather_data.idx[0]
print weather_data.ix["2012-03-10"]
print weather_data.events.value_counts("Rain") #similar to table in R
# iterate over each row in the DataFrame with iterrows()
rain_count = 0
for idx, row in weather_data.iterrows():
    if "Rain" in row["events"]:
        rain_count +=1

print "days with rain: {0}".format(rain_count)

# filtering / subsetting
freezing_days = weather_data[weather_data.max_temp <=32]
print freezing_days.head()
print freezing_days[freezing_days.min_temp >=20]