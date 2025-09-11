# Necessary library imports
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
import numpy as np

# Data import and cleanup
rideData = pd.read_csv('WaitTimeData.csv')
rideData = rideData.drop(columns = ['Notes'], axis = 1)
rideData['Date'] = pd.to_datetime(rideData['Date'], format = 'mixed')
rideData.astype({'Land':str, 'Ride':str, 'Actual Wait Time':int, 'Used Fastpass':bool})

# Color palette for visualizations
darkBlue = '#12436D'
turquoise = '#28A197'
darkPink = '#801650'
orange = '#F46A25'
darkGrey = '#3D3D3D'
lightPurple = '#A285D1'

# Color palette used from here:
# https://analysisfunction.civilservice.gov.uk/policy-store/data-visualisation-colours-in-charts/#section-3

# Code for graph containing all three days of data
fig, ax = plt.subplots(figsize = (30, 12))
bar_width = 0.4

index = np.arange(len(rideData))

for i, row in rideData.iterrows():
    barColor = turquoise if row['Used Fastpass'] else darkPink

    ax.bar(i - bar_width/2, row['Est. Wait Time'], bar_width, color = darkBlue)
    ax.bar(i + bar_width/2, row['Actual Wait Time'], bar_width, color = barColor)

ax.set_title('Estimated vs. Actual Wait Time', fontsize = 20, fontweight = 'bold', pad = 20)
ax.set_xlabel('Ride', fontsize = 18, labelpad = 25)
ax.set_ylabel('Wait Time (minutes)', fontsize = 18, labelpad = 20)


ax.set_xticks(index)
ax.set_xticklabels(rideData['Ride'], rotation = 45, ha = 'right')

ax.set_yticks(np.arange(0, 65, 5))

ax.set_xbound(-1, 48)

legend_elements = [Patch(facecolor = darkBlue, label = 'Estimated Wait Time'),
                   Patch(facecolor = turquoise, label = 'Lightning Lane Entry'),
                   Patch(facecolor = darkPink, label = 'Standby Line Wait')]

ax.legend(handles = legend_elements, fontsize = 12, loc = 'upper left')

plt.subplots_adjust(bottom = 0.35)
plt.grid(axis = 'y', alpha = 0.45)

plt.savefig('CombinedBarGraph.jpg', format = 'jpg', dpi = 300, bbox_inches = 'tight')

plt.close(fig)

# Code for creating graphs based on the day visited
days_visited = rideData['Date'].dt.date.unique()

dayCount = 1

for date in days_visited:
    daily_plots = rideData[rideData['Date'].dt.date == date]
    daily_plots.reset_index(inplace = True, drop = True)

    fig, ax = plt.subplots(figsize = (30, 12), dpi = 300)
    
    bar_width = 0.4
    index = np.arange(len(daily_plots))

    for i, row in daily_plots.iterrows():
        barColor = turquoise if row['Used Fastpass'] else darkPink

        ax.bar(i - bar_width/2, row['Est. Wait Time'], bar_width, color = darkBlue)
        ax.bar(i + bar_width/2, row['Actual Wait Time'], bar_width, color = barColor)

    ax.set_title(f'Estimated vs. Actual Wait Time ({date.strftime("%m/%d/%Y")})', fontsize = 20, fontweight = 'bold', pad = 30)
    ax.set_xlabel('Ride', fontsize = 20,  labelpad = 40)
    ax.set_ylabel('Wait Time (minutes)', fontsize = 20, labelpad = 20)

    ax.tick_params(labelsize = 14)

    ax.set_xticks(index)
    ax.set_xticklabels(daily_plots['Ride'], rotation = 45, ha = 'right')

    ax.set_yticks(np.arange(0, 65, 5))


    legend_elements = [Patch(facecolor = darkBlue, label = 'Estimated Wait Time'),
                       Patch(facecolor = turquoise, label = 'Lightning Lane Entry'),
                       Patch(facecolor = darkPink, label = 'Standby Line Entry Wait')]

    ax.legend(handles = legend_elements, fontsize = 15, loc = 'upper left')

    plt.subplots_adjust(bottom = 0.35)
    plt.grid(axis = 'y', alpha = 0.25)
    
    plt.savefig(f'Day {dayCount} Graph.jpg', format = 'jpg', dpi = 300, bbox_inches = 'tight')
    dayCount += 1

# Code for creating the summary table

# Calculations for table data
avg_LL_wait = rideData[rideData['Used Fastpass'] == True]['Actual Wait Time'].mean()
avg_standby_wait = rideData[(rideData['Used Fastpass'] == False) & (rideData['Actual Wait Time'] > 0)]['Actual Wait Time'].mean()
longest_wait = rideData['Actual Wait Time'].max()
shortest_wait = rideData[rideData['Actual Wait Time'] > 0]['Actual Wait Time'].min()
avg_time_saved = rideData['Actual Wait Time'].mean() - rideData['Est. Wait Time'].mean()

table_data = {
    'Metric' :[
              'Average LL Wait Time',
              'Average Standby Wait Time',
              'Average Time Saved',
              'Longest Wait',
              'Shortest Wait'
              ],
    'Wait Time (Minutes)' : [
              avg_LL_wait,
              avg_standby_wait,
              abs(avg_time_saved),
              longest_wait,
              shortest_wait
              ]
}

table_df = pd.DataFrame(table_data)
table_df['Wait Time (Minutes)'] = table_df['Wait Time (Minutes)'].round(2)

fix, ax = plt.subplots(figsize = (8, 4), dpi = 300)
ax.axis('off')

table = ax.table(cellText = table_df.values,
                 colLabels = table_df.columns,
                 loc = 'center',
                 cellLoc = 'center')

# Style the table
table.set_fontsize(12)
table.scale(1.5, 1.5)

for (i, j), cell in table.get_celld().items():
    if i == 0: 
        cell.set_facecolor("#40466e")
        cell.set_text_props(weight = 'bold', color = 'white')

plt.title('Quick Summary', fontsize = 16, y = 0.85, color = 'black')

plt.savefig('Summary Table.jpg', format = 'jpg', dpi = 300, bbox_inches = 'tight')