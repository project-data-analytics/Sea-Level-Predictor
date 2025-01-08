import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np


def draw_plot():
    # CSV: Year,CSIRO Adjusted Sea Level,Lower Error Bound,Upper Error Bound,NOAA Adjusted Sea Level
    # import the data from epa-sea-level.csv with Pandas
    df = pd.read_csv('epa-sea-level.csv')

    # Create a scatter plot with matplotlib: x-axis (Year column) and y-axis (CSIRO Adjusted Sea Level column)
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])
    plt.xlabel('Year')
    plt.ylabel('CSIRO Adjusted Sea Level')

    # Get the slope and y-intercept of the line of best fit with scipy.stats (linregress function).
    # Plot the line of best fit over the top of the scatter plot.
    # Make the line go through the year 2050 to predict the sea level rise in 2050.
    # Perform linear regression
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    # Calculate the line of best fit
    df['Best Fit Line'] = slope * df['Year'] + intercept
    # Create a scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Scatter Plot')
    # Plot the line of best fit
    plt.plot(df['Year'], df['Best Fit Line'], color='red', label='Line of Best Fit')
    # Extend the line of best fit to 2050
    future_years = pd.Series(range(1880, 2051))
    future_sea_levels = slope * future_years + intercept
    # Plot the extended line
    plt.plot(future_years, future_sea_levels, label='Extended Line to 2050')

    # Create second line of best fit:
    # Plot a new line of best fit just using the data from year 2000 through the most recent year in the dataset.
    # Make the line also go through the year 2050 to predict the sea level rise in 2050
    # if the rate of rise continues as it has since the year 2000.
    recent_df = df[df['Year'] >= 2000]
    # Perform linear regression on the recent data
    slope, intercept, r_value, p_value, std_err = linregress(recent_df['Year'], recent_df['CSIRO Adjusted Sea Level'])
    # Calculate the line of best fit for the recent data
    recent_df.loc[:, 'Best Fit Line (2000 onwards)'] = np.round(slope * recent_df['Year'] + intercept, 7)
    # Create a scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Scatter Plot')
    # Plot the original line of best fit
    plt.plot(df['Year'], np.round(slope * df['Year'] + intercept, 7), color='red', label='Line of Best Fit (2000 onwards)')
    # Extend the new line of best fit to 2050
    future_years = pd.Series(range(1880, 2051))
    future_sea_levels = np.round(slope * future_years + intercept, 7)
    # Plot the extended line of best fit (2000 onwards)
    plt.plot(future_years, future_sea_levels, label='Extended Line (2000 onwards)')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    # Show the plot plt.show()
    # Predict the sea level in 2050 with the new line of best fit
    predicted_sea_level_2050 = np.round(slope * 2050 + intercept, 7)

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
