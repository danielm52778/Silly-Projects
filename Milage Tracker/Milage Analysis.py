# Importing necessary libraries

import pandas as pd
from datetime import datetime
from meteostat import Daily
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Importing csv file and manually selecting data types
GasData = pd.read_csv('GasData.csv',
                      dtype = {'Invoice #': int,
                                'Starting Milage': int,
                                'Ending Milage': int,
                                'Gas Price': float,
                                'Gallons': float,
                                'Cost': float,
                                'MPG': float,
                                'Mi. Driven': int,
                                'Station': str
                                },
                        parse_dates = ['Date'],
                        date_format = '%m/%d/%y'
                        )


# Importing most up to date weather data starting at 2023 to present day

# Weather station to get data from (Harry Reid Intl.)
station_id = 72386

# Start and end dates for weather data retreival
start = datetime(2023, 1, 1)
end = datetime.now()

# Gathers data
data = Daily(station_id, start, end)

# Imports gathered data into a data frame
WeatherData = data.fetch()

# Clean up for weather data frame
WeatherData = WeatherData.reset_index()
WeatherData = WeatherData.rename(columns={ WeatherData.columns[0]: "Date" })
WeatherData = WeatherData.rename(columns={ WeatherData.columns[1]: "Temp" })

# Only keeps the Date and Temperature column
WeatherData = WeatherData[['Date', 'Temp']]

# Converts temperature column into fahrenheit from celsius
WeatherData['Temp'] = (WeatherData['Temp'] * 9/5) + 32

# Seperates the GasData dataframe into two data frames that contain only
# values from either Costco or Chevron
gasCostco = GasData[GasData['Station'] == 'Costco']

gasChevron = GasData[GasData['Station'] == 'Chevron']


# Creates a double axis plot
fig = make_subplots(specs = [[{'secondary_y' : True}]])

# Adds data points for refuels at costco in red
fig.add_trace(
    go.Scatter(x = gasCostco['Date'],
               y = gasCostco['MPG'],
               name = 'Costco',
               mode = 'markers',
               marker = dict(color = 'red'),
               hovertemplate = 
                            "<b>Refuel Information</b><br>" +           # Title for hovercard
                            "Date: %{x|%d %b %Y}<br>" +                 # Adds date info to hovercard 
                            "MPG: %{y}<br>" +                           # Adds mpg info to hovercard
                            "<extra></extra>",                          # Hides extra information
               ),
    
    secondary_y = False,
)

# Adds data points for refuels at chevron in blue
fig.add_trace(
    go.Scatter(x = gasChevron['Date'],
               y = gasChevron['MPG'],
               name = 'Chevron',
               mode = 'markers',
               marker = dict(color = 'blue'),
               hovertemplate = 
                            "<b>Refuel Information</b><br>" +           # Title for hovercard
                            "Date: %{x|%d %b %Y}<br>" +                 # Adds date info to hovercard on hover
                            "MPG: %{y}<br>" +                           # Adds mpg info to hovercard on hover
                            "<extra></extra>",                          # Hides extra information
               ),
    
    secondary_y = False,
)

# Adds the daily average temperature line to the graph
fig.add_trace(
    go.Scatter(x = WeatherData['Date'],
               y = WeatherData['Temp'],
               name = 'Temperature',
               mode = 'lines',
               opacity = 0.5,
               hoverinfo = 'skip',                                      # disables info on hover
               showlegend = False,                                      # hides line in legend
               line = dict(color = 'grey',
                           width = 1)
               ),
               
    
    secondary_y = True,
)

# Adds plot title and legend text
fig.update_layout(title_text = 'MPG vs. Average Daily Temperature',
                  legend_title_text = 'Station',
                  height = 500,                     # Sets plot height
                  width = 1100,                     # Sets plot width
                  autosize = True)

# Set y-axes titles
fig.update_yaxes(title_text = 'Miles Per Gallon (MPG)', secondary_y = False)
fig.update_yaxes(title_text = 'Average Daily Temperature (ºF)', secondary_y = True)

# Hides grid lines for secondary y-axis
fig['layout']['yaxis2']['showgrid'] = False

# Saves the plot to an html file to share
fig.write_html("MPG vs Daily Temp.html")

# Displays figure
#fig.show()