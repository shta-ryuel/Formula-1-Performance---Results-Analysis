import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Plot top N drivers by total points
def plot_top_drivers_by_points(df, top_n=10):
    """
    Plots the top N drivers by total points.
    Args:
    - df: DataFrame containing driver standings data.
    - top_n: Number of top drivers to plot.
    """
    if df.empty or 'driverId' not in df.columns or 'points' not in df.columns:
        print("Error: Missing required columns or data is empty.")
        return
    
    plt.figure(figsize=(12, 6))
    driver_points = df.groupby('driverId')['points'].sum().reset_index()
    driver_points = driver_points.sort_values(by='points', ascending=False).head(top_n)
    
    driver_names = pd.read_csv('drivers.csv')[['driverId', 'surname']]
    driver_points = pd.merge(driver_points, driver_names, on='driverId', how='left')
    
    # Update sns.barplot to avoid the deprecation warning
    sns.barplot(x='points', y='surname', data=driver_points, hue='surname', palette="viridis", legend=False)
    
    plt.title(f'Top {top_n} Drivers by Total Points')
    plt.xlabel('Total Points')
    plt.ylabel('Driver')
    plt.tight_layout()
    plt.show()
    plt.close()


# Plot constructor performance over time
def plot_constructor_performance(df, constructors_df, top_n=10):
    """
    Plots constructor performance over time using a scatter plot, showing only top N constructors.
    Args:
    - df: DataFrame containing race results.
    - constructors_df: DataFrame containing constructor names.
    - top_n: Number of top constructors to display.
    """
    if df.empty or constructors_df.empty:
        print("Error: Data is empty.")
        return
    
    # Grouping by constructor and season/year and summing points
    standings = df.groupby(['constructorId', 'raceId'])['points'].sum().reset_index()
    
    # Merging with constructor names
    standings = pd.merge(standings, constructors_df[['constructorId', 'name']], on='constructorId', how='left')
    
    # Summing points over time and selecting the top N constructors
    total_points_by_constructor = standings.groupby('name')['points'].sum().reset_index()
    top_constructors = total_points_by_constructor.sort_values(by='points', ascending=False).head(top_n)
    
    # Filter data for the top N constructors
    filtered_standings = standings[standings['name'].isin(top_constructors['name'])]
    
    # Plotting the performance over time using a scatter plot
    plt.figure(figsize=(12, 8))
    sns.scatterplot(data=filtered_standings, x='raceId', y='points', hue='name', style='name', s=100)

    plt.title(f'Top {top_n} Constructors Performance Over Time')
    plt.xlabel('Race ID / Season')
    plt.ylabel('Points')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    plt.close()


# Plot race position distribution
def plot_race_positions(df):
    """
    Plots the distribution of race positions.
    Args:
    - df: DataFrame containing race result data.
    """
    if df.empty or 'positionOrder' not in df.columns:
        print("Error: Missing 'positionOrder' column.")
        return
    
    plt.figure(figsize=(12, 6))
    sns.histplot(df['positionOrder'], bins=20, kde=False, color="skyblue")
    plt.title('Distribution of Race Positions')
    plt.xlabel('Position Order')
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.show()
    plt.close()

# Fastest Laps by Driver
def plot_fastest_laps(df, drivers_df):
    """
    Plots a line plot of the number of fastest laps by each driver.
    
    Args:
    - df: DataFrame containing race results, including fastest laps.
    - drivers_df: DataFrame containing driver information.
    """
    if df.empty or drivers_df.empty:
        print("Error: Data is empty.")
        return
    
    # Count the number of fastest laps by each driver
    fastest_laps = df.groupby('driverId')['fastestLap'].count().reset_index()
    fastest_laps = fastest_laps.sort_values(by='fastestLap', ascending=False).head(10)
    
    # Merge with driver names
    fastest_laps = pd.merge(fastest_laps, drivers_df[['driverId', 'surname']], on='driverId', how='left')
    
    # Plotting
    plt.figure(figsize=(12, 6))
    sns.lineplot(x='surname', y='fastestLap', data=fastest_laps, marker='o', color='green')
    
    # Adding titles and labels
    plt.title('Top 10 Drivers with the Most Fastest Laps')
    plt.xlabel('Driver')
    plt.ylabel('Number of Fastest Laps')
    plt.xticks(rotation=45)
    
    # Tidy up layout and show plot
    plt.tight_layout()
    plt.show()
    plt.close()


# Driver Nationalities: Distribution of drivers by nationality
def plot_driver_nationalities(drivers_df):
    
    if drivers_df.empty or 'nationality' not in drivers_df.columns:
        print("Error: Missing 'nationality' column.")
        return
    
    plt.figure(figsize=(8, 8))
    nationality_counts = drivers_df['nationality'].value_counts().head(10)
    
    plt.pie(nationality_counts, labels=nationality_counts.index, autopct='%1.1f%%', colors=sns.color_palette("Set3", len(nationality_counts)))
    plt.title('Top 10 Nationalities of Drivers')
    plt.tight_layout()
    plt.show()
    plt.close()

# Seasonal Analysis: Total points scored by constructors per season
def plot_seasonal_constructor_points(results_df, races_df, constructors_df):
    
    if results_df.empty or races_df.empty or constructors_df.empty:
        print("Error: Data is empty.")
        return
    
    # Merging the data
    merged_data = pd.merge(results_df, races_df[['raceId', 'year']], on='raceId', how='left')
    merged_data = pd.merge(merged_data, constructors_df[['constructorId', 'name']], on='constructorId', how='left')
    
    # Summing points over seasons
    season_points = merged_data.groupby(['year', 'name'])['points'].sum().reset_index()

    # Plotting
    plt.figure(figsize=(14, 7))
    sns.lineplot(data=season_points, x='year', y='points', hue='name', marker='o', legend=False)

    plt.title('Constructor Points Over Seasons')
    plt.xlabel('Year')
    plt.ylabel('Total Points')
    plt.tight_layout()
    plt.show()
    plt.close()

# Plot Race Locations using circuits.csv data
def plot_race_locations(circuits_df):
    
    if circuits_df.empty or 'lat' not in circuits_df.columns or 'lng' not in circuits_df.columns:
        print("Error: Missing latitude or longitude columns.")
        return

    # Plotting the locations on a map
    plt.figure(figsize=(12, 8))
    
    # Use a scatter plot to plot the latitude and longitude of each circuit
    sns.scatterplot(data=circuits_df, x='lng', y='lat', hue='country', palette="Set2", s=100, edgecolor='black')

    plt.title('Race Locations on the Map')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.legend(title='Race locations', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.subplots_adjust(right=0.8)
    plt.show()
    plt.close()    

if __name__ == "__main__":
    from data_preparation import load_data, clean_data
    data = load_data()
    clean_data(data)
    
    driver_standings = data['driver_standings']
    constructor_standings = data['constructor_standings']
    results = data['results']
    drivers = data['drivers']
    constructors = data['constructors']
    races = data['races']
    circuits = data['circuits']

    
    plot_top_drivers_by_points(driver_standings)
    plot_constructor_performance(constructor_standings, constructors)
    plot_race_positions(results)
    plot_fastest_laps(results, drivers)
    plot_driver_nationalities(drivers)
    plot_race_locations(circuits)

