import pandas as pd

# Compute descriptive statistics
def descriptive_stats(df):
    print(df.describe())

# Analyze driver standings
def driver_performance_analysis(df):
    print(df.groupby('driverId')['points'].sum().sort_values(ascending=False))

if __name__ == "__main__":
    from data_preparation import load_data, clean_data
    data = load_data()
    clean_data(data)
    
    driver_standings = data['driver_standings']
    descriptive_stats(driver_standings)
    driver_performance_analysis(driver_standings)
